from tkinter import messagebox
from model.transition import parse_transitions, reverse_parse_transitions


class StateController:
    def __init__(self, parent, model, view):
        self.parent = parent
        self.model = model
        self.frame = view
        self.name = None

        self.bind()

    def bind(self):
        self.frame.button_save.configure(command=self.save_frame)
        self.frame.button_delete.configure(command=self.delete_frame)
        self.frame.button_edit.configure(command=self.edit_frame)

    def save_frame(self):
        name = self.frame.entry_name.get()
        transitions = self.frame.textbox_transitions.get("0.0", "end")

        try:
            self.name = self.model.turing_machine.check_name(name)
        except ValueError:
            messagebox.showinfo(title="Duplicate or empty name",
                                message="State name can't be empty and must be unique.")
            return

        try:
            parsed_transitions = parse_transitions(transitions)
            self.model.turing_machine.add_state(self.name, self.frame.is_halting, parsed_transitions)
            if self.frame.is_entry:
                self.model.turing_machine.entry_state = self.name
        except ValueError:
            message = "Transitions must be of the form\n" \
                      "[R]->[W],[M],[S]\n" \
                      "R = Symbol(s) being read divided by | for multiple tapes\n" \
                      "W = Symbol(s) being written divided by | for multiple tapes\n" \
                      "M = Head movement (L=Left, N=None, R=Right)\n" \
                      "S = New state (Name)\n" \
                      "For R and W: blank = blank symbol, div = |, comma = ,"

            messagebox.showinfo(title="Wrong Transition", message=message)
            return

        transitions_dict = self.model.turing_machine.states[self.name].to_dict()
        self.frame.show_state(self.name, transitions_dict)

    def delete_frame(self):
        if self.name in self.model.turing_machine.states.keys():
            self.model.turing_machine.delete_state(self.name)

        self.frame.destroy()
        self.parent.delete_state_controller(self)

    def edit_frame(self):
        self.parent.tapes_controller.delete_tape_controllers()
        transitions_str = reverse_parse_transitions(self.model.turing_machine.states[self.name].transitions)
        self.model.turing_machine.delete_state(self.name)

        self.frame.edit_state(self.name, transitions_str)


