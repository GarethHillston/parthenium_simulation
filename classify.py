from sklearn.cluster import KMeans
import numpy as np
import get_data


def kmeans(raw_data):
    date_range = raw_data.coords['date'].data
    valid_indices = [1, 2, 4, 5, 6, 8]
    training_dates = [date_range[i] for i in valid_indices]
    test_date = date_range[9]

    # training_set = []
    # for date in training_dates:
    #     training_set.append(indices.ndvi(raw_data, date))
    # training_set = np.array(training_set)

    training_set = get_data.all_bands_by_date(raw_data, training_dates[0])
    test_set = get_data.all_bands_by_date(raw_data, test_date)

    shape = np.shape(training_set)
    training_set = training_set.reshape(shape[0] * shape[1], 10)
    test_set = test_set.reshape(shape[0] * shape[1], 10)

    kmeans = KMeans(n_clusters=3).fit(training_set)
    results = kmeans.predict(test_set)

    results = results.reshape(2108, 2230)

    return results


class Classify:
    pass
