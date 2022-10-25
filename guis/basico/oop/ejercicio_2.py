"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Tk


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
        self.btn["command"] = self.calculate

    def setup_ui(self) -> None:
        self.x = Entry(self)
        self.y = Entry(self)
        self.result = Label(self)
        self.btn = Button(self, text="Calculate")
        self.x.pack(padx=5, pady=5)
        self.y.pack(padx=5, pady=5)
        self.btn.pack(padx=5, pady=5)
        self.result.pack(padx=5, pady=5)

    def calculate(self) -> None:
        try:
            result = float(self.x.get()) + float(self.y.get())
        except ValueError:
            self.result.config(text="Incorrect values")
            self._cleanup()
        else:
            self.result.config(text=result)

    def _cleanup(self):
        self.x.delete(0, "end")
        self.y.delete(0, "end")


if __name__ == "__main__":
    app = App()
    app.mainloop()
