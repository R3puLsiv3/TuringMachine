from tkinter import messagebox
from model.transition import parse_transitions


class StateController:
    def __init__(self, model, view):
        self.model = model
        self.frame = view

        self.bind()

    def bind(self):
        self.frame.button_save.configure(command=self.save_frame)
        self.frame.button_delete.configure(command=self.delete_frame)

    def save_frame(self):
        name = self.frame.entry_name.get()
        is_entry_state = self.frame.is_entry
        is_halting_state = self.frame.is_halting
        transitions = self.frame.textbox_transitions.get("0.0", "end")

        try:
            self.model.turing_machine.check_name(name)
        except ValueError:
            messagebox.showinfo(title="Duplicate or empty name",
                                message="State name can't be empty and must be unique.")
            return

        try:
            parsed_transitions = parse_transitions(transitions)
            self.model.turing_machine.add_state(name, is_halting_state, parsed_transitions)
        except ValueError:
            message = "Transitions must be of the form\n" \
                      "[T]:[R]->[W],[M],[N]\n" \
                      "T = Tape number (Empty and without colon afterwards defaults to tape 1)\n" \
                      "R = Symbol being read (Empty or space for blank symbol)\n" \
                      "W = Symbol being written (Empty or space for blank symbol)\n" \
                      "M = Head movement (L=Left, N=None, R=Right)\n" \
                      "N = New state (Name)"

            messagebox.showinfo(title="Wrong Transition", message=message)
            return

        transitions_dict = self.model.turing_machine.states[name].to_dict()
        self.frame.show_state(name, is_halting_state, is_entry_state, transitions_dict)

    def delete_frame(self):
        self.frame.destroy()
