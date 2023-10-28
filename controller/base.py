import model
import view
import controller
import sys


class Controller:
    def __init__(self, _model: model.Model, _view: view.View):
        self.view = _view
        self.model = _model

        self.states_controller = controller.StatesController(_model, _view)
        self.tapes_controller = controller.TapesController(_model, _view)
        self.options_controller = controller.OptionsController(_model, _view)
        self.info_controller = controller.InfoController(_model, _view)

        self.options_controller.set_controllers(self.states_controller, self.tapes_controller, self.info_controller)
        self.states_controller.set_controllers(self.tapes_controller, self.options_controller, self.info_controller)

    def start(self):
        self.setup_window(self.model.settings)
        self.view.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.view.start_mainloop()

    def setup_window(self, settings: dict):
        if settings["full-screen"]:
            if "linux" in sys.platform:
                self.view.root.after(0, lambda: self.view.root.attributes("zoomed", True))
            else:
                self.view.root.after(0, lambda: self.view.root.state("zoomed"))
        else:
            width = settings["width"]
            height = settings["height"]
            pos_x = settings["pos_x"]
            pos_y = settings["pos_y"]
            self.view.root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")

    def on_closing(self):
        # TODO: popup asking user to save turing machine

        self.model.settings["width"] = self.view.root.winfo_width()
        self.model.settings["height"] = self.view.root.winfo_height()
        self.model.settings["pos_x"] = self.view.root.winfo_x()
        self.model.settings["pos_y"] = self.view.root.winfo_y()
        self.model.settings["full-screen"] = 1 if self.view.root.state() == "zoomed" else 0
        model.update_settings(self.model.settings)

        self.view.root.quit()
