import pickle
import xarray as xr
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

import utilities as util
from imaging import get_data, indices, functions, render, classify

filePath = '/scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)
date_times = [util.get_dates(raw_data)[0]]

for i in range(len(date_times)):
    date = date_times[i]
    date_neat = date.split('T')[0]

    binary_prediction = np.load('./progressions/19_20_binaries/bin_predict_' + date_neat + '.npy')
    SCL = raw_data.sel(date=date).variables['SCL']

    """
                 0 - absence  - brown
                 1 - presence - green
        SCL
        1/2  -   2 - no good  - black
        3    -   3 - shadows  - dark grey
        6    -   4 - water    - blue
        8-10 -   5 - clouds   - grey
        11   -   6 - snow     - white
    """

    bad = np.where(SCL == 1, 2, 0)
    dark = np.where(SCL == 2, 2, 0)
    shadow = np.where(SCL == 3, 3, 0)
    veg = np.where(SCL == 4, 1, 0)
    soil = np.where(SCL == 5, 1, 0)
    water = np.where(SCL == 6, 4, 0)
    low = np.where(SCL == 7, 1, 0)
    med = np.where(SCL == 8, 5, 0)
    high = np.where(SCL == 9, 5, 0)
    cirrus = np.where(SCL == 10, 5, 0)
    ice = np.where(SCL == 11, 6, 0)

    mask = bad + dark + shadow + veg + soil + water + low + med + high + cirrus + ice

    image_data = np.where(mask == 1, binary_prediction, mask)

    colours = ['peachpuff', 'mediumseagreen', 'black', 'dimgrey', 'cornflowerblue', 'lightgrey', 'white']
    cmap = ListedColormap(colours)

    figure = plt.figure()
    axes = figure.add_subplot(111)
    im = axes.imshow(image_data, vmin=0, vmax=len(colours), cmap=cmap)
    figure.set_dpi(600)
    axes.axis('off')
    axes.title.set_text(date_neat)

    divider = make_axes_locatable(axes)
    cax = divider.append_axes("right", size="5%", pad=0.2)
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_ticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
    cbar.set_ticklabels(['No Parthenium', 'Parthenium', 'Dark/defective', 'Cloud shadow', 'Water', 'Cloud', 'Ice/snow'])

    plt.show()

    # render.single_plot(image_data, date_neat, cmap, 'coloured')
