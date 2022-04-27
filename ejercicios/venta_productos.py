"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una tienda vende tres tipos de productos a los precios dados en la
siguiente tabla:

    +----------+----------+
    | Producto |  Precio  |
    +----------+----------+
    |    P1    | S/. 15.0 | 
    |    P2    | S/. 17.5 | 
    |    P3    | S/. 20.0 |
    +----------+----------+

Dados el tipo de producto y la cantidad de unidades requeridas, diseñe
un programa que muestre luego de cada venta:

- El importe a pagar para la venta efectuada.
- La cantidad de ventas efectuadas de cada tipo de producto.
- El importe pagado acumulado por cada tipo de producto.

Declare como globales a las variables absolutamente necesarias y use
los siguientes métodos:

- getProducto: Lee y retorna el producto a vender
- getCantidad: Lee y retorna la cantidad de unidades a vender
- calcularImportePagar: Calcula y retorna el importe a pagar
- efectuarIncrementos: Efectúa los incrementos requeridos
- mostrarResultados: Muestra los resultados solicitados

NOTE: Se opta por rediseñar.
"""
from dataclasses import dataclass
from typing import Dict
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
        self.total = 0
        self.ventas = {
            k: 0 for k in self.productos.keys()
        }

    def ingresar_venta(self) -> None:
        producto = menu_input(tuple(self.productos.keys()), numbers=True)
        cantidad = float_input("Cantidad: ")
        self.productos[producto].cantidad += cantidad
        importe = self.productos[producto].importe()
        self.total += importe
        self.ventas[producto] += 1
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

    def ver_ventas(self) -> None:
        textbox("Cantidad de ventas efectuadas por producto", width=30)
        for k, v in self.ventas.items():
            print(f"{self.productos[k].nombre}: {v}")

    def ver_total(self) -> None:
        print(f"Total: {self.total}")

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
    app = Tienda()
    app.run()
