import numpy as np
from astropy.stats import sigma_clip


def by_band_and_date(raw_data, band, date):
    reflectance_data = raw_data.sel(band=band, date=date).reflectance.data
    clipped_data = sigma_clip(reflectance_data, sigma_upper=3)
    clipped_data.raw_data[clipped_data.mask] = np.median(reflectance_data)
    return clipped_data


def by_band_and_date_manual_clip(raw_data, band, date):
    reflectance_data = raw_data.sel(band=band, date=date).reflectance.data
    clipped_data = reflectance_data.clip(max=3500)
    return clipped_data


class GetData:
    pass
