import numpy as np
import get_data
import calculate
import render


def bare_soil_index(raw_data, date):
    soil_index = calculate.bare_soil_index(raw_data, date)

    low_swir = get_data.by_band_and_date(raw_data, 'B11', date)
    nir = get_data.by_band_and_date(raw_data, 'B08', date)

    norm_index = get_data.normalise(soil_index)
    norm_swir = get_data.normalise(low_swir)
    norm_nir = get_data.normalise(nir)

    print("index")
    print(np.median(norm_index))
    print("nir")
    print(np.median(norm_nir))
    print("swir")
    print(np.median(norm_swir))

    image_data = np.dstack((norm_index, norm_nir, norm_swir))

    render.rgb_plot(image_data)


class Display:
    pass
