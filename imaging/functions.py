import numpy as np
from imaging import get_data, indices, render, classify


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


def generate_rgb_image(raw_data, date):
    red_band = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
    green_band = get_data.by_band_and_date_manual_clip(raw_data, 'B03', date)
    blue_band = get_data.by_band_and_date_manual_clip(raw_data, 'B02', date)

    return {date: [red_band, green_band, blue_band]}


def rgb_series(raw_data, date_range, to_file):
    image_series = {}

    for date in date_range:
        image_series.update(generate_rgb_image(raw_data, date))

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
    clusters = 8

    training_set = []
    for date in dates:
        training_set.append(indices.ndvi(raw_data, date))
    training_set = np.array(training_set)
    classifier = classify.train_kmeans(training_set, 1, clusters)

    start_set = indices.ndvi(raw_data, start_date)
    start_set = start_set.reshape(np.prod(image_size), 1)
    start_results = classify.run_classification(classifier, start_set, image_size)
    image_data[start_date] = start_results

    end_set = indices.ndvi(raw_data, end_date)
    end_set = end_set.reshape(np.prod(image_size), 1)
    end_results = classify.run_classification(classifier, end_set, image_size)
    image_data[end_date] = end_results

    colours = ['plum', 'coral', 'lightgreen', 'paleturquoise', 'black', 'white', 'silver', 'firebrick', 'khaki', 'royalblue', 'forestgreen']
    colour_subset = colours[0:clusters]
    render.multi_plot(image_data, colour_subset)

    return [start_results, end_results]


def mask_set():
    return
    # scl_mask = get_data.cloud_water_mask(raw_data, dates[0])
    # band_data = get_data.all_bands_by_date(raw_data, dates[0])
    # masked_set = []
    #
    # for i in range(image_size[0]):
    #     for j in range(image_size[1]):
    #         band_data[i][j] = band_data[i][j] * scl_mask[i][j]
    #         if np.sum(band_data[i][j]) != 0:
    #             masked_set.append(band_data[i][j])
    #
    # masked_set = np.array(masked_set)
    # num_classes = 8
    # classifier = classify.train_kmeans(masked_set, 10, num_classes)
    #
    # pickle.dump(classifier, open("./imaging/classifiers/allBandOneDateNoCloud.pkl", "wb"))


class Display:
    pass
