import model

TAPE_PADDING = 64


class Tape:
    def __init__(self, state, position=0, true_position=TAPE_PADDING,
                 amortization_value_front=TAPE_PADDING * 2, amortization_value_back=TAPE_PADDING * 2):
        self.state: list[str] = state
        self.true_position = true_position
        self.position = position
        self.amortization_value_front = amortization_value_front
        self.amortization_value_back = amortization_value_back
        self.space_used = 0

    def append_front_amortized(self):
        to_append: list[str] = [model.BLANK_SYMBOL] * self.amortization_value_front
        self.state = to_append + self.state
        self.amortization_value_front *= 2
        self.true_position += len(to_append)

    def append_back_amortized(self):
        to_append: list[str] = [model.BLANK_SYMBOL] * self.amortization_value_back
        self.state = self.state + to_append
        self.amortization_value_back *= 2

    def read(self):
        return self.state[self.true_position]

    def set_position(self, direction):
        self.position += direction
        self.true_position += direction

    def write(self, symbol: str):
        self.state[self.true_position] = symbol

