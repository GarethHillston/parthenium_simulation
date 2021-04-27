import numpy as np
from astropy.stats import sigma_clip


def normalise(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))


def by_band_and_date_sigma_clip(raw_data, band, date):
    reflectance_data = raw_data.sel(band=band, date=date).reflectance.data.astype(np.float64)
    clipped_data = sigma_clip(reflectance_data, sigma_upper=3)
    return clipped_data


def by_band_and_date(raw_data, band, date):
    return raw_data.sel(band=band, date=date).reflectance.data.astype(np.float64)


class GetData:
    pass
