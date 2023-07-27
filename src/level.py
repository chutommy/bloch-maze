from maze import Maze, parse_maze
from qstate import QState
from config import *


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
                or self.maze.grid.shape[0] > DIMENSIONS[0] \
                or self.maze.grid.shape[1] > DIMENSIONS[1]:
            raise ValueError('invalid level')


def get_levels():
    """Retrieves the list of all levels."""
    dimensions = levels[0].maze.grid.shape
    for level in levels:
        level.validate(dimensions)
    return levels, dimensions


levels = [
    Level("playground", QState.ZERO, QState.PLUS, Maze(parse_maze("""
    
    wwwwwwwwww
    wA.......w
    w..X.Y.Z.w
    w........w
    w..H.S...w
    w..0.1...w
    w.......Bw
    wwwwwwwwww
    
    """))),
    Level("warm-up", QState.ZERO, QState.PLUS, Maze(parse_maze("""
    
    wwwwwwwwww
    wA...H..Bw
    wwwwwwwwww
    
    """))),
    Level("don't rush", QState.ZERO, QState.ZERO, Maze(parse_maze("""
    
    wwwwwwwwww
    wA...H..Bw
    wwww.www.w
    ...w.w.w.w
    ...w.www.w
    ...w.....w
    ...wwwwwww

"""))),
]
