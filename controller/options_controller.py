import threading


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
        self.frame.button_play.configure(command=lambda: threading.Thread(target=self.play, daemon=True).start())

    def create_state(self):
        self.states_controller.create_state_controller()

    def create_tape(self):
        self.tapes_controller.create_tape_controller()

    def delete_tape(self):
        self.tapes_controller.delete_tape_controller()

    def play(self):
        # TODO: Check if turing machine is in order and make it impossible to change turing machine during play
        if self.tapes_controller.is_playing:
            self.frame.button_play.configure(text="Play")
            self.tapes_controller.is_playing = False
        else:
            self.frame.button_play.configure(text="Pause")
            self.tapes_controller.play()
            self.model.turing_machine.entry_state = self.model.turing_machine.current_state


