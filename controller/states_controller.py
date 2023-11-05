import controller


class StatesController:
    def __init__(self, model, view):
        self.model = model
        self.frame = view

        self.tapes_controller = None
        self.options_controller = None
        self.info_controller = None
        self.state_controllers = []

    def set_controllers(self, tapes_controller, options_controller, info_controller):
        self.tapes_controller = tapes_controller
        self.options_controller = options_controller
        self.info_controller = info_controller

    def create_state_controller(self):
        self.state_controllers.append(controller.StateController(self, self.model, self.frame.create_state()))

    def delete_state_controller(self, state_controller):
        self.state_controllers.remove(state_controller)

