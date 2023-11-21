
class TapeController:
    def __init__(self, model, view, tape_number):
        self.model = model
        self.frame = view
        self.tape_number = tape_number

    def read_symbol(self):
        return self.model.turing_machine.tapes[self.tape_number].read()

    def perform_transition(self, write, movement, new_state):
        self.frame.labels[self.frame.pos].configure(text=write)
        self.model.turing_machine.tapes[self.tape_number].write(write)
        match movement:
            case "L":
                self.frame.do_after(-1)
                self.frame.pos -= 1
                self.model.turing_machine.tapes[self.tape_number].set_position(-1)
            case "N":
                self.frame.do_after(0)
            case "R":
                self.frame.do_after(1)
                self.frame.pos += 1
                self.model.turing_machine.tapes[self.tape_number].set_position(1)

        self.model.turing_machine.current_state = new_state
