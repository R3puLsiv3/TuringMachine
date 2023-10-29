
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

    def create_state(self):
        self.states_controller.create_state()

