import model


class TuringMachine(object):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(TuringMachine, cls).__new__(cls)

            # For the current state s and tape t states[s][t] is a collection of possible transitions of the form:
            # current input -> [output, head movement, next state]
            cls.instance.states: list[list[dict[str, list[str, str, int]]]] = []
            cls.instance.halting_states: set = {}
            cls.instance.current_state = 0
            cls.instance.blank_symbol = " "
        return cls.instance

    def get_tape_alphabet(self) -> set[str]:
        return set([self.states[state][tape][inp][0] for state in range(len(self.states))
                    for tape in range(len(self.states[state])) for inp in self.states[state][tape]])\
            .union(self.get_input_alphabet()).union(self.blank_symbol)

    def get_input_alphabet(self) -> set[str]:
        return set([key for state in range(len(self.states)) for tape in range(len(self.states[state]))
                   for key in self.states[state][tape]]).difference(self.blank_symbol)
