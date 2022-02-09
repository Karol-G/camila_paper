import numpy as np
import SimpleITK as sitk
import torch
from torch.nn import functional
import gc
import os
from natsort import natsorted
from os.path import join
import global_mp_pool


def resample(image: np.ndarray, target_shape, is_seg=False) -> np.ndarray:
    if all([i == j for i, j in zip(image.shape, target_shape)]):
        return image

    with torch.no_grad():
        image = torch.from_numpy(image.astype(np.float32)).cuda()
        if not is_seg:
            image = functional.interpolate(image[None, None], target_shape, mode='trilinear')[0, 0]
        else:
            image = functional.interpolate(image[None, None], target_shape, mode='nearest')[0, 0]
    image = image.cpu().numpy()
    torch.cuda.empty_cache()
    return image


def standardize(img_npy: np.ndarray) -> np.ndarray:
    with torch.no_grad():
        img_npy = torch.from_numpy(img_npy.astype(np.float32)).cuda()
        mn = img_npy.mean()
        sd = img_npy.std()
        img_npy -= mn
        img_npy /= sd

    img_npy = img_npy.cpu().numpy()
    torch.cuda.empty_cache()
    return img_npy


def load_filepaths(load_dir, extensions=None, return_path=True, return_extension=True):
    filepaths = []
    if extensions is not None:
        extensions = tuple(extensions)

    for filename in os.listdir(load_dir):
        if extensions is None or filename.endswith(extensions):
            if not return_extension:
                filename = filename.split(".")[0]
            if return_path:
                filename = join(load_dir, filename)
            filepaths.append(filename)
    filepaths = np.asarray(filepaths)
    filepaths = natsorted(filepaths)

    return filepaths


def load_nifti(filename, return_meta=False, is_seg=False):
    image = sitk.ReadImage(filename)
    image_np = sitk.GetArrayFromImage(image)

    if is_seg:
        image_np = np.rint(image_np)
        # image_np = image_np.astype(np.int16)  # In special cases segmentations can contain negative labels, so no np.uint8

    if not return_meta:
        return image_np
    else:
        spacing = image.GetSpacing()
        keys = image.GetMetaDataKeys()
        header = {key:image.GetMetaData(key) for key in keys}
        affine = None  # How do I get the affine transform with SimpleITK? With NiBabel it is just image.affine
        return image_np, spacing, affine, header


def save_nifti(filename, image, spacing=None, affine=None, header=None, is_seg=False, dtype=None, in_background=False):
    if is_seg:
        image = np.rint(image)
        if dtype is None:
            image = image.astype(np.int16)  # In special cases segmentations can contain negative labels, so no np.uint8 by default

    if dtype is not None:
        image = image.astype(dtype)

    image = sitk.GetImageFromArray(image)

    if header is not None:
        [image.SetMetaData(key, header[key]) for key in header.keys()]

    if spacing is not None:
        image.SetSpacing(spacing)

    if affine is not None:
        pass  # How do I set the affine transform with SimpleITK? With NiBabel it is just nib.Nifti1Image(img, affine=affine, header=header)

    if not in_background:
        sitk.WriteImage(image, filename)
    else:
        global_pool, global_pool_results = global_mp_pool.get_pool()
        # global_pool_results.append(global_pool.starmap_async(_save, ((filename, image), )))
        global_mp_pool.queue_job(global_pool.starmap_async, _save, ((filename, image), ))


def _save(filename, image):
    sitk.WriteImage(image, filename)
    os.remove(filename)
    return None
