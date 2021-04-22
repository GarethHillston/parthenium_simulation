import matplotlib.pyplot as plt
import numpy as np
import get_data

band_names = dict(B02='blue', B03='green', B04='red', B05='low IR', B06='mid NIR', B07='high NIR', B08='wide NIR',
                  B8A='higher NIR', B11='1610 SWIR', B12='2190 SWIR')


def all_bands(raw_data, date):
    num_images = 0
    bands = raw_data.coords['band'].data
    figure = plt.figure()

    for band in bands:
        num_images += 1
        reflectance_data = get_data.by_band_and_date_manual_clip(raw_data, band, date)

        print(reflectance_data)

        normalised_reflectance = normalise(reflectance_data)

        axes = figure.add_subplot(1, len(bands), num_images)
        axes.title.set_text(band_names[band])
        axes.axis('off')
        axes.imshow(normalised_reflectance)

    figure.tight_layout()
    plt.show()


def rgb_series(raw_data, dates):
    num_images = 0
    figure = plt.figure()

    for date in dates:
        num_images += 1
        red_band = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
        green_band = get_data.by_band_and_date_manual_clip(raw_data, 'B03', date)
        blue_band = get_data.by_band_and_date_manual_clip(raw_data, 'B02', date)

        norm_red = normalise(red_band)
        norm_green = normalise(green_band)
        norm_blue = normalise(blue_band)

        rgb_data = np.dstack((norm_red, norm_green, norm_blue))

        axes = figure.add_subplot(1, len(dates), num_images)
        axes.title.set_text(date.split('T')[0])
        axes.axis('off')
        axes.imshow(rgb_data)

    figure.tight_layout()
    plt.show()


def get_ndvi_scores(raw_data, date):
    red = get_data.by_band_and_date_manual_clip(raw_data, 'B04', date)
    nir = get_data.by_band_and_date_manual_clip(raw_data, 'B08', date)

    return (nir - red) / (nir + red)


def ndvi(raw_data, date):
    ndvi_data = get_ndvi_scores(raw_data, date)
    norm_data = normalise(ndvi_data)

    print("ndvi")
    print(ndvi_data.min())
    print(ndvi_data.max())
    print(ndvi_data.mean())
    print(np.median(ndvi_data))
    print(ndvi_data)

    colours = {}

    # 000000
    # a50026
    # d73027
    # f46d43
    # fdae61
    # fee08b
    # ffffbf
    # d9ef8b
    # a6d96a
    # 66bd63
    # 1a9850
    # 006837

    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.imshow(norm_data, cmap=plt.get_cmap('viridis'))
    plt.show()


def normalise(array):
    return array / array.max()


class Render:
    pass
