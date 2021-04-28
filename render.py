import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import get_data

band_names = dict(B02='blue', B03='green', B04='red', B05='low IR', B06='mid NIR', B07='high NIR', B08='wide NIR',
                  B8A='higher NIR', B11='1610 SWIR', B12='2190 SWIR')


def histogram(bands_data):
    flat_arrays = []

    for band in bands_data.keys():
        flat_arrays.append(bands_data[band].flatten())

    figure = plt.figure()
    axes2 = figure.add_subplot(111)
    axes2.hist(flat_arrays, bins=50, histtype='bar')
    plt.show()


def multi_plot(raw_data, date):
    num_images = 0
    bands = raw_data.coords['band'].data
    figure = plt.figure()

    for band in bands:
        num_images += 1
        reflectance_data = get_data.by_band_and_date(raw_data, band, date)

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
        red_band = get_data.by_band_and_date(raw_data, 'B04', date)
        green_band = get_data.by_band_and_date(raw_data, 'B03', date)
        blue_band = get_data.by_band_and_date(raw_data, 'B02', date)

        red_band = red_band.clip(max=3500)
        green_band = green_band.clip(max=3500)
        blue_band = blue_band.clip(max=3500)

        #clipped_data = reflectance_data.clip(max=3500)

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


def single_plot(image_data, colour_map):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(image_data, cmap=plt.get_cmap(colour_map))
    axes.axis('off')
    plt.show()


def rgb_plot(rgb_data):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(rgb_data)
    axes.axis('off')
    plt.show()


def normalise(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))


class Render:
    pass
