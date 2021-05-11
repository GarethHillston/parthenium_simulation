import xarray as xr
import numpy as np
from imaging import get_data
from modelling import utilities as util

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data
valid_dates = [1, 2, 4, 5, 6, 8, 9, 12, 13, 14, 15, 17, 19, 21, 26, 27, 29, 32, 36, 37, 38, 39, 40, 41, 42, 44]
invalid_dates = [0, 3, 7, 10, 11, 16, 18, 20, 22, 23, 24, 25, 28, 30, 31, 33, 34, 35, 43, 45]

image_size = np.shape(get_data.by_band_and_date(raw_data, 'B02', date_range[0]))

# display.rgb_series(raw_data, date_range[[valid_dates[0], valid_dates[-1]]], False)

progress = np.load('./progressions/progress1.npy', allow_pickle=True)

transition_matrix = np.zeros((3, 3), dtype=int)
start_date = date_range[valid_dates[0]]
end_date = date_range[valid_dates[-1]]
start_classes = progress.item().get(start_date).flatten()
end_classes = progress.item().get(end_date).flatten()

for i in range(len(start_classes)):
    transition_matrix[start_classes[i]][end_classes[i]] += 1

total_transitions = np.sum(transition_matrix)

transition_matrix = transition_matrix / total_transitions

normalised_matrix = util.normalise_matrix(transition_matrix)

print(np.array_str(transition_matrix, precision=4, suppress_small=True))
