from sklearn.cluster import KMeans
import xarray as xr
import numpy as np
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import calculate
import render
import get_data
import model

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data

# training_set = []

# for date in training_dates:
#     training_set.append(get_data.all_bands_by_date(raw_data, date))
#
# training_set = np.array(training_set)
#
# test_set = get_data.all_bands_by_date(raw_data, test_date)

valid_indices = [1, 2, 4, 5, 6, 8]
training_dates = [date_range[i] for i in valid_indices]
test_date = date_range[9]

training_set = calculate.ndvi(raw_data, training_dates[0])
test_set = calculate.ndvi(raw_data, test_date)

training_set = training_set.flatten().reshape(-1, 1)
test_set = test_set.flatten().reshape(-1, 1)

kmeans = KMeans(n_clusters=2).fit(training_set)
results = kmeans.predict(test_set)

results = results.reshape(2108, 2230)
test_set = test_set.reshape(2108, 2230)

figure = plt.figure()

axes = figure.add_subplot(131)
axes.imshow(test_set, cmap=plt.get_cmap('inferno'))
axes.axis('off')
axes.title.set_text('NDVI')

cmap = ListedColormap(['slateblue', 'aquamarine'])
axes2 = figure.add_subplot(132)
image = axes2.imshow(results, cmap=cmap)
axes2.axis('off')
axes2.title.set_text('Classification')

red_band = get_data.by_band_and_date(raw_data, 'B04', test_date)
green_band = get_data.by_band_and_date(raw_data, 'B03', test_date)
blue_band = get_data.by_band_and_date(raw_data, 'B02', test_date)

red_band = red_band.clip(max=3500)
green_band = green_band.clip(max=3500)
blue_band = blue_band.clip(max=3500)

norm_red = get_data.normalise(red_band)
norm_green = get_data.normalise(green_band)
norm_blue = get_data.normalise(blue_band)

rgb_data = np.dstack((norm_red, norm_green, norm_blue))

axes3 = figure.add_subplot(133)
axes3.imshow(rgb_data)
axes3.axis('off')
axes3.title.set_text('True Colour')

plt.show()
