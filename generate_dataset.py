import torchio as tio
import utils
import numpy as np
import argparse
from tqdm import tqdm
from os.path import join
from pathlib import Path
import global_mp_pool
from nnunet.dataset_conversion.utils import generate_dataset_json


def generate_dataset(load_image_dir, load_seg_dir, save_dir, task, transform, parallel):
    save_dir = join(save_dir, task)
    if load_seg_dir is not None:
        image_save_path = join(save_dir, "imagesTr")
        seg_save_path = join(save_dir, "labelsTr")
        Path(image_save_path).mkdir(parents=True, exist_ok=True)
        Path(seg_save_path).mkdir(parents=True, exist_ok=True)
    else:
        image_save_path = join(save_dir, "imagesTs")
        Path(image_save_path).mkdir(parents=True, exist_ok=True)

    names = utils.load_filepaths(load_image_dir, return_path=False, return_extension=False)
    names = [name[:-3] for name in names]

    for name in tqdm(names):
        if load_seg_dir is not None:
            image, spacing, affine, header = utils.load_nifti(join(load_image_dir, name + "_ct.nii.gz"), return_meta=True)
            seg = utils.load_nifti(join(load_seg_dir, name + "_seg.nii.gz"), return_meta=False, is_seg=True)
            subject = tio.Subject(
                image=tio.ScalarImage(tensor=image[np.newaxis, ...]),
                seg=tio.LabelMap(tensor=seg[np.newaxis, ...])
            )
        else:
            image, spacing, affine, header = utils.load_nifti(join(load_image_dir, name + "_ct.nii.gz"), return_meta=True)
            subject = tio.Subject(
                image=tio.ScalarImage(tensor=image[np.newaxis, ...])
            )

        subject = transform(subject)

        utils.save_nifti(join(image_save_path, name + "_0000.nii.gz"), subject["image"].numpy(), spacing=spacing, in_background=parallel)
        if load_seg_dir is not None:
            utils.save_nifti(join(seg_save_path, name + ".nii.gz"), subject["seg"].numpy(), spacing=spacing, is_seg=True, dtype=np.uint8, in_background=parallel)

    print("Still saving images in background...")
    global_mp_pool.get_results()
    global_mp_pool.close_pool()
    print("Finished saving images.")

    generate_dataset_json(join(save_dir, 'dataset.json'), join(save_dir, "imagesTr"), None, ("CT",), {0: 'Background', 1: 'GGO'}, task)


if __name__ == '__main__':
    # Strongly recommended to use --parallel. Already only 4 processes decrease generation time from 50 minutes down to 3 minutes.
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--img", required=True, help="Absolute path to the folder with the input images.")
    parser.add_argument('-s', "--seg", required=False, default=None, help="(Optional) Absolute path to the folder with the input segmentation masks.")
    parser.add_argument('-o', "--output", required=True, help="Absolute output path to the folder that should be used for saving")
    parser.add_argument('-t', "--task", required=True, help="The full task name (e.g. Task200_COVID19)")
    parser.add_argument('-p', '--parallel', required=False, default=0, type=int, help="Number of threads to use for parallel processing. 0 to disable multiprocessing.")
    args = parser.parse_args()

    load_image_dir = args.img
    load_seg_dir = args.seg
    output = args.output

    if args.parallel > 0:
        global_mp_pool.init_pool(args.parallel)

    transform = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])

    generate_dataset(load_image_dir, load_seg_dir, output, args.task, transform, args.parallel > 0)
