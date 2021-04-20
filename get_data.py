import numpy as np
from astropy.stats import sigma_clip


def by_band_and_date(raw_data, band, date):
    raw_data = raw_data.sel(band=band, date=date).reflectance.raw_data
    clipped_data = sigma_clip(raw_data, sigma_upper=3)
    clipped_data.raw_data[clipped_data.mask] = np.median(raw_data)
    normalised_data = clipped_data / clipped_data.max()
    return normalised_data


def by_band_and_date_manual_clip(raw_data, band, date):
    raw_data = raw_data.sel(band=band, date=date).reflectance.raw_data
    clipped_data = raw_data.clip(max=3500)
    normalised_data = clipped_data / clipped_data.max()
    return normalised_data


class GetData:
    pass
