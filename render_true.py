import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import get_data

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)


def render_rgb_series():
    num_images = 0
    figure = plt.figure()

    for date in dates:
        num_images += 1
        red_band = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
        green_band = get_data.by_band_and_date_manual_clip(raw_data, 'B03', date)
        blue_band = get_data.by_band_and_date_manual_clip(raw_data, 'B02', date)

        rgb_data = np.dstack((red_band, green_band, blue_band))

        axes = figure.add_subplot(1, len(dates), num_images)
        axes.title.set_text(date.split('T')[0])
        axes.axis('off')
        axes.imshow(rgb_data)

    figure.tight_layout()
    plt.show()


def render_ndvi():


    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(ndvi_data)
    plt.show()


dates = raw_data.coords['date'].data[:10]

render_ndvi()
