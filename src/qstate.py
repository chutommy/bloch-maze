from enum import Enum

from config import *


class QState(str, Enum):
    """Lists the basic quantum states."""

    ZERO = STATE_SYMBOL_ZERO
    ONE = STATE_SYMBOL_ONE
    PLUS = STATE_SYMBOL_PLUS
    MINUS = STATE_SYMBOL_MINUS
    Y_PLUS = STATE_SYMBOL_Y_PLUS
    Y_MINUS = STATE_SYMBOL_Y_MINUS
