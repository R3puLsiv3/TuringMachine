import model


class Tape:
    def __init__(self, state, position=None, current_state=None, amortization_value_front=128,
                 amortization_value_back=128):
        self.state: list[str] = state
        self.head = model.Head(position, current_state)
        self.amortization_value_front = amortization_value_front
        self.amortization_value_back = amortization_value_back
        self.space_used = 0

    def append_front_amortized(self):
        to_append: list[str] = [model.BLANK_SYMBOL] * self.amortization_value_front
        self.state = to_append + self.state
        self.amortization_value_front *= 2
        self.head.position += len(to_append)

    def append_back_amortized(self):
        to_append: list[str] = [model.BLANK_SYMBOL] * self.amortization_value_back
        self.state = self.state + to_append
        self.amortization_value_back *= 2


