import numpy as np
from modelling import plot_data, spread_model, initialise_grid


def basic_markov_sim(grid_size, max_iterations, trans_matrix):
    locations = np.zeros(grid_size, dtype=int)

    initialise_grid.random_start(locations, len(trans_matrix))

    for i in range(max_iterations):
        print("{pc} %".format(pc=(100 * i/max_iterations)))
        plot_data.replot(locations, i)

        locations = spread_model.markov_basic(locations, trans_matrix)

    plot_data.replot(locations, max_iterations + 1)


class Simulate:
    pass
