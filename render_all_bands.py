import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
from astropy.stats import sigma_clip

filePath = '../../../../scratch/nas_bridle/sentinel/shared/rawalpindi_1.nc'

data = xr.open_dataset(filePath)


def get_normalised_band_data_manual_clip(band, date):
    raw_data = data.sel(band=band, date=date).reflectance.data
    clipped_data = raw_data.clip(max=3500)
    normalised_data = clipped_data / clipped_data.max()
    return normalised_data


band_names = dict(B02='blue', B03='green', B04='red', B05='low IR', B06='mid IR', B07='high IR', B08='wide IR',
                  B8A='higher IR', B11='1610 SWIR', B12='2190 SWIR')

date = data.coords['date'].data[9]
bands = data.coords['band'].data
num_columns = 5
num_images = 0
figure = plt.figure()

for band in bands:
    num_images += 1
    image_data = get_normalised_band_data_manual_clip(band, date)
    x_position = num_images if num_images < 6 else num_images - 5
    y_position = 1 if num_images > 5 else 2
    axes = figure.add_subplot(y_position, num_columns, x_position)
    axes.title.set_text(band_names[band])
    axes.axis('off')
    axes.imshow(image_data)

#figure.tight_layout()
plt.show()

#axes = figure.add_subplot(111)
#plt.savefig('plots/rawalpindi-{iter:03d}.png'.format(iter=num_images), bbox_inches='tight')
