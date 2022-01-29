"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Frame, Tk

TITLE, DIMENSIONS = "Calculadora", "300x340"
GRID = (("AC", "+/-", "%", "/"),
        ( "7",   "8", "9", "*"),
        ( "4",   "5", "6", "-"),
        ( "1",   "2", "3", "+"),
        ( "π",   "0", ".", "="))


class App(Frame):

    def __init__(self):
        self.root = Tk()
        self.config()
        self._widgets()

    def _widgets(self):
        self.lcd = Entry(
            self.root, font=("Arial", 20, "bold"), width=20, justify="right")
        self.lcd.grid(row=0, column=0, columnspan=4)
        for row in GRID:
            for btn in row:
                Button(self.root, width=6, height=2, font=("Arial", 14),
                    text=btn, command=lambda btn=btn: self._calculate(btn)
                ).grid(row=GRID.index(row)+1, column=row.index(btn))

    def _calculate(self, btn):
        value = self.lcd.get()
        if btn == "AC":
            self._output("")
        elif btn == "π":
            self._output(value + "3.1416")
        elif btn == "=":
            try:
                self._output(eval(value))
            except:
                self._output("Error")
        elif btn == "+/-":
            try:
                self._output(-float(value))
            except:
                self._output("Error")
        else:
            self._output(value + btn)

    def _output(self, value):
        self.lcd.delete(0, "end")
        self.lcd.insert("end", str(value))

    def config(self):
        self.root.title(TITLE)
        self.root.geometry(DIMENSIONS)
        self.root.resizable(False, False)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()