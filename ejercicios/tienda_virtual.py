"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un sistema en consola que simule a una tienda virtual y permita
realizar lo siguiente:

1) Menú de opciones mínmio con 4 tipos de productos.
2) Realizar el cálculo total a pagar del cliente.
3) Validaciones necesarias que le permita al usuario continuar o salir
    en el sistema.
"""
from typing import Dict
# pip install prototools
from prototools import Menu, menu_input, float_input, textbox


PRODUCTOS: Dict[str, float] = {
    "televisor": 1780.99,
    "celular": 1490.99,
    "laptop": 2390.99,
    "tablet": 999.99,
}


class TiendaVirtual(Menu):

    def __init__(self):
        super().__init__()
        self.productos = PRODUCTOS
        self.total = 0
        self.add_options(
            ("Ingresar venta", self.ingresar_venta),
            ("Calcular total", self.ver_total),
        )

    def ingresar_venta(self):
        self._clear()
        producto = menu_input(tuple(self.productos.keys()), numbers=True)
        cantidad = float_input("Ingrese la cantidad: ")
        self.total += self.productos[producto] * cantidad

    def ver_total(self):
        textbox(f"El total a pagar es: {self.total}")

    def _clear(self):
        self.total = 0


if __name__ == "__main__":
    tienda = TiendaVirtual()
    tienda.run()
