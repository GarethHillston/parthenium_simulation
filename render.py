import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'

data = xr.open_dataset(filePath)

subset = data.sel(band='B08', date='2019-07-05T05:46:41Z').reflectance

cmap = plt.get_cmap('inferno')
levels = MaxNLocator(nbins=15).tick_values(subset.data.min(), subset.data.max())
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

figure = plt.figure()
axes = figure.add_subplot(111)
image = axes.pcolormesh(subset.data, cmap=cmap, norm=norm)
figure.colorbar(image, ax=axes)
plt.show()

