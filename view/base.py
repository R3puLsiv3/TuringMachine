import view


class View:
    def __init__(self):
        self.root = view.Root()
        self.options_frame = self.root.main_view.options_view
        self.state_frame = self.root.main_view.states_view
        self.state_frames = {}
        self.tape_frames = {}

    def add_state_frame(self, frame, name):
        self.state_frames[name] = frame

    def add_tape_frame(self, frame, name):
        self.tape_frames[name] = frame

    def start_mainloop(self):
        self.root.mainloop()
