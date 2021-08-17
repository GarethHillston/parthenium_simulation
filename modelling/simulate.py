import numpy as np
from modelling import spread_model, initialise_grid
from modelling.plot_data import PlotData


def markov_lulc(locations, trans_matrix, land_classes, lulc_proportions, max_iterations, out_dir):
    plotter = PlotData(out_dir)

    for i in range(max_iterations):
        print("{pc} %".format(pc=(100 * i/max_iterations)))
        plotter.replot_binary(locations, i)

        locations = spread_model.circle_spread_lulc(locations, trans_matrix, land_classes, lulc_proportions)

    plotter.replot_binary(locations, max_iterations + 1)


def markov(locations, max_iterations, trans_matrix, out_dir):
    plotter = PlotData(out_dir)

    for i in range(max_iterations):
        print("{pc} %".format(pc=(100 * i/max_iterations)))
        plotter.replot_binary(locations, i)

        locations = spread_model.circle_spread(locations, trans_matrix)

    plotter.replot_binary(locations, max_iterations + 1)


def markov_test(grid_size, max_iterations, trans_matrix):
    locations = np.zeros(grid_size, dtype=int)
    locations = initialise_grid.centre_start(locations, 5)

    markov(locations, max_iterations, trans_matrix)


class Simulate:
    pass
