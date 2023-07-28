import numpy as np

from config import *
from coor import Coor
from game import Cell


def parse_maze(text):
    """Parses a maze string to a 2D grid."""
    stripped = [list(r.strip()) for r in text.strip().upper().split('\n')]
    np_stripped = np.array(stripped, dtype=Cell)

    width_remaining = DIMENSIONS[1] - np_stripped.shape[1]
    height_remaining = DIMENSIONS[0] - np_stripped.shape[0]
    left = width_remaining // 2
    right = width_remaining - left
    top = height_remaining // 2
    bottom = height_remaining - top
    padded = np.pad(stripped, ((top, bottom), (left, right)), constant_values='.')

    return Maze(padded)


class Maze:
    """Represents a general maze grid."""

    def __init__(self, init_grid):
        self.grid = np.array(init_grid, dtype=Cell)
        self.width = self.grid.shape[1]
        self.height = self.grid.shape[0]

        # initialize entrance and exit
        self.entrance = Coor(-1, -1)
        self.exit = Coor(-1, -1)
        for x in range(self.width):
            for y in range(self.height):
                if self[x, y] == Cell.ENTRANCE:
                    self.entrance = Coor(x, y)
                elif self[x, y] == Cell.EXIT:
                    self.exit = Coor(x, y)
        if not self.entrance.valid() or not self.exit.valid():
            raise ValueError('invalid maze')

    def __getitem__(self, key):
        if isinstance(key, tuple):
            # (x, y)
            return self.grid[key[1], key[0]]
        elif isinstance(key, Coor):
            # Coor(x, y)
            return self.grid[key.y, key.x]
        raise ValueError(f'invalid key: {key}')
