from model.transition import Transition
from model.tape import Tape
from model.state import State

BLANK_SYMBOL = " "


class TuringMachine(object):
    def __new__(cls, states=None, tapes=None, entry_state=None):
        if not hasattr(cls, "instance"):
            cls.instance = super(TuringMachine, cls).__new__(cls)

            cls.instance.states: dict[str, State] = states or {}
            cls.instance.tapes: list[Tape] = tapes or []
            cls.instance.entry_state: int = entry_state
        return cls.instance

    def get_tape_alphabet(self) -> set[str]:
        return set([transition.write for state in self.states.keys()
                    for transition in self.states[state].transitions]) \
            .union(self.get_input_alphabet()).union(BLANK_SYMBOL)

    def get_input_alphabet(self) -> set[str]:
        return set([transition.read for state in self.states.keys()
                    for transition in self.states[state].transitions]).difference(BLANK_SYMBOL)

    def get_halting_states(self):
        return set([name for name in self.states.keys() if self.states[name].is_halting_state])

    def check_name(self, name: str):
        if name in self.states.keys() or not name:
            raise ValueError

    def add_state(self, name: str, is_halting_state: bool, transitions: list[Transition]):
        self.states[name] = State(is_halting_state, transitions)

