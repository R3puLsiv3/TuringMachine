import model


class State:

    def __init__(self, name=None, is_halting_state=False, transitions=None):
        self.name: str = name
        self.halt: bool = is_halting_state
        self.transitions: list[model.Transition] = transitions
