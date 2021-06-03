import pickle
import xarray as xr
import numpy as np

from imaging import get_data, indices, functions, render, classify

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data
valid_dates = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 17, 19, 21, 26, 27, 29, 32, 36, 37, 38, 39, 40, 41, 42, 44]
invalid_dates = [0, 3, 7, 10, 11, 16, 18, 20, 22, 23, 24, 25, 28, 30, 31, 33, 34, 35, 43, 45]
dates = date_range[valid_dates]

# image_size = np.shape(get_data.by_band_and_date(raw_data, 'B02', date_range[0]))

model = pickle.load(open('./imaging/classifiers/allBandOneDateNoCloud.pkl', 'rb'))

test_set = get_data.all_bands_by_date(raw_data, dates[0])
classified_image = classify.run_classification(model, test_set)

cmap = {'white', 'grey', 'black', 'indianred', 'gold', 'yellowgreen', 'darkturquoise', 'violet'}
render.single_plot(classified_image, 'Classified Rawalpindi', cmap)
