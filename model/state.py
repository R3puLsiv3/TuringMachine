import model


class State:
    def __init__(self, is_halting_state=False, transitions=None):
        self.is_halting_state: bool = is_halting_state
        self.transitions: list[model.Transition] = transitions or []

    def list_transitions(self) -> list[str]:
        transitions_list = []
        for transition in self.transitions:
            transitions_list.append(str(transition.tape) + " " + transition.read + " " + transition.write + " " +
                                    transition.movement + " " + transition.new_state)
