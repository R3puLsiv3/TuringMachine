import model


class Model:
    def __init__(self):
        self.settings_object = model.Settings()
        self.settings = self.settings_object.settings
        self.turing_machine = model.TuringMachine()
