import controller


class TapesController:
    def __init__(self, model, view):
        self.model = model
        self.frame = view

        self.states_controller = None
        self.options_controller = None
        self.info_controller = None
        self.tape_controllers = []

    def set_controllers(self, states_controller, options_controller, info_controller):
        self.states_controller = states_controller
        self.options_controller = options_controller
        self.info_controller = info_controller

    def create_tape_controller(self):
        tape_name = str(len(self.model.turing_machine.tapes) + 1)
        tape_view = self.frame.create_tape(tape_name)

        if tape_view is not None:
            self.tape_controllers.append(controller.TapeController(self.model, tape_view))
            self.model.turing_machine.add_tape(tape_view.tape_input)

    def delete_tape_controller(self):
        if self.tape_controllers:
            self.tape_controllers.pop().frame.delete_tape()
            self.model.turing_machine.delete_tape()
