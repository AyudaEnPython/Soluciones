"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, messagebox, Tk


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.entries = []
        self.labels = []
        self.setup_ui()
        self.btn["command"] = self.calculate

    def setup_ui(self) -> None:
        for _ in range(3):
            self.entries.append(Entry(self))
            self.labels.append(Label(self))
        self.btn = Button(self, text="Order")
        for entry in self.entries:
            entry.pack(padx=5, pady=5)
        self.btn.pack(padx=5, pady=5)
        for label in self.labels:
            label.pack(padx=5, pady=5)

    def calculate(self) -> None:
        try:
            xs = [float(x.get()) for x in self.entries]
        except ValueError:
            messagebox.showerror(message="Incorrect values")
            self._cleanup()
        else:
            xs = sorted(xs, reverse=True)
            for label, number in zip(self.labels, xs):
                label.config(text=number)

    def _cleanup(self) -> None:
        for entry in self.entries:
            entry.delete(0, "end")


if __name__ == "__main__":
    app = App()
    app.mainloop()
