import customtkinter as ctk

class StateView(ctk.CTkTextbox):
    def __init__(self, parent, name: str):
        super().__init__(parent)
        self.name = name
