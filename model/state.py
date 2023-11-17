import model


class State:
    def __init__(self, is_halting_state=False, transitions=None):
        self.is_halting_state: bool = is_halting_state
        self.transitions: list[model.Transition] = transitions or []

    def to_dict(self) -> list[dict[str]]:
        transitions = []
        for transition in self.transitions:
            transitions_entry = {"read": transition.read, "write": transition.write,
                                 "movement": transition.movement, "new_state": transition.new_state}
            transitions.append(transitions_entry)
        return transitions

