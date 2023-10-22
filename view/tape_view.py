import customtkinter as ctk

count = 0
base = 0


class TapeView(ctk.CTkScrollableFrame):
    def __init__(self, parent, tape_input):
        super().__init__(parent, corner_radius=0, orientation="horizontal", height=120)

        for i in range(64):
            label = ctk.CTkLabel(self, height=50, width=50, text=" ", fg_color="white", font=("", 35, "bold"),
                                 text_color="black", corner_radius=0)
            label.grid(row=1, column=i, pady=4, padx=2)

        for i in range(len(tape_input)):
            label = ctk.CTkLabel(self, height=50, width=50, text=tape_input[i], fg_color="white", font=("", 35, "bold"),
                                 text_color="black", corner_radius=0)
            label.grid(row=1, column=i+64, pady=4, padx=2)

        for i in range(64):
            label = ctk.CTkLabel(self, height=50, width=50, text=" ", fg_color="white", font=("", 35, "bold"),
                                 text_color="black", corner_radius=0)
            label.grid(row=1, column=i+64+len(tape_input), pady=4, padx=2)

        head = ctk.CTkLabel(self, height=50, width=50, text="2", fg_color="white", font=("", 35, "bold"),
                            text_color="black", corner_radius=0)
        head.grid(row=0, column=64, pady=(10, 0))

        # Adjust tape to show beginning of input with head approximately in the middle
        base = head.cget("width") + 4
        offset = (self.winfo_screenwidth() // base) // 2
        self._parent_canvas.xview(ctk.SCROLL, (100 - offset) * base + (base // 2), ctk.UNITS)

        def do_after(pos, direction):
            global count, base
            if count < 10:
                self._parent_canvas.xview(ctk.SCROLL, direction * 5, ctk.UNITS)
                count += 1
                self.after(10, do_after, pos, direction)
            else:
                count = 0
                head.grid(row=0, column=pos + direction)
                self._parent_canvas.xview(ctk.SCROLL, direction * 4, ctk.UNITS)
