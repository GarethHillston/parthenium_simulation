from sklearn.cluster import KMeans
import numpy as np
import get_data


def train_kmeans(training_set):
    shape = np.shape(training_set)
    training_set = training_set.reshape(np.prod(shape[:-1]), 10)
    classifier = KMeans(n_clusters=3).fit(training_set)
    return classifier


def run_classification(classifier, test_set, shape):
    return classifier.predict(test_set).reshape(shape[0], shape[1])


def kmeans_single(raw_data, date):
    training_set = get_data.all_bands_by_date(raw_data, date)

    kmeans = train_kmeans(training_set)

    test_set = get_data.all_bands_by_date(raw_data, date)
    test_shape = np.shape(test_set)
    test_set = test_set.reshape(np.prod(test_shape[:-1]), 10)

    return run_classification(kmeans, test_set, test_shape)


def kmeans(raw_data, dates):
    training_dates = dates[:-1]

    training_set = []
    for date in training_dates:
        training_set.append(get_data.all_bands_by_date(raw_data, date))
    training_set = np.array(training_set)

    kmeans = train_kmeans(training_set)

    test_date = dates[-1:]
    test_set = get_data.all_bands_by_date(raw_data, test_date)
    test_shape = np.shape(test_set)
    test_set = test_set.reshape(np.prod(test_shape[:-2]), 10)

    return run_classification(kmeans, test_set, test_shape)


class Classify:
    pass
