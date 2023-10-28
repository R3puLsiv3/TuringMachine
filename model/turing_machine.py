import model

BLANK_SYMBOL = " "


class TuringMachine(object):
    def __new__(cls, states=None, tapes=None, entry_state=None):
        if not hasattr(cls, "instance"):
            cls.instance = super(TuringMachine, cls).__new__(cls)

            cls.instance.states: list[model.State] = states
            cls.instance.tapes: list[model.Tape] = tapes
            cls.instance.entry_state: int = entry_state
        return cls.instance

    def get_tape_alphabet(self) -> set[str]:
        return set([transition.write for state in range(len(self.states))
                    for transition in self.states[state].transitions]) \
            .union(self.get_input_alphabet()).union(BLANK_SYMBOL)

    def get_input_alphabet(self) -> set[str]:
        return set([transition.read for state in range(len(self.states))
                    for transition in self.states[state].transitions]).difference(BLANK_SYMBOL)

    def get_halting_states(self):
        return set([state.name for state in self.states if state.is_halting_state])
