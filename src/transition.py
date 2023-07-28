from src.cell import Cell
from src.qstate import QState


def transition(current_state, gate):
    """Returns the state after applying the given gate on the current state."""
    if gate in TRANSITIONS[current_state]:
        return TRANSITIONS[current_state][gate]
    return current_state


TRANSITIONS = {
    QState.ZERO: {
        Cell.X_GATE: QState.ONE,
        Cell.Y_GATE: QState.ONE,
        Cell.Z_GATE: QState.ZERO,
        Cell.H_GATE: QState.PLUS,
        Cell.S_GATE: QState.ZERO,
        Cell.RESET_0_GATE: QState.ZERO,
        Cell.RESET_1_GATE: QState.ONE,
    },

    QState.ONE: {
        Cell.X_GATE: QState.ZERO,
        Cell.Y_GATE: QState.ZERO,
        Cell.Z_GATE: QState.ONE,
        Cell.H_GATE: QState.MINUS,
        Cell.S_GATE: QState.ONE,
        Cell.RESET_0_GATE: QState.ZERO,
        Cell.RESET_1_GATE: QState.ONE,
    },

    QState.PLUS: {
        Cell.X_GATE: QState.PLUS,
        Cell.Y_GATE: QState.MINUS,
        Cell.Z_GATE: QState.MINUS,
        Cell.H_GATE: QState.ZERO,
        Cell.S_GATE: QState.Y_PLUS,
        Cell.RESET_0_GATE: QState.ZERO,
        Cell.RESET_1_GATE: QState.ONE,
    },

    QState.MINUS: {
        Cell.X_GATE: QState.MINUS,
        Cell.Y_GATE: QState.PLUS,
        Cell.Z_GATE: QState.PLUS,
        Cell.H_GATE: QState.ONE,
        Cell.S_GATE: QState.Y_MINUS,
        Cell.RESET_0_GATE: QState.ZERO,
        Cell.RESET_1_GATE: QState.ONE,
    },

    QState.Y_PLUS: {
        Cell.X_GATE: QState.Y_MINUS,
        Cell.Y_GATE: QState.Y_PLUS,
        Cell.Z_GATE: QState.Y_MINUS,
        Cell.H_GATE: QState.Y_MINUS,
        Cell.S_GATE: QState.MINUS,
        Cell.RESET_0_GATE: QState.ZERO,
        Cell.RESET_1_GATE: QState.ONE,
    },

    QState.Y_MINUS: {
        Cell.X_GATE: QState.Y_PLUS,
        Cell.Y_GATE: QState.Y_MINUS,
        Cell.Z_GATE: QState.Y_PLUS,
        Cell.H_GATE: QState.Y_PLUS,
        Cell.S_GATE: QState.PLUS,
        Cell.RESET_0_GATE: QState.ZERO,
        Cell.RESET_1_GATE: QState.ONE,
    },
}
