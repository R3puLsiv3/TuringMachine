
class StatesController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.state_frame
        self.frames = self.view.state_frames

        self.tapes_controller = None
        self.options_controller = None
        self.info_controller = None

    def set_controllers(self, tapes_controller, options_controller, info_controller):
        self.tapes_controller = tapes_controller
        self.options_controller = options_controller
        self.info_controller = info_controller

    def create_state(self):
        self.frame.create_state()

