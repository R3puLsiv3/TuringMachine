import customtkinter as ctk


class OptionsView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, height=50)

        self.button_add_state = ctk.CTkButton(self, width=50, text="Add state")
        self.button_add_state.pack(side="left")
