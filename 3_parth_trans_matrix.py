import numpy as np
import xarray as xr
import utilities as util

from modelling import transition_matrix as matrix

# create normal matrix
progressions = np.load('lulc_parth_combined_model/19_20_binaries/first_10_predictions.npy', allow_pickle=True)
trans_matrix = matrix.create(progressions)
np.save('lulc_parth_combined_model/transition_matrix.npy', trans_matrix)

# modify for lulc weights
