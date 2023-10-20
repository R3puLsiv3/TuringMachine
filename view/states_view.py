import customtkinter as ctk


class StatesView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, orientation="horizontal", corner_radius=0)
        self.scrollable_frame.pack(fill="both", expand=True)

        name = "0"
        self.add_state(name)

    def add_state(self, name: str):
        example_state1 = ctk.CTkTextbox(self.scrollable_frame).pack(fill="y", expand=True, side="right", padx="5", pady="5")
        example_state2 = ctk.CTkTextbox(self.scrollable_frame).pack(fill="y", expand=True, side="right", padx="5", pady="5")
        example_state3 = ctk.CTkTextbox(self.scrollable_frame).pack(fill="y", expand=True, side="right", padx="5", pady="5")

