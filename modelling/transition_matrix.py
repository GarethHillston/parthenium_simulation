import numpy as np


def create(progress):
    num_values = int(np.max(progress) + 1)
    transition_matrix = np.zeros((num_values, num_values), dtype=float)

    for date in range(len(progress)-1):
        current_date = progress[date].flatten()
        next_date = progress[date+1].flatten()
        for i in range(len(current_date)):
            if current_date[i] != np.nan and next_date[i] != np.nan:
                transition_matrix[current_date[i]][next_date[i]] += 1

    return normalise(transition_matrix)


def create_basic(progress):
    num_clusters = int(np.max(progress) + 1)
    transition_matrix = np.zeros((num_clusters, num_clusters), dtype=float)
    start_classes = progress[0].flatten()
    end_classes = progress[-1].flatten()

    for i in range(len(start_classes)):
        if start_classes[i] != np.nan and end_classes[i] != np.nan:
            transition_matrix[start_classes[i]][end_classes[i]] += 1

    return normalise(transition_matrix)


def normalise(matrix):
    dim = len(np.shape(matrix))
    if dim == 2:
        norm_matrix = []
        for i in range(np.shape(matrix)[0]):
            norm_matrix.append(matrix[i]/np.sum(matrix[i]))
        return norm_matrix
    else:
        raise ValueError('Transition matrix should have 2 dimensions, instead it has {dim}'.format(dim=dim))


class TransitionMatrix:
    pass
