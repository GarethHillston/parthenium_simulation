import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
from datetime import datetime

from matplotlib.colors import ListedColormap
from mpl_toolkits.axes_grid1 import make_axes_locatable

band_names = dict(B02='blue', B03='green', B04='red', B05='low IR', B06='mid NIR', B07='high NIR', B08='wide NIR',
                  B8A='higher NIR', B11='1610 SWIR', B12='2190 SWIR')

eight_colours = ['black', 'white', 'grey', 'blue', 'orange', 'green', 'purple', 'brown']
binary_colours = ['white', 'mediumseagreen']

now = datetime.now().strftime("%d_%m_%y__%H%M%S")
output_folder = "{dateTime}".format(dateTime=now)


def histogram(bands_data):
    flat_arrays = []

    for band in bands_data.keys():
        flat_arrays.append(bands_data[band].flatten())

    figure = plt.figure()
    axes2 = figure.add_subplot(111)
    axes2.hist(flat_arrays, bins=50, histtype='bar')
    plt.show()


def multi_plot(image_data, colour_map):
    cmap = plt.get_cmap(colour_map) if colour_map == str else plt.get_cmap('inferno')
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


def single_plot(image_data, title, colour_map, to_file):
    cmap = plt.get_cmap('inferno') if colour_map == str else ListedColormap(colour_map)

    figure = plt.figure()
    axes = figure.add_subplot(111)
    im = axes.imshow(image_data)
    figure.set_dpi(600)
    axes.axis('off')

    values = np.unique(image_data)
    bounds = range(len(values)+1)
    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="5%", pad=0.2)
    cbar = plt.colorbar(im, cax=cax, cmap=cmap, spacing='proportional', boundaries=bounds)
    cbar.set_ticks(values+0.5)
    cbar.set_ticklabels(values)
    cbar.ax.tick_params(labelsize=8)

    if title != '':
        axes.title.set_text(title)

    if to_file != '':
        time = datetime.now().strftime("%H%M%S")
        plt.savefig('{outputFolder}/plot_{time}.png'.format(outputFolder=to_file, time=time))
        plt.close()
    else:
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
