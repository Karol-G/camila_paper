import torchio as tio
from collections import defaultdict

transforms = defaultdict(lambda: defaultdict(dict))

weak_scales = (0.9, 1.4)
weak_degrees = 5
weak_translation = 15
weak_isotropic = True
transforms["affine"]["weak"]["random"] = tio.Compose([tio.RandomAffine(scales=weak_scales, degrees=weak_degrees, translation=weak_translation, isotropic=weak_isotropic, p=1)])

medium_scales = (0.7, 1.8)
medium_degrees = 8
medium_translation = 20
medium_isotropic = True
transforms["affine"]["medium"]["random"] = tio.Compose([tio.RandomAffine(scales=medium_scales, degrees=medium_degrees, translation=medium_translation, isotropic=medium_isotropic, p=1)])

strong_scales = (0.6, 2)
strong_degrees = 9
strong_translation = 20
strong_isotropic = False
transforms["affine"]["strong"]["random"] = tio.Compose([tio.RandomAffine(scales=strong_scales, degrees=strong_degrees, translation=strong_translation, isotropic=strong_isotropic, p=1)])

transforms["affine"]["weak"]["identical"] = tio.Compose([tio.OneOf([tio.RandomAffine(scales=(weak_scales[0], weak_scales[0]), degrees=(weak_degrees, weak_degrees),
                                                                                     translation=(weak_translation, weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[0], weak_scales[0]), degrees=(-weak_degrees, -weak_degrees),
                                                                                     translation=(weak_translation, weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[0], weak_scales[0]), degrees=(weak_degrees, weak_degrees),
                                                                                     translation=(-weak_translation, -weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[0], weak_scales[0]), degrees=(-weak_degrees, -weak_degrees),
                                                                                     translation=(-weak_translation, -weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[1], weak_scales[1]), degrees=(weak_degrees, weak_degrees),
                                                                                     translation=(weak_translation, weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[1], weak_scales[1]), degrees=(-weak_degrees, -weak_degrees),
                                                                                     translation=(weak_translation, weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[1], weak_scales[1]), degrees=(weak_degrees, weak_degrees),
                                                                                     translation=(-weak_translation, -weak_translation), isotropic=weak_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(weak_scales[1], weak_scales[1]), degrees=(-weak_degrees, -weak_degrees),
                                                                                     translation=(-weak_translation, -weak_translation), isotropic=weak_isotropic, p=1)
                                                                    ])])
transforms["affine"]["medium"]["identical"] = tio.Compose([tio.OneOf([tio.RandomAffine(scales=(medium_scales[0], medium_scales[0]), degrees=(medium_degrees, medium_degrees),
                                                                                     translation=(medium_translation, medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[0], medium_scales[0]), degrees=(-medium_degrees, -medium_degrees),
                                                                                     translation=(medium_translation, medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[0], medium_scales[0]), degrees=(medium_degrees, medium_degrees),
                                                                                     translation=(-medium_translation, -medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[0], medium_scales[0]), degrees=(-medium_degrees, -medium_degrees),
                                                                                     translation=(-medium_translation, -medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[1], medium_scales[1]), degrees=(medium_degrees, medium_degrees),
                                                                                     translation=(medium_translation, medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[1], medium_scales[1]), degrees=(-medium_degrees, -medium_degrees),
                                                                                     translation=(medium_translation, medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[1], medium_scales[1]), degrees=(medium_degrees, medium_degrees),
                                                                                     translation=(-medium_translation, -medium_translation), isotropic=medium_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(medium_scales[1], medium_scales[1]), degrees=(-medium_degrees, -medium_degrees),
                                                                                     translation=(-medium_translation, -medium_translation), isotropic=medium_isotropic, p=1)
                                                                    ])])
transforms["affine"]["strong"]["identical"] = tio.Compose([tio.OneOf([tio.RandomAffine(scales=(strong_scales[0], strong_scales[0]), degrees=(strong_degrees, strong_degrees),
                                                                                     translation=(strong_translation, strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[0], strong_scales[0]), degrees=(-strong_degrees, -strong_degrees),
                                                                                     translation=(strong_translation, strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[0], strong_scales[0]), degrees=(strong_degrees, strong_degrees),
                                                                                     translation=(-strong_translation, -strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[0], strong_scales[0]), degrees=(-strong_degrees, -strong_degrees),
                                                                                     translation=(-strong_translation, -strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[1], strong_scales[1]), degrees=(strong_degrees, strong_degrees),
                                                                                     translation=(strong_translation, strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[1], strong_scales[1]), degrees=(-strong_degrees, -strong_degrees),
                                                                                     translation=(strong_translation, strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[1], strong_scales[1]), degrees=(strong_degrees, strong_degrees),
                                                                                     translation=(-strong_translation, -strong_translation), isotropic=strong_isotropic, p=1),
                                                                    tio.RandomAffine(scales=(strong_scales[1], strong_scales[1]), degrees=(-strong_degrees, -strong_degrees),
                                                                                     translation=(-strong_translation, -strong_translation), isotropic=strong_isotropic, p=1)
                                                                    ])])

