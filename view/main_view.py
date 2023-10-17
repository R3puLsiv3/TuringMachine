from tkinter import ttk
import tkinter as tk
import view


class MainView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=5)

        states_view = view.StatesView(self)
        states_view.grid(column=0, row=0)

        tapes_view_ = view.TapesView(self)
        options_view = view.OptionsView(self)

    def set_controller(self, controller):
        self.controller = controller
