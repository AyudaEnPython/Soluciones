"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu, int_input, tabulate

from models import Catalog, Order
from utils import FILENAME


class App(Menu):

    def __init__(self) -> None:
        super().__init__()
        self.add_options(
            ("Mostrar catalogo", self.show_catalog),
            ("Agregar producto, accesorio o servicio", self.add_to_catalog),
            ("Agregar orden", self.add_order),
            ("Calcular monto", self.calculate_price),
        )
        self.catalog = Catalog(FILENAME)
        self.orders = []

    def add_to_catalog(self) -> None:
        code = int_input("Ingrese el código: ")
        description = input("Ingrese la descripción: ")
        price = int_input("Ingrese el precio: ")
        self.catalog.add_item(code, description, price)
        self.catalog.save(FILENAME)

    def add_order(self) -> None:
        id_ = int_input("Ingrese el id: ")
        code = int_input("Ingrese el código: ")
        quantity = int_input("Ingrese la cantidad: ")
        self.orders.append(Order(id_, code, quantity))

    def calculate_price(self) -> None:
        orders = self.catalog.calculate(self.orders)
        for i, order in  enumerate(orders, 1):
            print(f"Orden # {i:02d}: {order}")
        print(f"Total: {sum(orders)}")
    
    def show_catalog(self) -> None:
        print(tabulate(
            self.catalog.data, headers=["id", "description", "price"]
        ))


if __name__ == "__main__":
    app = App()
    app.run()
