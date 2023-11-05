import customtkinter as ctk
import view


class StatesView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, orientation="horizontal", corner_radius=0)
        self.states: list[view.StateView] = []

    def create_state(self):
        state = view.StateView(self)
        state.pack(fill="y", expand=True, side="left", anchor="w", padx="5", pady="5")
        self.states.append(state)
        return state

    def delete_states(self):
        for state in self.states:
            state.destroy()

    def set_entry(self, entry_state):
        for state in self.states:
            if state is not entry_state:
                state.is_entry = True
                state.set_entry()

