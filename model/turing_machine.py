

class TuringMachine(object):

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(TuringMachine, cls).__new__(cls)

            # For the current state s, states[s] is a collection of possible transitions of the form
            # current input -> [output, head movement, next state]
            cls.instance.states: list[dict[str, list[str, str, int]]] = []
            cls.instance.current_state = 0
            cls.instance.blank_symbol = "_"
        return cls.instance

    def get_tape_alphabet(self) -> set[str]:
        return set([self.states[i][key][0] for i in range(len(self.states)) for key in self.states[i]])\
            .union(self.get_input_alphabet()).union(self.blank_symbol)

    def get_input_alphabet(self) -> set[str]:
        return set([key for i in range(len(self.states)) for key in self.states[i]])\
            .difference(self.blank_symbol)
