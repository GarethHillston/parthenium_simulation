import numpy as np


def markov_basic(locations, grid_size):
    new_locs = locations.copy()

    # [DD, DA]  Dead or Alive
    # [AD, AA]
    transition_matrix = [[0.8, 0.2],
                         [0.01, 0.99]]

    # for each cell, transition randomly as per matrix
    for x in range(0, grid_size - 1):
        for y in range(0, grid_size - 1):
            if locations[x, y] == 1:
                x_start, x_stop = max(x - 1, 0), min(x + 1, grid_size)
                y_start, y_stop = max(y - 1, 0), min(y + 1, grid_size)

                for i in range(x_start, x_stop+1):
                    for j in range(y_start, y_stop+1):
                        new_locs[i, j] = 1 if np.random.rand() > transition_matrix[locations[i][j]][0] else 0

    return new_locs


def spread_basic_threshold(locations, grid_size, infectious_threshold, virality):
    new_locs = locations.copy()
    infectiousThreshold = 0.2
    virality = 0.2

    # for each live cell, spread to neighbouring dead cells
    for x in range(grid_size):
        for y in range(grid_size):
            if locations[x, y] >= infectious_threshold:
                spill_over = locations[x, y] * virality
                x_start, x_stop = max(x - 1, 0), min(x + 1, grid_size)
                y_start, y_stop = max(y - 1, 0), min(y + 1, grid_size)

                new_locs[x_start, y] = min(locations[x_start, y] + spill_over, 1)
                new_locs[x_stop, y] = min(locations[x_stop, y] + spill_over, 1)
                new_locs[x, y_start] = min(locations[x, y_start] + spill_over, 1)
                new_locs[x, y_stop] = min(locations[x, y_stop] + spill_over, 1)

    return new_locs


def spread_basic(locations, grid_size, virality):
    new_locs = locations.copy()
    virality = 0.2

    # for each live cell, spread to neighbouring dead cells
    for x in range(grid_size):
        for y in range(grid_size):
            if locations[x, y] >= 1:
                x_start, x_stop = max(x - 1, 0), min(x + 1, grid_size)
                y_start, y_stop = max(y - 1, 0), min(y + 1, grid_size)

                new_locs[x_start, y] += min(new_locs[x_start, y] + virality, 1)
                new_locs[x_stop, y] += min(new_locs[x_stop, y] + virality, 1)
                new_locs[x, y_start] += min(new_locs[x, y_start] + virality, 1)
                new_locs[x, y_stop] += min(new_locs[x, y_stop] + virality, 1)

    return new_locs


def circle_spread(locations, grid_size):
    new_locs = locations.copy()

    # for each live cell, spread to neighbouring dead cells
    for x in range(0, grid_size-1):
        for y in range(0, grid_size-1):
            if locations[x, y] >= 1:
                x_start, x_stop = max(x - 1, 0), min(x + 1, grid_size)
                y_start, y_stop = max(y - 1, 0), min(y + 1, grid_size)

                if new_locs[x_start, y_start] == 0:
                    new_locs[x_start, y_start] = 1 if np.random.randint(100) >= 57 else 0
                if new_locs[x_start, y_stop] == 0:
                    new_locs[x_start, y_stop] = 1 if np.random.randint(100) >= 57 else 0
                if new_locs[x_stop, y_start] == 0:
                    new_locs[x_stop, y_start] = 1 if np.random.randint(100) >= 57 else 0
                if new_locs[x_stop, y_stop] == 0:
                    new_locs[x_stop, y_stop] = 1 if np.random.randint(100) >= 57 else 0

                new_locs[x_start, y] = 1
                new_locs[x_stop, y] = 1
                new_locs[x, y_start] = 1
                new_locs[x, y_stop] = 1

    return new_locs


class SpreadModel:
    pass
