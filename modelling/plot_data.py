import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as colours
from matplotlib.colors import ListedColormap


class PlotData:
    def __init__(self, out_dir):
        if (out_dir == ''):
            now = datetime.now().strftime("%d_%m_%y__%H%M%S")
            self.output_folder = "./modelling/simulations/{dateTime}".format(dateTime=now)
        else:
            self.output_folder = out_dir
        os.mkdir(self.output_folder)

    def replot_binary(self, locations, iteration):
        figure = plt.figure()
        axes = figure.add_subplot(111)
        cmap = colours.ListedColormap(['white', 'mediumseagreen'])
        axes.imshow(locations, cmap=cmap)
        figure.set_dpi(300)
        plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=self.output_folder, iter=iteration))
        plt.close()

    def replot(self, locations, iteration):
        figure = plt.figure()
        axes = figure.add_subplot(111)
        cMap = colours.ListedColormap(
            {'white', 'navajowhite', 'coral', 'indianred', 'firebrick', 'maroon', 'indigo', 'black'})
        axes.imshow(locations, cmap=cMap)
        figure.set_dpi(300)
        plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=self.output_folder, iter=iteration))
        plt.close()

    def replot_gradient(self, locations, iteration):
        figure = plt.figure()
        axes = figure.add_subplot(111)
        image = axes.pcolormesh(locations, cmap=plt.get_cmap('inferno'), shading='gouraud', vmin=0, vmax=1)
        figure.colorbar(image, ax=axes)
        plt.savefig('{outputFolder}/sim-{iter:03d}.png'.format(outputFolder=self.output_folder, iter=iteration))
        plt.close()
