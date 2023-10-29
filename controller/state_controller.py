
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
        is_halting_state = self.frame.checkbox_halting_state.get()
        transitions = self.frame.textbox_transitions.get("0.0", "end")
        self.model.turing_machine.add_state(name, is_halting_state, transitions)

        transitions_list = self.model.turing_machine.states[name].list_transitions()
        self.frame.show_state(name, is_halting_state, transitions_list)

    def delete_frame(self):
        self.frame.destroy()
