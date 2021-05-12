import numpy as np
from modelling import plot_data, spread_model, initialise_grid


def basic_markov_sim(grid_size, max_iterations):
    locations = np.zeros((grid_size, grid_size), dtype=int)

    initialise_grid.random_start(locations, grid_size, 5)

    for i in range(max_iterations):
        plot_data.replot(locations, i)

        locations = spread_model.markov_basic(locations, grid_size)

    plot_data.replot(locations, max_iterations + 1)


class Simulate:
    pass
