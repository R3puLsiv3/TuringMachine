import tkinter as tk
import view
import model


class App(tk.Tk):
    def __init__(self, title):
        super().__init__()

        self.title(title)

        # Credit: <a target="_blank" href="https://icons8.com/icon/50uytEmrQnGV/gamma">Gamma</a>
        # icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        self.iconbitmap("./resources/icon_gamma.ico")

        # TODO: Load last known state of window settings and last turing machine used and hand to (main) view

        # self.state('zoomed')

        tm = model.TuringMachine()
        tm.states[0] = {"1": ["7", "L", 2]}
        tm.states.append({"0": ["a", "L", 1]})
        tm.states.append({"2": ["4", "R", 0]})
        tm.states.append({"1": ["2", "L", 2]})
        print(tm.get_tape_alphabet())
        print(tm.get_input_alphabet())

        view_ = view.MainView(self)
