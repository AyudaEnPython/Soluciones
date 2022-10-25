"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Tk


def show(entry, label):
    txt = entry.get()
    label.config(text=f"Hello {txt}")


def setup_ui(master):
    entry = Entry(master)
    label = Label(master)
    button = Button(master, text="Press me")
    button["command"] = lambda: show(entry, label)
    entry.pack(padx=5, pady=5)
    button.pack(padx=5, pady=5)
    label.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    root.mainloop()
