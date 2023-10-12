from tkinter import ttk
import view


class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        states_view = view.StatesView(self)
        tapes_view_ = view.TapesView(self)
        options_view = view.OptionsView(self)
