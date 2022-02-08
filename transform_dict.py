import torchio as tio
from collections import defaultdict

transforms = defaultdict(dict)

transforms["affine"]["easy"] = tio.Compose([tio.RandomAffine(scales=(0.5, 2.5), degrees=0, translation=0, p=1)])
transforms["affine"]["medium"] = tio.Compose([tio.RandomAffine(scales=(0.5, 2.5), degrees=0, translation=0, p=1)])
transforms["affine"]["hard"] = tio.Compose([tio.RandomAffine(scales=(0.5, 2.5), degrees=0, translation=0, p=1)])

transforms["intensity"]["easy"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])
transforms["intensity"]["medium"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])
transforms["intensity"]["hard"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])

transforms["artifacts"]["easy"] = tio.Compose([tio.RandomGhosting(num_ghosts=3, axes=(0,1,2), intensity=0.7, p=1)])
transforms["artifacts"]["medium"] = tio.Compose([tio.RandomGhosting(num_ghosts=3, axes=(0,1,2), intensity=0.7, p=1)])
transforms["artifacts"]["hard"] = tio.Compose([tio.RandomGhosting(num_ghosts=3, axes=(0,1,2), intensity=0.7, p=1)])