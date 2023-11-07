
class OptionsController:
    def __init__(self, model, view):
        self.model = model
        self.frame = view

        self.states_controller = None
        self.tapes_controller = None
        self.info_controller = None

        self.bind()

    def set_controllers(self, states_controller, tapes_controller, info_controller):
        self.states_controller = states_controller
        self.tapes_controller = tapes_controller
        self.info_controller = info_controller

    def bind(self):
        self.frame.button_add_state.configure(command=self.create_state)
        self.frame.button_add_tape.configure(command=self.create_tape)
        self.frame.button_delete_tape.configure(command=self.delete_tape)

    def create_state(self):
        self.states_controller.create_state_controller()

    def create_tape(self):
        self.tapes_controller.create_tape_controller()

    def delete_tape(self):
        self.tapes_controller.delete_tape_controller()

