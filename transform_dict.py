import torchio as tio
from collections import defaultdict

transforms = defaultdict(lambda: defaultdict(dict))

transforms["affine"]["weak"]["random"] = tio.Compose([tio.RandomAffine(scales=(0.8, 1.5), degrees=15, translation=15, isotropic=True, p=1)])
transforms["affine"]["medium"]["random"] = tio.Compose([tio.RandomAffine(scales=(0.5, 2.5), degrees=30, translation=30, isotropic=True, p=1)])
transforms["affine"]["strong"]["random"] = tio.Compose([tio.RandomAffine(scales=(0.5, 2.5), degrees=30, translation=30, isotropic=False, p=1)])

transforms["affine"]["weak"]["identical"] = tio.Compose([tio.OneOf([tio.RandomAffine(scales=(0.8, 0.8), degrees=(15, 15), translation=(15, 15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(0.8, 0.8), degrees=(-15, -15), translation=(15, 15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(0.8, 0.8), degrees=(15, 15), translation=(-15, -15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(0.8, 0.8), degrees=(-15, -15), translation=(-15, -15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(1.5, 1.5), degrees=(15, 15), translation=(15, 15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(1.5, 1.5), degrees=(-15, -15), translation=(15, 15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(1.5, 1.5), degrees=(15, 15), translation=(-15, -15), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(1.5, 1.5), degrees=(-15, -15), translation=(-15, -15), isotropic=True, p=1)
                                                                    ])])
transforms["affine"]["medium"]["identical"] = tio.Compose([tio.OneOf([tio.RandomAffine(scales=(0.5, 0.5), degrees=(30, 30), translation=(30, 30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(0.5, 0.5), degrees=(-30, -30), translation=(30, 30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(0.5, 0.5), degrees=(30, 30), translation=(-30, -30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(0.5, 0.5), degrees=(-30, -30), translation=(-30, -30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(30, 30), translation=(30, 30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(-30, -30), translation=(30, 30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(30, 30), translation=(-30, -30), isotropic=True, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(-30, -30), translation=(-30, -30), isotropic=True, p=1)
                                                                    ])])
transforms["affine"]["strong"]["identical"] = tio.Compose([tio.OneOf([tio.RandomAffine(scales=(0.5, 0.5), degrees=(30, 30), translation=(30, 30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(0.5, 0.5), degrees=(-30, -30), translation=(30, 30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(0.5, 0.5), degrees=(30, 30), translation=(-30, -30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(0.5, 0.5), degrees=(-30, -30), translation=(-30, -30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(30, 30), translation=(30, 30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(-30, -30), translation=(30, 30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(30, 30), translation=(-30, -30), isotropic=False, p=1),
                                                                    tio.RandomAffine(scales=(2.5, 2.5), degrees=(-30, -30), translation=(-30, -30), isotropic=False, p=1)
                                                                    ])])

transforms["intensity"]["weak"]["random"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-3000, 2000))])
transforms["intensity"]["medium"]["random"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-4000, 3000))])
transforms["intensity"]["strong"]["random"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])

transforms["intensity"]["weak"]["identical"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-3000, 2000))])
transforms["intensity"]["medium"]["identical"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-4000, 3000))])
transforms["intensity"]["strong"]["identical"] = tio.Compose([tio.RescaleIntensity(out_min_max=(-5000, 5000))])

transforms["artifacts"]["weak"]["random"] = tio.Compose([tio.RandomGhosting(num_ghosts=(1, 1), axes=(0,1,2), intensity=(0.0, 0.3), p=1),
                                                            tio.RandomSpike(num_spikes=(1, 1), intensity=(0.0, 0.5), p=1),
                                                            tio.RandomBlur(std=(0.0, 0.5), p=1),
                                                            tio.RandomNoise(mean=0, std=(0, 25), p=1)])

transforms["artifacts"]["medium"]["random"] = tio.Compose([tio.RandomGhosting(num_ghosts=(2, 2), axes=(0,1,2), intensity=(0.0, 0.4), p=1),
                                                            tio.RandomSpike(num_spikes=(1, 1), intensity=(0.0, 0.8), p=1),
                                                            tio.RandomBlur(std=(0.0, 0.9), p=1),
                                                            tio.RandomNoise(mean=0, std=(0, 50), p=1)])

transforms["artifacts"]["strong"]["random"] = tio.Compose([tio.RandomGhosting(num_ghosts=(3, 3), axes=(0,1,2), intensity=(0.0, 0.7), p=1),
                                                            tio.RandomSpike(num_spikes=(1, 1), intensity=(0, 1.2), p=1),
                                                            tio.RandomBlur(std=(0, 1.3), p=1),
                                                            tio.RandomNoise(mean=0, std=(0, 75), p=1)])

transforms["artifacts"]["weak"]["identical"] = tio.Compose([tio.RandomGhosting(num_ghosts=(1, 1), axes=(0,1,2), intensity=(0.3, 0.3), p=1),
                                                            tio.RandomSpike(num_spikes=(1, 1), intensity=(0.5, 0.5), p=1),
                                                            tio.RandomBlur(std=(0.5, 0.5), p=1),
                                                            tio.RandomNoise(mean=0, std=(25, 25), p=1)])

transforms["artifacts"]["medium"]["identical"] = tio.Compose([tio.RandomGhosting(num_ghosts=(2, 2), axes=(0,1,2), intensity=(0.4, 0.4), p=1),
                                                            tio.RandomSpike(num_spikes=(1, 1), intensity=(0.8, 0.8), p=1),
                                                            tio.RandomBlur(std=(0.9, 0.9), p=1),
                                                            tio.RandomNoise(mean=0, std=(50, 50), p=1)])

transforms["artifacts"]["strong"]["identical"] = tio.Compose([tio.RandomGhosting(num_ghosts=(3, 3), axes=(0,1,2), intensity=(0.7, 0.7), p=1),
                                                            tio.RandomSpike(num_spikes=(1, 1), intensity=(1.2, 1.2), p=1),
                                                            tio.RandomBlur(std=(1.3, 1.3), p=1),
                                                            tio.RandomNoise(mean=0, std=(75, 75), p=1)])
