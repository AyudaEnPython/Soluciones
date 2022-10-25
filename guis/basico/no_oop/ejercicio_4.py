"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, messagebox, Tk

entries = []
labels = []


def _cleanup(entries):
    for entry in entries:
        entry.delete(0, "end")


def calculate(entries, labels):
    try:
        xs = [float(x.get()) for x in entries]
    except ValueError:
        messagebox.showerror(message="Incorrect values")
        _cleanup(entries)
    else:
        xs = sorted(xs, reverse=True)
        for label, number in zip(labels, xs):
            label.config(text=number)


def setup_ui(master):
    for _ in range(3):
        entries.append(Entry(master))
        labels.append(Label(master))
    btn = Button(master, text="Order")
    btn["command"] = lambda: calculate(entries, labels)
    for entry in entries:
        entry.pack(padx=5, pady=5)
    btn.pack(padx=5, pady=5)
    for label in labels:
        label.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    root.mainloop()
