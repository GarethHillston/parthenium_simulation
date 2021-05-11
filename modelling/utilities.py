import numpy as np


def normalise_array_to_one(array):
    return array/np.sum(array)


def normalise_matrix(matrix):
    dim = len(np.shape(matrix))
    if dim == 2:
        for i in range(np.shape(matrix)[0]):
            matrix[i] = normalise_array_to_one(matrix[i])
    else:
        raise ValueError('Transition matrix should have 2 dimensions, instead it has {dim}'.format(dim=dim))

class Utilities:
    pass