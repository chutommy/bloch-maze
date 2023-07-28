import os

from maze import parse_maze


class Level:
    """Represents an instance of a game level."""

    def __init__(self, title, start_state, end_state, maze):
        self.title = title
        self.maze = maze
        self.start_state = start_state
        self.end_state = end_state

    def validate(self, dimensions):
        """Checks the state and dimensions of the level."""
        if not self.title or not self.start_state or not self.end_state \
                or self.maze.grid.shape[0] > dimensions['height'] \
                or self.maze.grid.shape[1] > dimensions['width']:
            raise ValueError('invalid level')


def get_levels(dir, dimensions):
    """Retrieves the list of all levels."""
    levels = []
    level_files = os.listdir(dir)
    level_files.sort()
    for file in level_files:
        levels.append(load_level_from_file(os.path.join(dir, file), dimensions))
    for level in levels:
        level.validate(dimensions)
    return levels


def load_level_from_file(path, dimensions):
    with open(path, 'r') as file:
        title = file.readline().strip().lower()
        start_state, end_state = file.readline().strip().replace(' ', '').split('->')
        maze = parse_maze(file.read(), dimensions)
        return Level(title, start_state, end_state, maze)
