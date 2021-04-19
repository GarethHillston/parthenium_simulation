import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from astropy.stats import sigma_clip

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'

data = xr.open_dataset(filePath)


def get_normalised_band_data(band, date):
    raw_data = data.sel(band=band, date=date).reflectance.data
    clipped_data = sigma_clip(raw_data, sigma_upper=3)
    clipped_data.data[clipped_data.mask] = np.median(raw_data)
    # clipped_data = raw_data.clip(max=3500)
    normalised_data = clipped_data / clipped_data.max()
    return normalised_data


def get_normalised_band_data_manual_clip(band, date):
    raw_data = data.sel(band=band, date=date).reflectance.data
    clipped_data = raw_data.clip(max=3500)
    normalised_data = clipped_data / clipped_data.max()
    return normalised_data


dates = data.coords['date'].data[:10]
num_images = 0

for date in dates:
    num_images += 1
    red_band = get_normalised_band_data_manual_clip('B04', date)
    green_band = get_normalised_band_data_manual_clip('B03', date)
    blue_band = get_normalised_band_data_manual_clip('B02', date)

    rgb_data = np.dstack((red_band, green_band, blue_band))

    figure = plt.figure()
    # axes = figure.add_subplot(1, len(dates), num_images)
    axes = figure.add_subplot(111)
    axes.imshow(rgb_data)
    plt.savefig('plots/rawalpindi-{iter:03d}.png'.format(iter=num_images))
    plt.close()
