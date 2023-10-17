import tkinter as tk
import view
import model
import controller


class App(tk.Tk):
    def __init__(self, title):
        super().__init__()

        self.title(title)

        # Credit: <a target="_blank" href="https://icons8.com/icon/50uytEmrQnGV/gamma">Gamma</a>
        # icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.iconbitmap("./resources/icon_gamma.ico")

        # TODO: Load last known state of window settings and last turing machine used and set up view

        # self.state('zoomed')

        _model = {"settings": model.Settings()}
        _view = view.MainView(self)
        _controller = controller.TuringMachineController(_model, _view)

        _view.set_controller(_controller)

