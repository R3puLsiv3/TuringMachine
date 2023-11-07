import customtkinter as ctk
import view


class StatesView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, orientation="horizontal", corner_radius=0)

    def create_state(self):
        state = view.StateView(self)
        state.pack(fill="y", expand=True, side="left", anchor="w", padx="5", pady="5")
        return state

    def delete_states(self):
        for child in self.winfo_children():
            child.destroy()

    def set_entry(self, entry_state):
        for child in self.winfo_children():
            if child is not entry_state:
                child.is_entry = True
                child.set_entry()
