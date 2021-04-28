import xarray as xr
import display
import calculate
import render

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data

display.histogram(raw_data, date_range[1], ['B02', 'B03', 'B04'])
