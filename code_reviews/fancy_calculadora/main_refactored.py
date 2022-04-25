"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: Needs more implementation
"""
from tkinter import Frame, Label, Tk, Button, Entry, PhotoImage
from settings import *


class Calculator(Frame):
    
    def __init__(self, master=None):
        super().__init__(master)
        self.btns = []
        self.config()
        self.setup_ui()

    def setup_ui(self):
        history = Label(self, **HISTORY_SETTINGS)
        history.grid(ipadx=26, ipady=6, columnspan=5)
        screen = Entry(self, **SCREEN_SETTINGS)
        screen.grid(ipadx=26, ipady=12, columnspan=5)
        for row in GRID:
            for btn in row:
                btn_ = Button(self, text=btn, **BUTTONS_SETTINGS)
                btn_.grid(
                    row=GRID.index(row)+2,
                    column=row.index(btn),
                    ipadx=10,
                    ipady=10,
                )
                self.btns.append(btn_)

    def pressed(self, btn):
        ...

    def calculate(self):
        ...


class App(Frame):

    def __init__(self) -> None:
        self.root = Tk()
        self.root.title(f"AeP Calculadora {VERSION}")
        self.root.iconphoto(True, PhotoImage(file="calc.png"))
        self.calculator = Calculator(self.root)
        self.calculator.pack(
            expand=True, fill="none", side="top", anchor="center"
        )

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
