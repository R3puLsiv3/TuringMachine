from tkinter import ttk


class StatesView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        self["padding"] = 5
        self["width"] = parent_width - 20
        self["height"] = parent_height - 20
        self["borderwidth"] = 5
        self["relief"] = "solid"

        self.grid(column=0, row=0)
