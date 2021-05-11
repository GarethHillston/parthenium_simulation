import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

from matplotlib.colors import ListedColormap

band_names = dict(B02='blue', B03='green', B04='red', B05='low IR', B06='mid NIR', B07='high NIR', B08='wide NIR',
                  B8A='higher NIR', B11='1610 SWIR', B12='2190 SWIR')

now = datetime.now().strftime("%d_%m_%y__%H%M%S")
output_folder = "./plots/{dateTime}".format(dateTime=now)


def histogram(bands_data):
    flat_arrays = []

    for band in bands_data.keys():
        flat_arrays.append(bands_data[band].flatten())

    figure = plt.figure()
    axes2 = figure.add_subplot(111)
    axes2.hist(flat_arrays, bins=50, histtype='bar')
    plt.show()


def multi_plot(image_data, colour_map):
    cmap = plt.get_cmap(colour_map) if colour_map == str else ListedColormap(colour_map)
    num_images = 0
    figure = plt.figure()

    for key in image_data.keys():
        num_images += 1

        axes = figure.add_subplot(1, len(image_data), num_images)
        axes.title.set_text(key)
        axes.axis('off')
        axes.imshow(image_data[key], cmap=cmap)

    figure.tight_layout()
    plt.show()


def rgb_series(image_series):
    num_images = 0
    figure = plt.figure()

    for date in image_series.keys():
        num_images += 1
        rgb_cube = image_series[date]

        norm_red = normalise(rgb_cube[0])
        norm_green = normalise(rgb_cube[1])
        norm_blue = normalise(rgb_cube[2])

        image = np.dstack((norm_red, norm_green, norm_blue))

        axes = figure.add_subplot(1, len(image_series), num_images)
        axes.title.set_text(date.split('T')[0])
        axes.axis('off')
        axes.imshow(image)

    figure.tight_layout()
    plt.show()


def single_plot(image_data, title, colour_map):
    cmap = plt.get_cmap(colour_map) if colour_map == str else ListedColormap(colour_map)

    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(image_data, cmap=cmap)
    axes.axis('off')
    axes.title.set_text(title)
    plt.show()


def rgb_plot(rgb_data):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(rgb_data)
    axes.axis('off')
    plt.show()


def rgb_series_to_file(image_series):
    iteration = 0
    os.mkdir(output_folder)

    for date in image_series.keys():
        iteration += 1
        rgb_cube = image_series[date]

        norm_red = normalise(rgb_cube[0])
        norm_green = normalise(rgb_cube[1])
        norm_blue = normalise(rgb_cube[2])

        image = np.dstack((norm_red, norm_green, norm_blue))

        figure = plt.figure()
        axes = figure.add_subplot(111)
        axes.imshow(image)
        axes.axis('off')
        plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=output_folder, iter=iteration))
        plt.close()


def normalise(array):
    divisor = (np.max(array) - np.min(array)) if np.max(array) != np.min(array) else 1.0
    return (array - np.min(array)) / divisor


class Render:
    pass
