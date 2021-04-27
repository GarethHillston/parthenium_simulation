import xarray as xr
import display
import calculate
import render

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'
raw_data = xr.open_dataset(filePath)

date_range = raw_data.coords['date'].data

image_data = calculate.urban_classified(raw_data, date_range[15])
render.rgb_plot(image_data)

# display.bare_soil_index(raw_data, date_range[15])
