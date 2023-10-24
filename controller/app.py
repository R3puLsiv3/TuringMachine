import customtkinter as ctk
import sys
import view
import model
import controller

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
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
        _view.pack(fill="both", expand=True)

        _controller = controller.TuringMachineController(_model, _view)

        _view.set_controller(_controller)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_window(self, settings: dict):
        if settings["full-screen"]:
            if "linux" in sys.platform:
                self.after(0, lambda: self.attributes("zoomed", True))
            else:
                self.after(0, lambda: self.state("zoomed"))
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
