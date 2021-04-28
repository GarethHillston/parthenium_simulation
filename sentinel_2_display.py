import xarray as xr
import display
import render

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data

display.rgb_series(raw_data, date_range[:10])
