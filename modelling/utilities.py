import numpy as np


def normalise_matrix(matrix):
    dim = len(np.shape(matrix))
    if dim == 2:
        norm_matrix = []
        for i in range(np.shape(matrix)[0]):
            norm_matrix.append(matrix[i]/np.sum(matrix[i]))
        return norm_matrix
    else:
        raise ValueError('Transition matrix should have 2 dimensions, instead it has {dim}'.format(dim=dim))


class Utilities:
    pass
