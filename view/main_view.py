import customtkinter as ctk
import tkinter as tk
import view


class MainView(tk.PanedWindow):
    def __init__(self, parent):
        super().__init__(parent, orient="vertical", bg="grey", bd=0, sashwidth=6, opaqueresize=False)

        self.controller = None

        # Upper half widgets
        upper_window = ctk.CTkFrame(self, corner_radius=0)

        _options_view = view.OptionsView(upper_window)
        _options_view.pack(fill="x", side="bottom", padx=10, pady=(0, 10))

        _states_view = view.StatesView(upper_window)
        _states_view.pack(fill="both", expand=True, side="top", padx=10, pady=10)

        self.add(upper_window)

        # Lower half widgets
        lower_window = ctk.CTkFrame(self, corner_radius=0)

        _tapes_view = view.TapesView(lower_window)
        _tapes_view.pack(fill="both", expand=True)

        _info_view = view.InfoView(lower_window)
        _info_view.pack(fill="x")

        self.add(lower_window)

    def set_controller(self, controller):
        self.controller = controller
