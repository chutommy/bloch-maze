from cell import Cell
from state import State


def transition(current_state, gate):
    if gate in TRANSITIONS[current_state]:
        return TRANSITIONS[current_state][gate]
    return current_state


TRANSITIONS = {
    State.ZERO: {
        Cell.X_GATE: State.ONE,
        Cell.Y_GATE: State.ONE,
        Cell.Z_GATE: State.ZERO,
        Cell.H_GATE: State.PLUS,
        Cell.S_GATE: State.ZERO,
        Cell.RESET_0_GATE: State.ZERO,
        Cell.RESET_1_GATE: State.ONE,
    },

    State.ONE: {
        Cell.X_GATE: State.ZERO,
        Cell.Y_GATE: State.ZERO,
        Cell.Z_GATE: State.ONE,
        Cell.H_GATE: State.MINUS,
        Cell.S_GATE: State.ONE,
        Cell.RESET_0_GATE: State.ZERO,
        Cell.RESET_1_GATE: State.ONE,
    },

    State.PLUS: {
        Cell.X_GATE: State.PLUS,
        Cell.Y_GATE: State.MINUS,
        Cell.Z_GATE: State.MINUS,
        Cell.H_GATE: State.ZERO,
        Cell.S_GATE: State.Y_PLUS,
        Cell.RESET_0_GATE: State.ZERO,
        Cell.RESET_1_GATE: State.ONE,
    },

    State.MINUS: {
        Cell.X_GATE: State.MINUS,
        Cell.Y_GATE: State.PLUS,
        Cell.Z_GATE: State.PLUS,
        Cell.H_GATE: State.ONE,
        Cell.S_GATE: State.Y_MINUS,
        Cell.RESET_0_GATE: State.ZERO,
        Cell.RESET_1_GATE: State.ONE,
    },

    State.Y_PLUS: {
        Cell.X_GATE: State.Y_MINUS,
        Cell.Y_GATE: State.Y_PLUS,
        Cell.Z_GATE: State.Y_MINUS,
        Cell.H_GATE: State.Y_MINUS,
        Cell.S_GATE: State.MINUS,
        Cell.RESET_0_GATE: State.ZERO,
        Cell.RESET_1_GATE: State.ONE,
    },

    State.Y_MINUS: {
        Cell.X_GATE: State.Y_PLUS,
        Cell.Y_GATE: State.Y_MINUS,
        Cell.Z_GATE: State.Y_PLUS,
        Cell.H_GATE: State.Y_PLUS,
        Cell.S_GATE: State.PLUS,
        Cell.RESET_0_GATE: State.ZERO,
        Cell.RESET_1_GATE: State.ONE,
    },
}
