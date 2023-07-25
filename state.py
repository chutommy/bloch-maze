from enum import Enum


class State(str, Enum):
    ZERO = '❘0❭'
    ONE = '❘1❭'
    PLUS = '❘+❭'
    MINUS = '❘-❭'
    Y_PLUS = '❘y+❭'
    Y_MINUS = '❘y-❭'
