import pickle
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist

from imaging import get_data, indices, functions, render, classify

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data
valid_dates = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 17, 19, 21, 26, 27, 29, 32, 36, 37, 38, 39, 40, 41, 42, 44]
invalid_dates = [0, 3, 7, 10, 11, 16, 18, 20, 22, 23, 24, 25, 28, 30, 31, 33, 34, 35, 43, 45]
dates = date_range[valid_dates]

image_size = np.shape(get_data.by_band_and_date(raw_data, 'B02', date_range[0]))

test_set = get_data.all_bands_by_date(raw_data, dates[0])
test_set = test_set.reshape(np.prod(image_size), 10)

distortions = []
inertias = []
mapping1 = {}
mapping2 = {}
K = range(1, 20)

for k in K:
    # Building and fitting the model
    kmeanModel = KMeans(n_clusters=k).fit(test_set)
    kmeanModel.fit(test_set)

    distortions.append(sum(np.min(cdist(test_set, kmeanModel.cluster_centers_,
                                        'euclidean'), axis=1)) / test_set.shape[0])
    inertias.append(kmeanModel.inertia_)

    mapping1[k] = sum(np.min(cdist(test_set, kmeanModel.cluster_centers_,
                                   'euclidean'), axis=1)) / test_set.shape[0]
    mapping2[k] = kmeanModel.inertia_

plt.plot(K, distortions, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Distortion')
plt.title('The Elbow Method using Distortion')
plt.savefig('./imaging/plots/knee_plots/distortion.png')
plt.close

plt.plot(K, inertias, 'bx-')
plt.xlabel('Values of K')
plt.ylabel('Inertia')
plt.title('The Elbow Method using Inertia')
plt.savefig('./imaging/plots/knee_plots/inertias.png')
