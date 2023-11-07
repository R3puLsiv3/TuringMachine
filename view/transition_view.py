import customtkinter as ctk
from PIL import Image


class TransitionView(ctk.CTkFrame):
    def __init__(self, parent, tape: str, read: str, write: str, movement: str, new_state: str):
        super().__init__(parent, fg_color="transparent")

        tape = tape + ":"

        image_right_arrow_light = Image.open("./resources/arrow_right_light.png")
        image_right_arrow_dark = Image.open("./resources/arrow_right_dark.png")
        image_right_arrow = ctk.CTkImage(light_image=image_right_arrow_light, dark_image=image_right_arrow_dark,
                                         size=(20, 20))

        self.tape_label = ctk.CTkLabel(self, text=tape, font=("", 15, "bold"), text_color="gray")
        self.tape_label.pack(padx=10, side="left")

        if read == " ":
            image_square_light = Image.open("./resources/square_dark.png")
            image_square_dark = Image.open("./resources/square_dark.png")
            image_square = ctk.CTkImage(light_image=image_square_light, dark_image=image_square_dark, size=(18, 18))

            self.read_label = ctk.CTkLabel(self, text="", image=image_square)
            self.read_label.pack(side="left")
        else:
            self.read_label = ctk.CTkLabel(self, width=18, text=read, font=("", 15, "bold"))
            self.read_label.pack(side="left")

        arrow = ctk.CTkLabel(self, text="", image=image_right_arrow, height=20)
        arrow.pack(padx=10, side="left")

        if write == " ":
            image_square_light = Image.open("./resources/square_dark.png")
            image_square_dark = Image.open("./resources/square_dark.png")
            image_square = ctk.CTkImage(light_image=image_square_light, dark_image=image_square_dark, size=(18, 18))

            self.write_label = ctk.CTkLabel(self, text="", image=image_square)
            self.write_label.pack(side="left")
        else:
            self.read_label = ctk.CTkLabel(self, width=18, text=write, font=("", 15, "bold"))
            self.read_label.pack(side="left")

        self.divider1 = ctk.CTkLabel(self, text="|", width=18, font=("", 15, "bold"), height=20)
        self.divider1.pack(side="left")

        self.movement = ctk.CTkLabel(self, text=movement, width=18, font=("", 15, "bold"), height=20)
        self.movement.pack(side="left")

        self.divider2 = ctk.CTkLabel(self, text="|", width=18, font=("", 15, "bold"), height=20)
        self.divider2.pack(side="left")

        self.new_state = ctk.CTkLabel(self, text=new_state, font=("", 15, "bold"), height=20, anchor="w")
        self.new_state.pack(side="left")
