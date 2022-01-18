import torchio as tio
import utils
import napari
from napari import Viewer
import os
import numpy as np

filenames = utils.load_filenames("/home/k539i/Documents/datasets/original/COVID19-Challenge/Train/images")
filenames = filenames[:1]

transform = tio.Compose([tio.RandomAffine(scales=(0.5, 0.5), p=1)])

for filename in filenames:
    print(os.path.basename(filename))
    subject = tio.Subject(
        image=tio.ScalarImage(filename)
    )
    subject = transform(subject)
    image = subject["image"].numpy()[0]

image = np.transpose(image, (2, 0, 1))
image = np.rot90(image, k=-1, axes=(1, 2))
image = np.flip(image, axis=2)

viewer = Viewer()
viewer.add_image(image, rgb=False)
napari.run()