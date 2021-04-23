import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import get_data

band_names = dict(B02='blue', B03='green', B04='red', B05='low IR', B06='mid NIR', B07='high NIR', B08='wide NIR',
                  B8A='higher NIR', B11='1610 SWIR', B12='2190 SWIR')


def histogram(raw_data, date):
    red_raw = raw_data.sel(band='B04', date=date).reflectance.data
    green_raw = raw_data.sel(band='B03', date=date).reflectance.data
    blue_raw = raw_data.sel(band='B02', date=date).reflectance.data

    red_clipped = red_raw.clip(max=3500)
    green_clipped = green_raw.clip(max=3500)
    blue_clipped = blue_raw.clip(max=3500)

    red_flattened = red_clipped.flatten()
    green_flattened = green_clipped.flatten()
    blue_flattened = blue_clipped.flatten()

    flat_array = [red_flattened, green_flattened, blue_flattened]

    figure = plt.figure()
    colors = ['red', 'green', 'blue']
    axes2 = figure.add_subplot(111)
    axes2.hist(flat_array, bins=30, histtype='bar', color=colors)
    plt.show()


def all_bands(raw_data, date):
    num_images = 0
    bands = raw_data.coords['band'].data
    figure = plt.figure()

    for band in bands:
        num_images += 1
        reflectance_data = get_data.by_band_and_date_manual_clip(raw_data, band, date)

        print(reflectance_data)

        normalised_reflectance = normalise(reflectance_data)

        axes = figure.add_subplot(1, len(bands), num_images)
        axes.title.set_text(band_names[band])
        axes.axis('off')
        axes.imshow(normalised_reflectance)

    figure.tight_layout()
    plt.show()


def rgb_series(raw_data, dates):
    num_images = 0
    figure = plt.figure()

    for date in dates:
        num_images += 1
        red_band = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
        green_band = get_data.by_band_and_date_manual_clip(raw_data, 'B03', date)
        blue_band = get_data.by_band_and_date_manual_clip(raw_data, 'B02', date)

        norm_red = normalise(red_band)
        norm_green = normalise(green_band)
        norm_blue = normalise(blue_band)

        rgb_data = np.dstack((norm_red, norm_green, norm_blue))

        axes = figure.add_subplot(1, len(dates), num_images)
        axes.title.set_text(date.split('T')[0])
        axes.axis('off')
        axes.imshow(rgb_data)

    figure.tight_layout()
    plt.show()


def get_ndvi_scores(raw_data, date):
    red = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
    nir = get_data.by_band_and_date_manual_clip(raw_data, 'B08', date)

    return (nir.astype(float) - red.astype(float)) / (nir + red)


def ndvi(raw_data, date):
    ndvi_data = get_ndvi_scores(raw_data, date)
    norm_data = normalise(ndvi_data)

    colours = {"#000000", "#a50026", "#d73027", "#f46d43", "#fdae61", "#fee08b", "#ffffbf", "#d9ef8b", "#a6d96a",
               "#66bd63", "#1a9850", "#006837"}

    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(norm_data, cmap=cmap)
    axes.axis('off')
    plt.show()


def normalise(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))


class Render:
    pass
