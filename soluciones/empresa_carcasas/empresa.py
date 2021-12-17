"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import Tuple, Dict, List

# pip install prototools
from prototools import Menu, menu_input, int_input, tabulate
from prototools.utils import textbox

MARCAS: Tuple[str] = ("Huawei", "Xiaomi", "Apple", "Samsung")


def _ingresar() -> Tuple[str, int]:
    marca = menu_input(MARCAS, numbers=True).lower()
    cantidad = int_input(f"Cantidad de carcasas ({marca}):")
    return marca, cantidad


@dataclass
class Carcasa:
    marca: str
    cantidad: int

    def __post_init__(self) -> None:
        self.precio = self._precio()
        self.cables = self._cables()
        self.micas = self._micas()

    def _precio(self):
        precios = {
            "huawei": 54.9,
            "xiaomi": 45.9,
            "apple": 60.9,
            "samsung": 50.9,
        }
        self.unitario = precios[self.marca]
        return precios[self.marca]*self.cantidad

    def _cables(self) -> int:
        cantidad: Dict[bool, int] = {
            self.cantidad <= 5: 2,
            5 < self.cantidad <= 10: 3,
            10 < self.cantidad <= 15: self.cantidad,
            self.cantidad > 15: self.cantidad *2,
        }
        return cantidad[True]

    def _micas(self) -> int:
        tipo: Dict[str, int] = {
            "huawei": 4,
            "xiaomi": 3,
            "apple": 2,
            "samsung": 2,
        }
        return tipo[self.marca]*self.cantidad


@dataclass
class Empresa:

    flag: bool = False
    
    def ingresar_pedidos(self) -> None:
        marca, cantidad = _ingresar()
        self.producto = Carcasa(marca, cantidad)
        textbox("Pedido ingresado correctamente!")
        self.flag = True

    def mostrar_importe(self) -> None:
        if not self.flag:
            textbox("No hay pedidos ingresados!")
            return
        print(
            tabulate(
                [
                    ["Marca", self.producto.marca.title()],
                    ["Precio por unidad", f"S/. {self.producto.unitario}"],
                    ["Cantidad", self.producto.cantidad],
                    ["Cables de obsequio", self.producto.cables],
                    ["Micas de obsequio", self.producto.micas],
                    ["Importe a pagar", f"S/. {self.producto.precio:.2f}"],
                ],
                headers=["Descripción", "Detalles"],
                align="right",
            )
        )
