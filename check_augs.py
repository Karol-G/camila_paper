import torchio as tio
import utils
import napari
from napari import Viewer
import os
import numpy as np
import SimpleITK as sitk

filenames = utils.load_filenames(r"D:\Datasets\camila_paper\COVID19-Challenge\Train\images")
filenames = filenames[:1]

# Set 1
# Case 1: transform = tio.Compose([tio.RandomAffine(scales=(0.5, 2.5), degrees=0, translation=0, p=1)])
# Case 2: transform = tio.Compose([tio.RandomAffine(scales=1, degrees=45, translation=0, p=1)])
# Case 3: transform = tio.Compose([tio.RandomAffine(scales=1, degrees=0, translation=50, p=1)])
# Case 4: transform = tio.Compose([tio.RandomElasticDeformation(num_control_points=10, max_displacement=30, p=1)])

# Set 2
# Case 1: transform = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])
# (This is not a range. The values are fix min max values and need to be adapted over a list with new values and a for loop)

# Set 3
# Case 1: transform = tio.Compose([tio.RandomGhosting(num_ghosts=3, axes=(0,1,2), intensity=0.7, p=1)])
# Case 2: transform = tio.Compose([tio.RandomSpike(num_spikes=3, intensity=5, p=1)])
# Case 3: transform = tio.Compose([tio.RandomBlur(std=1.8, p=1)])
# Case 4: transform = tio.Compose([tio.RandomNoise(mean=0, std=50, p=1)])  # Easy: 50. Middle: 100.  Strong: 200

transform = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])

for filename in filenames:
    print(os.path.basename(filename))
    subject = tio.Subject(
        image=tio.ScalarImage(filename)
    )
    subject = transform(subject)
    image = subject["image"].save(r"D:\Datasets\camila_paper\results\test.nii.gz")

# image = np.transpose(image, (2, 0, 1))
# image = np.rot90(image, k=-1, axes=(1, 2))
# image = np.flip(image, axis=2)
#
# image = sitk.GetArrayFromImage(image)
# viewer = Viewer()
# viewer.add_image(image, rgb=False)
# napari.run()