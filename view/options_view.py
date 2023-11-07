import customtkinter as ctk


class OptionsView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, height=50)

        self.button_add_state = ctk.CTkButton(self, width=50, text="Add state")
        self.button_add_state.pack(side="left")

        self.button_add_tape = ctk.CTkButton(self, width=50, text="Add tape")
        self.button_add_tape.pack(side="left")

        self.button_delete_tape = ctk.CTkButton(self, width=50, text="Delete tape")
        self.button_delete_tape.pack(side="left")
