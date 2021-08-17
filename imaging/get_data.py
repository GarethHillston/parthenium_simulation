import numpy as np
from astropy.stats import sigma_clip


def normalise(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))


def by_band_and_date(raw_data, band, date):
    return raw_data.sel(band=band, date=date).reflectance.data.astype(np.float64)


def all_bands_by_date(raw_data, date):
    return raw_data.sel(date=date).reflectance.data.astype(np.float64)


def by_band_and_date_sigma_clip(raw_data, band, date):
    reflectance_data = raw_data.sel(band=band, date=date).reflectance.data.astype(np.float64)
    clipped_data = sigma_clip(reflectance_data, sigma_upper=3)
    return clipped_data


def by_band_and_date_manual_clip(raw_data, band, date):
    reflectance_data = raw_data.sel(band=band, date=date).reflectance.data.astype(np.float64)
    clipped_data = reflectance_data.clip(max=3500)
    return clipped_data


def cloud_water_mask(raw_data, date):
    scl_data = raw_data.sel(date=date).variables['SCL']
    condition = (scl_data == 4) | (scl_data == 5) | (scl_data == 7)
    return np.where(condition, 1, 0)


class GetData:
    pass
