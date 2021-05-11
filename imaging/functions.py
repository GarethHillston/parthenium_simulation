import numpy as np
import get_data
import indices
import render
import classify


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


def rgb_series(raw_data, date_range, to_file):
    image_series = {}

    for date in date_range:
        red_band = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
        green_band = get_data.by_band_and_date_manual_clip(raw_data, 'B03', date)
        blue_band = get_data.by_band_and_date_manual_clip(raw_data, 'B02', date)

        image_series.update({date: [red_band, green_band, blue_band]})

    if to_file:
        render.rgb_series_to_file(image_series)
    else:
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


def classification_progression(raw_data, dates, start_date, end_date, image_size):
    image_data = {}

    training_set = []
    for date in dates:
        training_set.append(get_data.all_bands_by_date(raw_data, date))
    training_set = np.array(training_set)
    classifier = classify.train_kmeans(training_set)

    start_set = get_data.all_bands_by_date(raw_data, start_date)
    start_set = start_set.reshape(np.prod(image_size), 10)
    start_results = classify.run_classification(classifier, start_set, image_size)
    image_data[start_date] = start_results

    end_set = get_data.all_bands_by_date(raw_data, end_date)
    end_set = end_set.reshape(np.prod(image_size), 10)
    end_results = classify.run_classification(classifier, end_set, image_size)
    image_data[end_date] = end_results

    return image_data

    # colours = {'slateblue', 'aquamarine', 'indianred'}
    # render.multi_plot(progress, colours)


class Display:
    pass
