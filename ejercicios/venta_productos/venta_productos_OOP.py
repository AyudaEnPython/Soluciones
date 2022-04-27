"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import Dict, Tuple
# pip install prototools
from prototools import Menu, menu_input, float_input, tabulate, textbox


@dataclass
class Producto:
    nombre: str
    cantidad: int
    precio: float

    def importe(self):
        return self.cantidad * self.precio


class Tienda(Menu):

    def __init__(self, productos: Dict[str, Producto]) -> None:
        super().__init__()
        self.add_options(
            ("Ingresar venta", self.ingresar_venta),
            ("Ventas efectuadas", self.ver_ventas),
            ("Ver total", self.ver_total),
            ("Añadir producto", self.añadir_producto),
        )
        self.productos = productos
        self.ventas = {k: 0 for k in self.productos.keys()}
        self.total = 0

    def _ingresar(self) -> Tuple[str, float]:
        producto = menu_input(tuple(self.productos.keys()), numbers=True)
        cantidad = float_input("Cantidad: ")
        return producto, cantidad

    def _mostrar(self, producto: str, importe: float) -> None:
        print(tabulate(
            [
                ["Producto", self.productos[producto].nombre],
                ["Cantidad", self.productos[producto].cantidad],
                ["Precio unitario", self.productos[producto].precio],
                ["Total a pagar", importe],
            ],
            headers=["Descripción", "Importe"],
        ))
        textbox("Gracias por su compra", width=30)

    def ingresar_venta(self) -> None:
        producto, cantidad = self._ingresar()
        self.productos[producto].cantidad += cantidad
        importe = self.productos[producto].importe()
        self.total += importe
        self.ventas[producto] += 1
        self._mostrar(producto, importe)

    def ver_ventas(self) -> None:
        textbox("Cantidad de ventas efectuadas por producto", width=50)
        for k, v in self.ventas.items():
            print(f"{self.productos[k].nombre}: {v}")

    def ver_total(self) -> None:
        textbox(f"Total: {self.total}", width=30)

    def añadir_producto(self) -> None:
        textbox("Añadir producto", width=30)
        nombre = input("Nombre: ")
        precio = float_input("Precio: ")
        self.productos[nombre] = Producto(nombre, 0, precio)
        self.ventas[nombre] = 0


if __name__ == "__main__":
    productos = {
        "P1": Producto("P1", 0, 15.0),
        "P2": Producto("P2", 0, 17.5),
        "P3": Producto("P3", 0, 20.0),
    }
    app = Tienda(productos)
    app.run()
