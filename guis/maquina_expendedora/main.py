"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: do it later...
"""
from tkinter import Button, Canvas, Frame, Text, Tk

PRODUCTOS = {f"A{i}": 10 for i in range(1, 21)}
GRID = (
    ("1", "2", "3"),
    ("4", "5", "6"),
    ("7", "8", "9"),
    ("\u232b", "0", "\u21B5"),
)


class Container(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self["bg"] = "white"
        self.setup_ui()

    def setup_ui(self) -> None:
        k = 1
        for i in range(5):
            for j in range(4):
                Button(
                    self, text=f"A{i+k}", height=4, width=8
                ).grid(row=i, column=j+1, padx=5, pady=10)
                k += 1
            k -= 1


class Control(Frame):

    def __init__(self, master):
        super().__init__(master)
        self["bg"] = "gray25"
        self.setup_ui()

    def setup_ui(self):
        self.lcd = Text(self, height=2, width=16, bg="steel blue", fg="white")
        self.lcd.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
        self.lcd.insert("end", "Ingresar código:\n")
        self.lcd.insert("end", "_")
        self.lcd.config(state="disabled")
        for i, row in enumerate(GRID):
            for j, col in enumerate(row):
                Button(
                    self, text=col, height=1, width=4, bg="gray40", fg="white"
                ).grid(row=i+1, column=j, padx=2, pady=2)
        self.frm = Frame(self, height=130, width=130, bg="gray15")
        self.frm.grid(row=6, columnspan=3, padx=5, pady=5)
        self.frm.grid_propagate(False)
        self.frm.grid_rowconfigure(0, weight=1)
        self.frm.grid_columnconfigure(0, weight=1)
        Button(
            self.frm, height=4, width=8,
            bg="gray25", activebackground="gray15",
        ).grid(row=0, column=0, padx=5, pady=10)


class VendingMachine(Tk):

    def __init__(self):
        super().__init__()
        self.title("Vending Machine - Ayuda en Python")
        self.geometry("540x620")
        self["bg"] = "gray10"
        self.setup_ui()

    def setup_ui(self) -> None:
        self.left_frm = Frame(self, width=300, height=480, bg="white")
        self.left_frm.grid(row=0, column=0, sticky="new", padx=10, pady=10)
        self.right_frm = Frame(self, width=200, height=600, bg="gray25")
        self.right_frm.grid(
            row=0, rowspan=2, column=1, sticky="ew", padx=5, pady=10
        )
        self.container = Container(self.left_frm)
        self.container.grid(row=0, column=0, sticky="new")
        self.canvas = Canvas(
            self, width=300, height=125, bg="gray25", highlightthickness=0,
        )
        self.canvas.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        self.canvas.create_rectangle(50, 40, 260, 90, fill="gray50")
        self.right_frm.grid_propagate(False)
        self.right_frm.grid_rowconfigure(0, weight=1)
        self.right_frm.grid_columnconfigure(0, weight=1)
        self.control = Control(self.right_frm)
        self.control.grid(padx=10, pady=10)


if __name__ == "__main__":
    app = VendingMachine()
    app.mainloop()
