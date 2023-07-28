import os

from config import *
from maze import parse_maze


class Level:
    """Represents an instance of a game level."""

    def __init__(self, title, start_state, end_state, maze):
        self.title = title
        self.maze = maze
        self.start_state = start_state
        self.end_state = end_state

    def validate(self):
        """Checks the state and dimensions of the level."""
        if not self.title or not self.start_state or not self.end_state \
                or self.maze.grid.shape[0] > DIMENSIONS[0] \
                or self.maze.grid.shape[1] > DIMENSIONS[1]:
            raise ValueError('invalid level')


def get_levels():
    """Retrieves the list of all levels."""
    levels = []
    level_files = os.listdir(LEVELS)
    level_files.sort()
    for file in level_files:
        levels.append(load_level_from_file(os.path.join(LEVELS, file)))
    for level in levels:
        level.validate()
    return levels


def load_level_from_file(path):
    with open(path, 'r') as file:
        title = file.readline().strip().lower()
        start_state, end_state = file.readline().strip().replace(' ', '').split('->')
        maze = parse_maze(file.read())
        return Level(title, start_state, end_state, maze)
