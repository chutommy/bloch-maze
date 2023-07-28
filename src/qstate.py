import enum


class QState(str, enum.Enum):
    """Lists the basic quantum states."""

    ZERO = '❘0❭'
    ONE = '❘1❭'
    PLUS = '❘+❭'
    MINUS = '❘-❭'
    Y_PLUS = '❘R❭'
    Y_MINUS = '❘L❭'
