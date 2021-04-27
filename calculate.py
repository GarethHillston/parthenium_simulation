import numpy as np
import get_data


def __index(add_band, sub_band):
    return (add_band.astype(float) - sub_band.astype(float)) / (add_band + sub_band)


# https://custom-scripts.sentinel-hub.com/sentinel-2/ndvi/
def ndvi(raw_data, date):
    red = get_data.by_band_and_date(raw_data, 'B04', date)
    nir = get_data.by_band_and_date(raw_data, 'B08', date)

    return __index(nir, red)


# https://custom-scripts.sentinel-hub.com/sentinel-2/gndvi/
def gndvi(raw_data, date):
    green = get_data.by_band_and_date(raw_data, 'B03', date)
    nir = get_data.by_band_and_date(raw_data, 'B08', date)

    return __index(nir, green)


# https://custom-scripts.sentinel-hub.com/sentinel-2/ndmi/
def ndmi(raw_data, date):
    swir = get_data.by_band_and_date(raw_data, 'B11', date)
    nir = get_data.by_band_and_date(raw_data, 'B08', date)

    return __index(nir, swir)


def bare_soil_index(raw_data, date):
    low_swir = get_data.by_band_and_date(raw_data, 'B11', date)
    red = get_data.by_band_and_date(raw_data, 'B04', date)
    nir = get_data.by_band_and_date(raw_data, 'B08', date)
    blue = get_data.by_band_and_date(raw_data, 'B02', date)

    return ((low_swir + red) - (nir + blue)) / ((low_swir + red) + (nir + blue))


def urban_classified(raw_data, date):
    ndvi_scores = ndvi(raw_data, date)
    ndmi_scores = ndmi(raw_data, date)
    # ((B11 + B04) - (B08 + B02)) / ((B11 + B04) + (B08 + B02));


class Calculate:
    pass
