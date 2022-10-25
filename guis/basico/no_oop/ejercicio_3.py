"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, Tk


def total(x, y):
    return x * y


def _cleanup(w):
    w.delete(0, "end")


def calculate(price, quantity, result):
    try:
        price_ = float(price.get())
        quantity_ = float(quantity.get())
    except ValueError:
        result.config(text="Incorrect values")
        _cleanup(price)
        _cleanup(quantity)
    else:
        result.config(text=f"Total: $ {total(price_, quantity_)}")


def setup_ui(master):
    Label(master, text="Product name").pack()
    name = Entry(master)
    name.pack(padx=5, pady=5)
    Label(master, text="Price").pack()
    price = Entry(master)
    price.pack(padx=5, pady=5)
    Label(master, text="Quantity").pack()
    quantity = Entry(master)
    quantity.pack(padx=5, pady=5)
    result = Label(master)
    button = Button(master, text="Calculate")
    button["command"] = lambda: calculate(price, quantity, result)
    button.pack(padx=5, pady=5)
    result.pack(padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    root.mainloop()
