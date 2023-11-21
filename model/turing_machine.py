from model.transition import Transition
from model.tape import Tape
from model.state import State
from model.tape import TAPE_PADDING

BLANK_SYMBOL = " "


class TuringMachine(object):
    def __new__(cls, states=None, tapes=None, entry_state=None):
        if not hasattr(cls, "instance"):
            cls.instance = super(TuringMachine, cls).__new__(cls)

            cls.instance.states: dict[str, State] = states or {}
            cls.instance.tapes: list[Tape] = tapes or []
            cls.instance.entry_state: str = entry_state
            cls.instance.current_state: str = entry_state

            # Table for faster lookup of transitions
            # (state, read_symbols) -> (write_symbols, movements, new_state)
            cls.instance.multi_tape_transitions: dict[tuple[str, tuple[str, ...]], tuple[tuple[str], tuple[str], str]] = {}
            cls.instance.single_tape_transitions: dict[tuple[str, str], tuple[str, str, str]] = {}
        return cls.instance

    def create_single_tape_transitions(self):
        for state in self.states:
            for transition in self.states[state].transitions:
                self.single_tape_transitions[(state, transition.read[0])] = (transition.write[0], transition.movement[0], transition.new_state)

    def create_multi_tape_transitions(self):
        for state in self.states:
            for transition in self.states[state].transitions:
                self.multi_tape_transitions[(state, tuple(transition.read))] = (tuple(transition.write), tuple(transition.movement), transition.new_state)

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
        return name.replace(" ", "")

    def add_state(self, name: str, is_halting_state: bool, transitions: list[Transition]):
        self.states[name] = State(is_halting_state, transitions)

    def delete_state(self, name):
        del self.states[name]

    def add_tape(self, tape_input):
        tape_state = [BLANK_SYMBOL] * TAPE_PADDING + list(tape_input) + [BLANK_SYMBOL] * TAPE_PADDING
        self.tapes.append(Tape(tape_state))

    def delete_tape(self):
        del self.tapes[:-1]

    def reset_turing_machine(self):
        self.tapes.clear()

