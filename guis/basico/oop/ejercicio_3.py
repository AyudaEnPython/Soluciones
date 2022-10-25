"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from tkinter import Button, Entry, Label, Tk


@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total(self) -> float:
        return self.price * self.quantity


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()
        self.button["command"] = self.calculate

    def setup_ui(self) -> None:
        Label(self, text="Product name").pack()
        self.name = Entry(self)
        self.name.pack(padx=5, pady=5)
        Label(self, text="Price").pack()
        self.price = Entry(self)
        self.price.pack(padx=5, pady=5)
        Label(self, text="Quantity").pack()
        self.quantity = Entry(self)
        self.quantity.pack(padx=5, pady=5)
        self.result = Label(self)
        self.button = Button(self, text="Calculate")
        self.button.pack(padx=5, pady=5)
        self.result.pack(padx=5, pady=5)

    def calculate(self) -> None:
        try:
            price = float(self.price.get())
            quantity = float(self.quantity.get())
        except ValueError:
            self.result.config(text="Incorrect values")
            self._clenaup()
        else:
            product = Product(self.name.get(), price, quantity)
            self.result.config(text=f"Total: $ {product.total()}")

    def _clenaup(self):
        self.price.delete(0, "end")
        self.quantity.delete(0, "end")


if __name__ == "__main__":
    app = App()
    app.mainloop()
