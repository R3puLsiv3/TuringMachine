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

        # TODO: Load last turing machine used and tapes

        _model = {"settings": model.Settings().settings}

        self.setup_window(_model["settings"])

        _view = view.MainView(self)

        _controller = controller.TuringMachineController(_model, _view)

        _view.set_controller(_controller)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_window(self, settings: dict):
        if settings["full-screen"]:
            self.state("zoomed")
        else:
            width = settings["width"]
            height = settings["height"]
            pos_x = settings["pos_x"]
            pos_y = settings["pos_y"]
            self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def on_closing(self):
        # TODO: popup asking user to save turing machine

        settings = model.Settings().settings
        settings["width"] = self.winfo_width()
        settings["height"] = self.winfo_height()
        settings["pos_x"] = self.winfo_x()
        settings["pos_y"] = self.winfo_y()
        settings["full-screen"] = 1 if self.state() == "zoomed" else 0
        model.update_settings(settings)

        self.quit()
