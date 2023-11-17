import time


class TapeController:
    def __init__(self, model, view, tape_number):
        self.model = model
        self.frame = view
        self.tape_number = tape_number

    def find_transition(self):
        symbol_read = self.model.turing_machine.tapes[self.tape_number].read()
        for transition in self.model.turing_machine.states[self.model.turing_machine.current_state].transitions:
            if transition.read == symbol_read:
                return transition
        raise ValueError

    def perform_transition(self, transition):
        time.sleep(0.3)
        self.frame.labels[self.frame.pos].configure(text=transition.write)
        self.model.turing_machine.tapes[self.tape_number].write(transition.write)
        time.sleep(0.3)
        match transition.movement:
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

        self.model.turing_machine.current_state = transition.new_state
