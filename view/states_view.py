import customtkinter as ctk
import view


class StatesView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, orientation="horizontal", corner_radius=0)

    def add_state(self, name: str):
        state = view.StateView(self, name)
        state.pack(fill="y", expand=True, side="right", anchor="w", padx="5", pady="5")

