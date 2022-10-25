"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Tk


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
        self.button["command"] = self.show

    def setup_ui(self) -> None:
        self.entry = Entry(self)
        self.label = Label(self)
        self.button = Button(self, text="Press me")
        self.entry.pack(padx=5, pady=5)
        self.button.pack(padx=5, pady=5)
        self.label.pack(padx=5, pady=5)

    def show(self) -> None:
        txt = self.entry.get()
        self.label.config(text=f"Hello {txt}")


if __name__ == "__main__":
    app = App()
    app.mainloop()
