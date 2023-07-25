from enum import Enum


class Cell(str, Enum):
    NONE = '.'
    WALL = 'w'
    ENTRANCE = 'A'
    EXIT = 'B'

    X_GATE = 'X'
    Y_GATE = 'Y'
    Z_GATE = 'Z'
    H_GATE = 'H'
    S_GATE = 'S'
    RESET_0_GATE = '0'
    RESET_1_GATE = '1'


CELL_COLORS = {
    Cell.NONE: (255, 255, 255),
    Cell.WALL: (100, 100, 100),
    Cell.ENTRANCE: (50, 205, 50),
    Cell.EXIT: (255, 49, 49),

    Cell.X_GATE: (0, 170, 255),
    Cell.Y_GATE: (0, 204, 102),
    Cell.Z_GATE: (255, 102, 102),
    Cell.H_GATE: (255, 153, 0),
    Cell.S_GATE: (204, 153, 255),
    Cell.RESET_0_GATE: (130, 130, 130),
    Cell.RESET_1_GATE: (130, 130, 130),
}
