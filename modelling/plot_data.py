import os
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.colors as colours

now = datetime.now().strftime("%d_%m_%y__%H%M%S")
output_folder = "./simulations/{dateTime}".format(dateTime=now)
os.mkdir(output_folder)


def replot(locations, iteration):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    cMap = colours.ListedColormap(['w', 'r'])
    image = axes.pcolormesh(locations, cmap=cMap, shading='flat', vmin=0, vmax=1)
    plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=output_folder, iter=iteration))
    plt.close()


def replot_gradient(locations, iteration):
    figure = plt.figure()
    axes = figure.add_subplot(111)
    image = axes.pcolormesh(locations, cmap=plt.get_cmap('Inferno'), shading='gouraud', vmin=0, vmax=1)
    figure.colorbar(image, ax=axes)
    plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=output_folder, iter=iteration))
    plt.close()


class PlotData:
    pass
