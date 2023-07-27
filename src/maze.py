import numpy as np

from coor import Coor
from game import Cell
from config import *


def parse_maze(text):
    """Parses a maze string to a 2D grid."""
    return [list(r.strip()) for r in text.strip().split('\n')]


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
