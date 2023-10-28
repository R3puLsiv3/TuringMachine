import customtkinter as ctk
import view


class TapesView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, orientation="vertical", corner_radius=0)
        self.tapes: list[view.TapeView] = []

    def add_tape(self, tape_input: str):
        tape = view.TapeView(self, tape_input)
        tape.pack(fill="x", pady=(20, 0))
        self.tapes.append(tape)

    def delete_tape(self):
        if self.tapes:
            self.tapes[len(self.tapes)-1].destroy()
