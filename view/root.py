import view
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_TITLE = "Turing Machine"


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.iconbitmap("./resources/icon_gamma.ico")

        self.main_view = view.MainView(self)
        self.main_view.pack(fill="both", expand=True)
