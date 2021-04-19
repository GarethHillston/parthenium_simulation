import xarray as xr
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'

data = xr.open_dataset(filePath)

red_raw = data.sel(band='B04', date='2019-07-05T05:46:41Z').reflectance.data
green_raw = data.sel(band='B03', date='2019-07-05T05:46:41Z').reflectance.data
blue_raw = data.sel(band='B02', date='2019-07-05T05:46:41Z').reflectance.data

# red_raw = red_raw.clip(max=3500)
# green_raw = green_raw.clip(max=3500)
# blue_raw = blue_raw.clip(max=3500)

red_raw = sigma_clip(red_raw)
green_raw = sigma_clip(green_raw)
blue_raw = sigma_clip(blue_raw)

red_raw_flattened = red_raw.flatten()
green_raw_flattened = green_raw.flatten()
blue_raw_flattened = blue_raw.flatten()

flat_array = [red_raw_flattened, green_raw_flattened, blue_raw_flattened]

figure = plt.figure()
colors = ['red', 'green', 'blue']
axes2 = figure.add_subplot(111)
axes2.hist(flat_array, bins=30, histtype='bar', color=colors)
plt.show()

