"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any
# pip install prototools
from prototools import float_input


def ingresar_datos_lado(class_: type) -> None:
    lado: float = float_input("Ingresar el lado: ")
    _calcular(class_, lado)


def ingresar_datos_base_altura(class_: type) -> None:
    b: float = float_input("Ingresar la base: ")
    h: float = float_input("Ingresar la altura: ")
    _calcular(class_, b, h)


def _calcular(class_: type, *args: Any) -> None:
    objeto = class_(*args)
    area = objeto.area()
    perimetro = objeto.perimetro()
    print("El area es: ", area)
    print("El perimetro es: ", perimetro)
