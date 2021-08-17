import xarray as xr
import numpy as np

import utilities as util

filePath = '/scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)
date_times = util.get_dates(raw_data)
dates = np.array([d.split('T')[0] for d in date_times])

lulc_proportions = np.load('lulc_parth_combined_model/parth_lulc_proportions_19_20.npy', allow_pickle=True)

print(lulc_proportions)