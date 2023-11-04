import customtkinter as ctk
from PIL import Image


class TransitionView(ctk.CTkFrame):
    def __init__(self, parent, tape: str, read: str, write: str, movement: str, new_state: str):
        super().__init__(parent, fg_color="transparent")

        tape = tape + ":"
        read = read
        right = write + ", " + movement + ", " + new_state

        image_right_arrow_light = Image.open("./resources/arrow_right_light.png")
        image_right_arrow_dark = Image.open("./resources/arrow_right_dark.png")
        image_right_arrow = ctk.CTkImage(light_image=image_right_arrow_light, dark_image=image_right_arrow_dark,
                                         size=(20, 20))

        self.tape_label = ctk.CTkLabel(self, text=tape, font=("", 15, "bold"), text_color="gray")
        self.tape_label.pack(padx=10, side="left")

        self.read_label = ctk.CTkLabel(self, text=read, font=("", 15, "bold"))
        self.read_label.pack(side="left")

        arrow = ctk.CTkLabel(self, text="", image=image_right_arrow, height=20)
        arrow.pack(padx=10, side="left")

        self.right = ctk.CTkLabel(self, text=right, font=("", 15, "bold"), height=20, anchor="w")
        self.right.pack(padx=(0, 10), side="left")
