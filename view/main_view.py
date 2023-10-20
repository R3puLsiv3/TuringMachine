import customtkinter as ctk
from tkinter import ttk
import view


class MainView(ttk.PanedWindow):
    def __init__(self, parent):
        super().__init__(parent, orient="vertical", style="cool.TPanedwindow")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("cool.TPanedwindow", background="grey")

        self.controller = None

        upper_window = ctk.CTkFrame(self, corner_radius=0)

        _options_view = view.OptionsView(upper_window)
        _options_view.pack(fill="x", side="bottom", padx=10, pady=(0, 10))

        _states_view = view.StatesView(upper_window)
        _states_view.pack(fill="both", expand=True, side="top", padx=10, pady=10)

        self.add(upper_window, weight=0)

        _tapes_view = view.TapesView(self)

        self.add(_tapes_view)

    def set_controller(self, controller):
        self.controller = controller
