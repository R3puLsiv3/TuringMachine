import customtkinter as ctk
import view


class StatesView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, orientation="horizontal", corner_radius=0)

        self.states = []
        self.add_state()

    def add_state(self):
        state = view.StateView(self)
        state.pack(fill="y", expand=True, side="right", anchor="w", padx="5", pady="5")
        self.states.append(state)

