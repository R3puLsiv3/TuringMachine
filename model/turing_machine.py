import model
import re

BLANK_SYMBOL = " "
TRANSITION_REGEX = re.compile("[1-9][0,9]*:.?->.,[LRN],.+")


class TuringMachine(object):
    def __new__(cls, states=None, tapes=None, entry_state=None):
        if not hasattr(cls, "instance"):
            cls.instance = super(TuringMachine, cls).__new__(cls)

            cls.instance.states: dict[str, model.State] = states or {}
            cls.instance.tapes: list[model.Tape] = tapes or []
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

    def add_state(self, name: str, is_halting_state: bool, transitions: str):
        parsed_transitions: list[model.Transition] = []
        split_transitions = transitions.splitlines()
        for transition in split_transitions:
            transition.replace(" ", "")
            transitions.lstrip("0")
            if TRANSITION_REGEX.fullmatch(transition):
                tape_split = transition.split(":", 1)
                tape = int(tape_split[0])

                read = tape_split[1][0]
                rest = tape_split[1][3:]

                if tape_split[1].startswith("->"):
                    read = BLANK_SYMBOL
                    rest = tape_split[1][2:]

                write = rest[0]
                rest = rest[2:]

                movement = rest[0]
                new_state = rest[2:]

                parsed_transitions.append(model.Transition(tape, read, write, movement, new_state))

        if name not in self.states.keys():
            self.states[name] = model.State(is_halting_state, parsed_transitions)
