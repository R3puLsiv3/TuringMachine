import controller
from tkinter import messagebox


class TapesController:
    def __init__(self, model, view):
        self.model = model
        self.frame = view

        self.states_controller = None
        self.options_controller = None
        self.info_controller = None
        self.tape_controllers = []

        self.is_playing = False

    def set_controllers(self, states_controller, options_controller, info_controller):
        self.states_controller = states_controller
        self.options_controller = options_controller
        self.info_controller = info_controller

    def create_tape_controller(self):
        tape_number = (len(self.model.turing_machine.tapes))
        tape_name = str(tape_number + 1)
        tape_view = self.frame.create_tape(tape_name)

        if tape_view is not None:
            self.tape_controllers.append(controller.TapeController(self.model, tape_view, tape_number))
            self.model.turing_machine.add_tape(tape_view.tape_input)

    def delete_tape_controller(self):
        if self.tape_controllers:
            self.tape_controllers.pop().frame.delete_tape()
            self.model.turing_machine.delete_tape()

    def play(self):
        if self.model.turing_machine.entry_state not in self.model.turing_machine.states.keys():
            messagebox.showinfo(title="No entry state",
                                message="Turing machine requires an entry state.")
            return
        self.model.turing_machine.current_state = self.model.turing_machine.entry_state

        self.is_playing = True
        while self.is_playing:
            self.perform_step()

    def perform_step(self):
        transitions = []
        for tape_controller in self.tape_controllers:
            try:
                transition = tape_controller.find_transition()
                transitions.append(transition)
                print(transition.read, transition.write, transition.movement, transition.new_state)
            except ValueError:
                if self.model.turing_machine.states[self.model.turing_machine.current_state].is_halting_state:
                    self.info_controller.show_accept()
                else:
                    self.info_controller.show_not_accept()

        for index, transition in enumerate(transitions):
            self.tape_controllers[index].perform_transition(transition)

    def delete_tape_controllers(self):
        self.tape_controllers.clear()
        self.model.turing_machine.reset_turing_machine()
        self.frame.delete_tapes()

