import customtkinter as ctk
from PIL import Image


class TransitionView(ctk.CTkFrame):
    def __init__(self, parent, transition):
        super().__init__(parent, fg_color="transparent")

        split_transition = transition.split()
        print(split_transition[0])
        print(split_transition[1])
        left = split_transition[0]
        right = split_transition[1]

        image_right_arrow_light = Image.open("./resources/arrow_right_light.png")
        image_right_arrow_dark = Image.open("./resources/arrow_right_dark.png")
        image_right_arrow = ctk.CTkImage(light_image=image_right_arrow_light, dark_image=image_right_arrow_dark,
                                         size=(20, 20))

        left = ctk.CTkLabel(self, text=left, font=("", 13, "bold"), width=20, height=20)
        left.pack(padx=10, side="left")

        middle = ctk.CTkLabel(self, text="", image=image_right_arrow, height=20)
        middle.pack(padx=(0, 15), side="left")

        right = ctk.CTkLabel(self, text=right, font=("", 15, "bold"), height=20)
        right.pack(padx=(0, 10), side="left")
