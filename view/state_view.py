import customtkinter as ctk
from PIL import Image

import view


class StateView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.transitions = []

        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.pack(fill="x", padx=5, pady=(5, 0))

        self.label_name = ctk.CTkLabel(self.frame_top, width=0, height=18, font=("", 18, "bold"), anchor="w")

        self.entry_name = ctk.CTkEntry(self.frame_top, placeholder_text="Name", width=150, height=18)
        self.entry_name.pack(fill="both", expand=True, pady=2, side="left")

        image_entry_faded_dark = Image.open("./resources/entry_faded_dark.png")
        image_entry_faded = ctk.CTkImage(light_image=image_entry_faded_dark, dark_image=image_entry_faded_dark,
                                         size=(20, 20))

        self.button_entry = ctk.CTkButton(self.frame_top, width=20, image=image_entry_faded, text="",
                                          command=self.set_entry, fg_color="transparent", hover=False)
        self.button_entry.pack(padx=(5, 0), pady=2, side="left")
        self.is_entry = False

        image_halting_faded_dark = Image.open("./resources/halting_faded_dark.png")
        image_halting_faded = ctk.CTkImage(light_image=image_halting_faded_dark, dark_image=image_halting_faded_dark,
                                           size=(20, 20))

        self.button_halting = ctk.CTkButton(self.frame_top, width=20, image=image_halting_faded, text="",
                                            command=self.set_halting, fg_color="transparent", hover=False)
        self.button_halting.pack(padx=(0, 5), pady=2, side="left")
        self.is_halting = False

        image_save_light = Image.open("./resources/save_light.png")
        image_save_dark = Image.open("./resources/save_dark.png")
        image_save = ctk.CTkImage(light_image=image_save_light, dark_image=image_save_dark, size=(20, 20))

        self.button_save = ctk.CTkButton(self.frame_top, width=20, image=image_save, text="")
        self.button_save.pack(padx=(0, 2), pady=2, side="left")

        image_close_light = Image.open("./resources/close_light.png")
        image_close_dark = Image.open("./resources/close_dark.png")
        image_close = ctk.CTkImage(light_image=image_close_light, dark_image=image_close_dark, size=(20, 20))

        self.button_delete = ctk.CTkButton(self.frame_top, width=20, image=image_close, text="", anchor="e")
        self.button_delete.pack(padx=(0, 2), pady=2, side="left")

        image_edit_light = Image.open("./resources/edit_light.png")
        image_edit_dark = Image.open("./resources/edit_dark.png")
        image_edit = ctk.CTkImage(light_image=image_edit_light, dark_image=image_edit_dark, size=(20, 20))

        self.button_edit = ctk.CTkButton(self.frame_top, width=20, image=image_edit, text="")

        self.textbox_transitions = ctk.CTkTextbox(self)
        self.textbox_transitions.pack(fill="both", expand=True, padx=5, pady=5)

        # Used to manually adjust the size of scrollable frame, since it doesn't expand as a usual frame.
        self.frame_bottom_width = 0
        self.frame_bottom = ctk.CTkScrollableFrame(self, orientation="vertical", width=self.frame_bottom_width)

    def set_entry(self):
        if self.is_entry:
            image_entry_faded_dark = Image.open("./resources/entry_faded_dark.png")
            image_entry_faded = ctk.CTkImage(light_image=image_entry_faded_dark, dark_image=image_entry_faded_dark,
                                             size=(20, 20))
            self.button_entry.configure(image=image_entry_faded)
            self.is_entry = False
        else:
            image_entry_dark = Image.open("./resources/entry_dark.png")
            image_entry = ctk.CTkImage(light_image=image_entry_dark, dark_image=image_entry_dark, size=(20, 20))
            self.button_entry.configure(image=image_entry)
            self.is_entry = True

            self.parent.set_entry(self)

    def set_halting(self):
        if self.is_halting:
            image_halting_faded_dark = Image.open("./resources/halting_faded_dark.png")
            image_halting_faded = ctk.CTkImage(light_image=image_halting_faded_dark,
                                               dark_image=image_halting_faded_dark, size=(20, 20))
            self.button_halting.configure(image=image_halting_faded)
            self.is_halting = False
        else:
            image_halting_dark = Image.open("./resources/halting_dark.png")
            image_halting = ctk.CTkImage(light_image=image_halting_dark, dark_image=image_halting_dark, size=(20, 20))
            self.button_halting.configure(image=image_halting)
            self.is_halting = True

    def show_transition(self, read: list[str], write: list[str], movement: str, new_state: str):
        transition_view = view.TransitionView(self.frame_bottom, read, write,
                                              movement, new_state)
        transition_view.pack(anchor="w", fill="x", expand=True)
        self.transitions.append(transition_view)

        if transition_view.width > self.frame_bottom_width:
            self.frame_bottom_width = transition_view.width
            self.frame_bottom.configure(width=self.frame_bottom_width)

    def show_state(self, name: str, transitions: list[dict[str]]):
        self.label_name.configure(text=name)
        self.entry_name.pack_forget()
        self.button_entry.pack_forget()
        self.button_halting.pack_forget()
        self.button_save.pack_forget()
        self.button_delete.pack_forget()
        self.label_name.pack(fill="both", expand=True, padx=(20, 10), pady=2, side="left")
        self.button_delete.pack(padx=(0, 2), pady=2, side="right")
        self.button_edit.pack(padx=(0, 2), pady=2, side="right")

        self.textbox_transitions.pack_forget()
        for child in self.frame_bottom.winfo_children():
            child.destroy()
        self.frame_bottom.pack(fill="both", expand=True, padx=5, pady=5)

        for transition in transitions:
            self.show_transition(transition["read"], transition["write"], transition["movement"],
                                 transition["new_state"])

        if self.is_halting:
            self.configure(border_color="black", border_width=2)

    def edit_state(self, name: str, transitions: str):
        self.entry_name.delete(0, ctk.END)
        self.entry_name.insert(0, name)
        self.label_name.pack_forget()
        self.button_edit.pack_forget()
        self.button_delete.pack_forget()
        self.entry_name.pack(fill="both", expand=True, pady=2, side="left")
        self.button_entry.pack(padx=(5, 0), pady=2, side="left")
        self.button_halting.pack(padx=(0, 5), pady=2, side="left")
        self.button_save.pack(padx=(0, 2), pady=2, side="left")
        self.button_delete.pack(padx=(0, 2), pady=2, side="left")

        self.textbox_transitions = ctk.CTkTextbox(self)
        self.textbox_transitions.insert("0.0", transitions)
        self.frame_bottom.pack_forget()
        self.textbox_transitions.pack(fill="both", expand=True, padx=5, pady=5)
