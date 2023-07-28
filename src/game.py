import enum

from cell import Cell
from coor import Coor
from transition import transition


class GameState(int, enum.Enum):
    """Represents the state of the game."""

    RUNNING = enum.auto()
    JUMP = enum.auto()
    SUCCESS = enum.auto()
    FAIL = enum.auto()


class Game:
    """Represents an instance of a level."""

    def __init__(self, level):
        self.level = level
        self.maze = self.level.maze
        self.player = self.level.maze.entrance
        self.player_state = self.level.start_state
        self.state = GameState.RUNNING

    def set_jump(self):
        self.state = GameState.JUMP

    def set_success(self):
        self.state = GameState.SUCCESS

    def set_fail(self):
        self.state = GameState.FAIL

    def evaluate(self):
        """Evaluates the player's position and updates the state of the game."""
        if self.maze[self.player] == Cell.ENTRANCE:
            self.player_state = self.level.start_state
        elif self.maze[self.player] == Cell.EXIT:
            if self.player_state == self.level.end_state:
                self.set_success()
            else:
                self.set_fail()
        else:
            self.player_state = transition(self.player_state, self.maze[self.player])

    def move(self, dx, dy):
        """Updates the player's position."""
        new_coor = Coor(self.player.x + dx, self.player.y + dy)
        if self.maze[new_coor] != Cell.WALL:
            self.player = new_coor
            self.evaluate()

    def move_up(self):
        self.move(0, -1)

    def move_down(self):
        self.move(0, +1)

    def move_left(self):
        self.move(-1, 0)

    def move_right(self):
        self.move(+1, 0)
