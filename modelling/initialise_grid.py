import numpy as np


def random_start(locations, grid_size, num_seeds):
    centre = grid_size // 2
    grid_quarter = grid_size // 4
    for i in range(num_seeds):
        seedX = np.random.randint(centre - grid_quarter, centre + grid_quarter)
        seedY = np.random.randint(centre - grid_quarter, centre + grid_quarter)
        locations[seedX, seedY] = 1


class InitialiseGrid:
    pass
