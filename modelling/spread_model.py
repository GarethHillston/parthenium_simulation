import numpy as np
import random


def markov_basic_all(locations, transition_matrix):
    new_locs = locations.copy()
    classes = range(len(transition_matrix))
    shape = np.shape(locations)
    size_x = shape[0]
    size_y = shape[1]

    # for each cell, transition randomly as per matrix
    for x in range(0, size_x - 1):
        for y in range(0, size_y - 1):
            new_locs[x, y] = random.choices(classes, transition_matrix[locations[x][y]], k=1)[0]

    return new_locs


def markov_basic(locations, transition_matrix):
    new_locs = locations.copy()
    classes = range(len(transition_matrix))
    shape = np.shape(locations)
    size_x = shape[0]
    size_y = shape[1]

    # for each cell, transition randomly as per matrix
    for x in range(0, size_x - 1):
        for y in range(0, size_y - 1):
            if locations[x, y] == 1:
                x_start, x_stop = max(x - 1, 0), min(x + 1, size_x)
                y_start, y_stop = max(y - 1, 0), min(y + 1, size_y)

                for i in range(x_start, x_stop+1):
                    for j in range(y_start, y_stop+1):
                        new_locs[i, j] = random.choices(classes, transition_matrix[locations[i][j]], k=1)[0]

    return new_locs


def spread_basic_threshold(locations, grid_size, infectious_threshold):
    new_locs = locations.copy()
    virality = 0.2
    size_x = grid_size[0]
    size_y = grid_size[1]

    # for each live cell, spread to neighbouring dead cells
    for x in range(size_x):
        for y in range(size_y):
            if locations[x, y] >= infectious_threshold:
                spill_over = locations[x, y] * virality
                x_start, x_stop = max(x - 1, 0), min(x + 1, size_x)
                y_start, y_stop = max(y - 1, 0), min(y + 1, size_y)

                new_locs[x_start, y] = min(locations[x_start, y] + spill_over, 1)
                new_locs[x_stop, y] = min(locations[x_stop, y] + spill_over, 1)
                new_locs[x, y_start] = min(locations[x, y_start] + spill_over, 1)
                new_locs[x, y_stop] = min(locations[x, y_stop] + spill_over, 1)

    return new_locs


def spread_basic(locations, grid_size, virality):
    new_locs = locations.copy()
    virality = 0.2
    size_x = grid_size[0]
    size_y = grid_size[1]

    # for each live cell, spread to neighbouring dead cells
    for x in range(size_x):
        for y in range(size_y):
            if locations[x, y] >= 1:
                x_start, x_stop = max(x - 1, 0), min(x + 1, size_x)
                y_start, y_stop = max(y - 1, 0), min(y + 1, size_y)

                new_locs[x_start, y] += min(new_locs[x_start, y] + virality, 1)
                new_locs[x_stop, y] += min(new_locs[x_stop, y] + virality, 1)
                new_locs[x, y_start] += min(new_locs[x, y_start] + virality, 1)
                new_locs[x, y_stop] += min(new_locs[x, y_stop] + virality, 1)

    return new_locs


def circle_spread(locations, matrix):
    new_locs = locations.copy()
    classes = range(len(matrix))
    grid_size = np.shape(locations)
    size_x = grid_size[0]
    size_y = grid_size[1]

    # for each live cell, spread to neighbouring dead cells
    for x in range(0, size_x-1):
        for y in range(0, size_y-1):
            if locations[x, y] >= 1:
                new_locs[x, y] = random.choices(classes, matrix[locations[x][y]], k=1)[0]

                x_start, x_stop = max(x - 1, 0), min(x + 1, size_x)
                y_start, y_stop = max(y - 1, 0), min(y + 1, size_y)

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


def circle_spread_lulc(locations, matrix, land_types, lulc_proportions):
    new_locs = locations.copy()
    classes = range(len(matrix))
    grid_size = np.shape(locations)
    size_x = grid_size[0]
    size_y = grid_size[1]

    # for each live cell, spread to neighbouring dead cells
    for x in range(0, size_x-1):
        for y in range(0, size_y-1):
            if locations[x, y] > 0:
                x_start, x_stop = max(x - 1, 0), min(x + 1, size_x)
                y_start, y_stop = max(y - 1, 0), min(y + 1, size_y)

                probability_grid = [
                    [0.57, 1.0, 0.57],
                    [1.0, 1.0, 1.0],
                    [0.57, 1.0, 0.57]]

                land_prob_grid = np.zeros((3, 3), dtype=float)

                x_offset = 1 if x_start != x - 1 else 0
                y_offset = 1 if y_start != y - 1 else 0

                for i, loc_x in zip(range(3-x_offset), range(x_start, x_stop+1)):
                    for j, loc_y in zip(range(3-y_offset), range(y_start, y_stop+1)):
                        land_prob_grid[i+x_offset, j+y_offset] = lulc_proportions[land_types[loc_x][loc_y]]

                probability_grid *= land_prob_grid

                # if np.sum(land_prob_grid > 0):
                #     print(np.array(probability_grid).flatten())
                #     print()
                #     for loc_x in range(x_start, x_stop + 1):
                #         for loc_y in range(y_start, y_stop + 1):
                #             print(new_locs[loc_x][loc_y], end=',')
                #     print()

                for i, loc_x in zip(range(3 - x_offset), range(x_start, x_stop + 1)):
                    for j, loc_y in zip(range(3 - y_offset), range(y_start, y_stop + 1)):
                        if new_locs[loc_x][loc_y] == 0:
                            new_locs[loc_x][loc_y] = 1 if np.random.random() <= probability_grid[i][j] else 0

                # if np.sum(land_prob_grid > 0):
                #     for loc_x in range(x_start, x_stop + 1):
                #         for loc_y in range(y_start, y_stop + 1):
                #             print(new_locs[loc_x][loc_y], end=',')
                #     print()
                #     print()

    return new_locs


class SpreadModel:
    pass
