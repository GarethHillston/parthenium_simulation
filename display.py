import numpy as np
import get_data
import indices
import render


def histogram(raw_data, date, bands):
    data = {}

    for band in bands:
        data.update({band: raw_data.sel(band=band, date=date).reflectance.data})

    render.histogram(data)


def multi_plot(raw_data, date, bands):
    data = {}

    for band in bands:
        data.update({band: raw_data.sel(band=band, date=date).reflectance.data})

    render.multi_plot(data, date)


def rgb_series(raw_data, date_range):
    image_series = {}

    for date in date_range:
        red_band = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
        green_band = get_data.by_band_and_date_manual_clip(raw_data, 'B03', date)
        blue_band = get_data.by_band_and_date_manual_clip(raw_data, 'B02', date)

        image_series.update({date: [red_band, green_band, blue_band]})

    render.rgb_series(image_series)


def bare_soil_index(raw_data, date):
    soil_index = indices.bare_soil_index(raw_data, date)

    nir = get_data.by_band_and_date(raw_data, 'B08', date)
    low_swir = get_data.by_band_and_date(raw_data, 'B11', date)

    norm_index = get_data.normalise(soil_index)
    norm_nir = get_data.normalise(nir)
    norm_swir = get_data.normalise(low_swir)

    image_data = np.dstack((norm_index, norm_nir, norm_swir))

    render.rgb_plot(image_data)


class Display:
    pass
