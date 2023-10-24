import customtkinter as ctk
from PIL import Image

PADDING = 64


class TapeView(ctk.CTkScrollableFrame):
    def __init__(self, parent, tape_input):
        super().__init__(parent, corner_radius=0, orientation="horizontal", height=120)

        self.count = 0
        self.base = 0

        for i in range(PADDING):
            label = ctk.CTkLabel(self, height=50, width=50, text=" ", fg_color="white", font=("", 35, "bold"),
                                 text_color="black", corner_radius=0)
            label.grid(row=1, column=i, pady=4, padx=2)

        for i in range(len(tape_input)):
            label = ctk.CTkLabel(self, height=50, width=50, text=tape_input[i], fg_color="white", font=("", 35, "bold"),
                                 text_color="black", corner_radius=0)
            label.grid(row=1, column=i+PADDING, pady=4, padx=2)

        for i in range(PADDING):
            label = ctk.CTkLabel(self, height=50, width=50, text=" ", fg_color="white", font=("", 35, "bold"),
                                 text_color="black", corner_radius=0)
            label.grid(row=1, column=i+PADDING+len(tape_input), pady=4, padx=2)

        # Credit: <a target="_blank" href="https://icons8.com/icon/6kvmvAorttE3/down">Down</a>
        # icon by <a target="_blank" href = "https://icons8.com">Icons8</a>
        image = Image.open("./resources/head.png")
        image = ctk.CTkImage(light_image=image, dark_image=image, size=(50, 50))
        head = ctk.CTkLabel(self, height=50, width=50, image=image, text="")
        head.grid(row=0, column=PADDING, pady=(10, 0))
        self.pos = PADDING

        # Adjust tape to show beginning of input with head approximately in the middle
        base = head.cget("width") + 4
        offset = (self.winfo_screenwidth() // base) // 2
        self._parent_canvas.xview(ctk.SCROLL, (PADDING - offset) * base + (base // 2), ctk.UNITS)

        def do_after(direction):
            if self.count < 10:
                self._parent_canvas.xview(ctk.SCROLL, direction * 5, ctk.UNITS)
                self.count += 1
                self.after(10, do_after, direction)
            else:
                self.count = 0
                head.grid(row=0, column=self.pos + direction)
                self._parent_canvas.xview(ctk.SCROLL, direction * 4, ctk.UNITS)
