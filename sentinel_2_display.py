import xarray as xr
import render

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)
date_range = raw_data.coords['date'].data[:16]

#render.ndvi(raw_data, date_range[15])
#render.rgb_series(raw_data, date_range)
#render.all_bands(raw_data, date_range[15])
render.histogram(raw_data, date_range[15])
