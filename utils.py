import numpy as np
import SimpleITK as sitk
import torch
from torch.nn import functional
import gc
import os
from natsort import natsorted
from os.path import join


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


def fix_path(path):
    if path[-1] != "/":
        path += "/"
    return path


def load_filenames(img_dir, extensions=None):
    img_filenames = []
    if extensions is not None:
        extensions = tuple(extensions)

    for file in os.listdir(img_dir):
        if extensions is None or file.endswith(extensions):
            img_filenames.append(join(img_dir, file))
    img_filenames = np.asarray(img_filenames)
    img_filenames = natsorted(img_filenames)

    return img_filenames


def load_nifti(filename, return_meta=False, is_seg=False):
    image = sitk.ReadImage(filename)
    image_np = sitk.GetArrayFromImage(image)

    if is_seg:
        image_np = np.rint(image_np)
        image_np = image_np.astype(np.int32)  # In special cases segmentations can contain negative labels, so no np.uint8

    if not return_meta:
        return image_np
    else:
        spacing = image.GetSpacing()
        keys = image.GetMetaDataKeys()
        header = {key:image.GetMetaData(key) for key in keys}
        affine = None  # How do I get the affine transform with SimpleITK? With NiBabel it is just image.affine
        return image_np, spacing, affine, header


def save_nifti(filename, image, spacing=None, affine=None, header=None, is_seg=False, mp_pool=None, free_mem=False):
    if is_seg:
        image = np.rint(image)
        image = image.astype(np.int32)  # In special cases segmentations can contain negative labels, so no np.uint8

    image = sitk.GetImageFromArray(image)

    if header is not None:
        [image.SetMetaData(key, header[key]) for key in header.keys()]

    if spacing is not None:
        image.SetSpacing(list(spacing)[::-1])  # TODO: Keep the reversing of the spacing?

    if affine is not None:
        pass  # How do I set the affine transform with SimpleITK? With NiBabel it is just nib.Nifti1Image(img, affine=affine, header=header)

    if mp_pool is None:
        sitk.WriteImage(image, filename)
        if free_mem:
            del image
            gc.collect()
    else:
        mp_pool.apply_async(_save, args=(filename, image, free_mem,))
        if free_mem:
            del image
            gc.collect()


def _save(filename, image, free_mem):
    sitk.WriteImage(image, filename)
    if free_mem:
        del image
        gc.collect()