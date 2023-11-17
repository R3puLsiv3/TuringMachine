import customtkinter as ctk
import view


class TapesView(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, orientation="vertical", corner_radius=0)

    def create_tape(self, name):
        prompt_tape_input = ctk.CTkInputDialog(title="Add tape", text="Tape " + name + " input:")
        tape_input = prompt_tape_input.get_input()

        if tape_input is None:
            return

        tape_input = tape_input.replace(" ", "")
        tape = view.TapeView(self, tape_input)
        tape.pack(fill="x", pady=(20, 0))
        return tape

    def delete_tapes(self):
        for child in self.winfo_children():
            child.destroy()
