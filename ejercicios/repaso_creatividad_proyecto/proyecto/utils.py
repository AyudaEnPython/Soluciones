# pip install prototools
from typing import Any
from prototools.entradas import entrada_float


def ingresar_datos_lado(class_: type) -> None:
    lado: float = entrada_float("Ingresar el lado: ")
    _calcular(class_, lado)


def ingresar_datos_base_altura(class_: type) -> None:
    b: float = entrada_float("Ingresar la base: ")
    h: float = entrada_float("Ingresar la altura: ")
    _calcular(class_, b, h)


def _calcular(class_: type, *args: Any) -> None:
    objeto = class_(*args)
    area = objeto.area()
    perimetro = objeto.perimetro()
    print("El area es: ", area)
    print("El perimetro es: ", perimetro)