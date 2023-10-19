import customtkinter as ctk
from tkinter import ttk
import view


class MainView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.controller = None

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("cool.TPanedwindow", background="grey")

        paned_window = ttk.PanedWindow(self, orient="vertical", style="cool.TPanedwindow")
        paned_window.pack(fill="both", expand=True)

        states_view = view.StatesView(paned_window)
        states_view.pack(fill="x", expand=True, anchor="n")
        paned_window.add(states_view)

        example_label = ctk.CTkLabel(paned_window, text="Hallo", bg_color="white")
        paned_window.add(example_label)

        options_view = view.OptionsView(self)

        tapes_view_ = view.TapesView(self)

    def set_controller(self, controller):
        self.controller = controller
