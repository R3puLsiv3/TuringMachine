import customtkinter as ctk
from PIL import Image

import view


class StateView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.frame_top = ctk.CTkFrame(self)
        self.frame_top.pack(fill="x", padx=5, pady=(5, 0))

        self.label_name = ctk.CTkLabel(self.frame_top)

        self.entry_name = ctk.CTkEntry(self.frame_top, placeholder_text="Name", width=150, height=18)
        self.entry_name.pack(fill="both", expand=True, padx=(0, 10), pady=2, side="left")

        self.checkbox_halting_state = ctk.CTkCheckBox(self.frame_top, text="Halt", width=20, font=("", 14, "bold"))
        self.checkbox_halting_state.pack(padx=(0, 10), pady=2, side="left")

        image_save_light = Image.open("./resources/save_light.png")
        image_save_dark = Image.open("./resources/save_dark.png")
        image_save = ctk.CTkImage(light_image=image_save_light, dark_image=image_save_dark, size=(20, 20))

        self.button_save = ctk.CTkButton(self.frame_top, width=20, image=image_save, text="",
                                         command=self.on_button_save_click)
        self.button_save.pack(padx=(0, 2), pady=2, side="left")

        image_close_light = Image.open("./resources/close_light.png")
        image_close_dark = Image.open("./resources/close_dark.png")
        image_close = ctk.CTkImage(light_image=image_close_light, dark_image=image_close_dark, size=(20, 20))

        self.button_delete = ctk.CTkButton(self.frame_top, width=20, image=image_close, text="", anchor="e",
                                           command=self.on_button_delete_click)
        self.button_delete.pack(padx=(0, 2), pady=2, side="right")

        image_edit_light = Image.open("./resources/edit_light.png")
        image_edit_dark = Image.open("./resources/edit_dark.png")
        image_edit = ctk.CTkImage(light_image=image_edit_light, dark_image=image_edit_dark, size=(20, 20))

        self.button_edit = ctk.CTkButton(self.frame_top, width=20, image=image_edit, text="",
                                         command=self.on_button_edit_click)

        self.textbox_bottom = ctk.CTkTextbox(self)
        self.textbox_bottom.pack(fill="both", expand=True, padx=5, pady=5)

        self.frame_bottom = ctk.CTkScrollableFrame(self, orientation="vertical", width=100)

        self.add_transition("M", "b, L, 2")
        self.add_transition("b", "a, R, 1")
        self.add_transition(" ", "b, N, 1")

        name_show = ctk.CTkEntry(self, placeholder_text="Name")

    def add_transition(self, right: str, left: str):
        transition = view.TransitionView(self.frame_bottom, right, left)
        transition.pack(anchor="w", fill="x", expand=True)

    def on_button_delete_click(self):
        self.destroy()

    def on_button_edit_click(self):
        entry_name = ctk.CTkEntry(self, text=self.label_name.cget("text"))

    def on_button_save_click(self):
        self.label_name.configure(width=60, height=18, font=("", 18, "bold"))
        self.entry_name.pack_forget()
        self.button_save.pack_forget()
        self.checkbox_halting_state.pack_forget()
        self.label_name.configure(text=self.entry_name.get())
        self.label_name.pack(fill="both", expand=True, padx=10, pady=2, side="left")
        self.button_edit.pack(padx=(0, 2), pady=2, side="left")

        self.textbox_bottom.pack_forget()
        # TODO: Implement parser and create transition views
        self.frame_bottom.pack(fill="both", expand=True, padx=5, pady=5)