weak_intensity = (-3000, 2000)
transforms["intensity"]["weak"]["random"] = tio.Compose([tio.RescaleIntensity(out_min_max=weak_intensity)])
medium_intensity = (-4000, 3000)
transforms["intensity"]["medium"]["random"] = tio.Compose([tio.RescaleIntensity(out_min_max=medium_intensity)])
strong_intensity = (-5000, 5000)
transforms["intensity"]["strong"]["random"] = tio.Compose([tio.RescaleIntensity(out_min_max=strong_intensity)])

transforms["intensity"]["weak"]["identical"] = tio.Compose([tio.RescaleIntensity(out_min_max=weak_intensity)])
transforms["intensity"]["medium"]["identical"] = tio.Compose([tio.RescaleIntensity(out_min_max=medium_intensity)])
transforms["intensity"]["strong"]["identical"] = tio.Compose([tio.RescaleIntensity(out_min_max=strong_intensity)])

weak_num_ghosts = (1, 1)
weak_ghost_intensity = (0.0, 0.2)
weak_num_spikes = (1, 1)
weak_spike_intensity = (0.0, 0.2)
weak_blur = (0.0, 0.3)
weak_noise = (0, 15)
transforms["artifacts"]["weak"]["random"] = tio.Compose([tio.RandomGhosting(num_ghosts=weak_num_ghosts, axes=(0,1,2), intensity=weak_ghost_intensity, p=1),
                                                            tio.RandomSpike(num_spikes=weak_num_spikes, intensity=weak_spike_intensity, p=1),
                                                            tio.RandomBlur(std=weak_blur, p=1),
                                                            tio.RandomNoise(mean=0, std=weak_noise, p=1)])

medium_num_ghosts = (1, 1)
medium_ghost_intensity = (0.0, 0.4)
medium_num_spikes = (1, 1)
medium_spike_intensity = (0.0, 0.5)
medium_blur = (0.0, 0.3)
medium_noise = (0, 30)
transforms["artifacts"]["medium"]["random"] = tio.Compose([tio.RandomGhosting(num_ghosts=medium_num_ghosts, axes=(0,1,2), intensity=medium_ghost_intensity, p=1),
                                                            tio.RandomSpike(num_spikes=medium_num_spikes, intensity=medium_spike_intensity, p=1),
                                                            tio.RandomBlur(std=medium_blur, p=1),
                                                            tio.RandomNoise(mean=0, std=medium_noise, p=1)])

strong_num_ghosts = (1, 1)
strong_ghost_intensity = (0.0, 0.7)
strong_num_spikes = (1, 1)
strong_spike_intensity = (0, 0.7)
strong_blur = (0, 0.3)
strong_noise = (0, 30)
transforms["artifacts"]["strong"]["random"] = tio.Compose([tio.RandomGhosting(num_ghosts=strong_num_ghosts, axes=(0,1,2), intensity=strong_ghost_intensity, p=1),
                                                            tio.RandomSpike(num_spikes=strong_num_spikes, intensity=strong_spike_intensity, p=1),
                                                            tio.RandomBlur(std=strong_blur, p=1),
                                                            tio.RandomNoise(mean=0, std=strong_noise, p=1)])


transforms["artifacts"]["weak"]["identical"] = tio.Compose([tio.RandomGhosting(num_ghosts=(weak_num_ghosts[1], weak_num_ghosts[1]), axes=(0,1,2),
                                                                               intensity=(weak_ghost_intensity[1], weak_ghost_intensity[1]), p=1),
                                                            tio.RandomSpike(num_spikes=(weak_num_spikes[1], weak_num_spikes[1]), intensity=(weak_spike_intensity[1], weak_spike_intensity[1]), p=1),
                                                            tio.RandomBlur(std=(weak_blur[1], weak_blur[1]), p=1),
                                                            tio.RandomNoise(mean=0, std=(weak_noise[1], weak_noise[1]), p=1)])

transforms["artifacts"]["medium"]["identical"] = tio.Compose([tio.RandomGhosting(num_ghosts=(medium_num_ghosts[1], medium_num_ghosts[1]), axes=(0,1,2),
                                                                               intensity=(medium_ghost_intensity[1], medium_ghost_intensity[1]), p=1),
                                                            tio.RandomSpike(num_spikes=(medium_num_spikes[1], medium_num_spikes[1]), intensity=(medium_spike_intensity[1], medium_spike_intensity[1]), p=1),
                                                            tio.RandomBlur(std=(medium_blur[1], medium_blur[1]), p=1),
                                                            tio.RandomNoise(mean=0, std=(medium_noise[1], medium_noise[1]), p=1)])

transforms["artifacts"]["strong"]["identical"] = tio.Compose([tio.RandomGhosting(num_ghosts=(strong_num_ghosts[1], strong_num_ghosts[1]), axes=(0,1,2),
                                                                               intensity=(strong_ghost_intensity[1], strong_ghost_intensity[1]), p=1),
                                                            tio.RandomSpike(num_spikes=(strong_num_spikes[1], strong_num_spikes[1]), intensity=(strong_spike_intensity[1], strong_spike_intensity[1]), p=1),
                                                            tio.RandomBlur(std=(strong_blur[1], strong_blur[1]), p=1),
                                                            tio.RandomNoise(mean=0, std=(strong_noise[1], strong_noise[1]), p=1)])

