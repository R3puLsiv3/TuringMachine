import tkinter as tk
from view import MainView


class App(tk.Tk):
    def __init__(self, title):
        super().__init__()

        self.title(title)

        # <a target="_blank" href="https://icons8.com/icon/50uytEmrQnGV/gamma">Gamma</a>
        # icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.iconbitmap("./resources/icon_gamma.ico")

        view = MainView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

