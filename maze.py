import numpy as np

from game import Cell


def str_to_array(input):
    return [list(r.strip()) for r in input.strip().split('\n')]


class Coor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def valid(self):
        return self.x >= 0 and self.y >= 0


class Maze:
    def __init__(self, init_grid):
        self.grid = np.array(init_grid, dtype=Cell)
        self.width = self.grid.shape[1]
        self.height = self.grid.shape[0]

        self.entrance = Coor(-1, -1)
        self.exit = Coor(-1, -1)

        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y, x] == Cell.ENTRANCE:
                    self.entrance = Coor(x, y)
                elif self.grid[y, x] == Cell.EXIT:
                    self.exit = Coor(x, y)

        if not self.entrance.valid() \
                or not self.exit.valid():
            raise ValueError('invalid maze')

    def __getitem__(self, coor):
        return self.grid[coor.y, coor.x]
