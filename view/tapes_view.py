import customtkinter as ctk
import view


class TapesView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=0)

    def add_tape(self, tape_input: str):
        tape = view.TapeView(self, tape_input)
        tape.pack(fill="x", pady=(20, 0))
