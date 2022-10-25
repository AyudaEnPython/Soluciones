"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Tk


def _cleanup(w):
    w.delete(0, "end")


def calculate(x, y, result):
    try:
        result_ = float(x.get()) + float(y.get())
    except ValueError:
        result.config(text="Incorrect values")
        _cleanup(x)
        _cleanup(y)
    else:
        result.config(text=result_)


def setup_ui(master):
    x = Entry(master)
    y = Entry(master)
    result = Label(master)
    btn = Button(master, text="Calculate")
    btn["command"] = lambda: calculate(x, y, result)
    x.pack(padx=5, pady=5)
    y.pack(padx=5, pady=5)
    btn.pack(padx=5, pady=5)
    result.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    root.mainloop()
