import customtkinter as ctk
from PIL import Image

SYMBOL_WIDTH = 18
DIVIDER_WIDTH = 5
PADDING = 5
COMMA_WIDTH = 10
FONT_SIZE = 15


class TransitionView(ctk.CTkFrame):
    def __init__(self, parent, read: list[str], write: list[str], movement: list[str], new_state: str):
        super().__init__(parent, fg_color="transparent")
        self.width = 0

        current_label = ctk.CTkLabel(self)
        for symbol in read:
            if symbol == " ":
                image_square_light = Image.open("./resources/square_dark.png")
                image_square_dark = Image.open("./resources/square_dark.png")
                image_square = ctk.CTkImage(light_image=image_square_light, dark_image=image_square_dark,
                                            size=(SYMBOL_WIDTH, SYMBOL_WIDTH))

                current_label = ctk.CTkLabel(self, text="", image=image_square)
                current_label.pack(side="left")
            else:
                current_label = ctk.CTkLabel(self, width=SYMBOL_WIDTH, text=symbol, font=("", FONT_SIZE, "bold"))
                current_label.pack(side="left")

            current_label = ctk.CTkLabel(self, text="|", width=DIVIDER_WIDTH, font=("", FONT_SIZE, "bold"))
            current_label.pack(side="left")
            self.width += SYMBOL_WIDTH + DIVIDER_WIDTH
        current_label.pack_forget()
        self.width -= DIVIDER_WIDTH

        image_right_arrow_light = Image.open("./resources/arrow_right_light.png")
        image_right_arrow_dark = Image.open("./resources/arrow_right_dark.png")
        image_right_arrow = ctk.CTkImage(light_image=image_right_arrow_light, dark_image=image_right_arrow_dark,
                                         size=(SYMBOL_WIDTH, SYMBOL_WIDTH))

        arrow = ctk.CTkLabel(self, text="", image=image_right_arrow)
        arrow.pack(padx=PADDING, side="left")
        self.width += 2*PADDING + SYMBOL_WIDTH

        for symbol in write:
            if symbol == " ":
                image_square_light = Image.open("./resources/square_dark.png")
                image_square_dark = Image.open("./resources/square_dark.png")
                image_square = ctk.CTkImage(light_image=image_square_light, dark_image=image_square_dark,
                                            size=(SYMBOL_WIDTH, SYMBOL_WIDTH))

                current_label = ctk.CTkLabel(self, text="", image=image_square)
                current_label.pack(side="left")
            else:
                current_label = ctk.CTkLabel(self, width=SYMBOL_WIDTH, text=symbol, font=("", FONT_SIZE, "bold"))
                current_label.pack(side="left")

            current_label = ctk.CTkLabel(self, text="|", width=DIVIDER_WIDTH, font=("", FONT_SIZE, "bold"))
            current_label.pack(side="left")
            self.width += SYMBOL_WIDTH + DIVIDER_WIDTH
        current_label.pack_forget()
        self.width -= DIVIDER_WIDTH

        self.divider1 = ctk.CTkLabel(self, text=",", width=COMMA_WIDTH, font=("", FONT_SIZE, "bold"))
        self.divider1.pack(side="left")
        self.width += COMMA_WIDTH

        for symbol in movement:
            current_label = ctk.CTkLabel(self, width=SYMBOL_WIDTH, text=symbol, font=("", FONT_SIZE, "bold"))
            current_label.pack(side="left")

            current_label = ctk.CTkLabel(self, text="|", width=DIVIDER_WIDTH, font=("", FONT_SIZE, "bold"))
            current_label.pack(side="left")
            self.width += SYMBOL_WIDTH + DIVIDER_WIDTH
        current_label.pack_forget()
        self.width -= DIVIDER_WIDTH

        self.divider2 = ctk.CTkLabel(self, text=",", width=COMMA_WIDTH, font=("", FONT_SIZE, "bold"))
        self.divider2.pack(side="left")
        self.width += COMMA_WIDTH

        self.new_state = ctk.CTkLabel(self, text=new_state, font=("", FONT_SIZE, "bold"), anchor="w")
        self.new_state.pack(side="left")
        width_new_state = ctk.CTkFont("", FONT_SIZE, "bold").measure(new_state)
        self.width += width_new_state + PADDING

