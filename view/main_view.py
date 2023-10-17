from tkinter import ttk
import view


class MainView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = None

        states_view = view.StatesView(self)
        tapes_view_ = view.TapesView(self)
        options_view = view.OptionsView(self)

    def set_controller(self, controller):
        self.controller = controller
