"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realice un programa que reciba el radio y la altura de un cilindro.
Con base en estos datos, el programa debe preguntarle al usuario qué
operación de las siguientes desea realizar:

1) Calcular el área de las bases.
2) Calcular el área lateral.
3) Calcular el área total
4) Calcular el volumen.

Cree su programa utilizando estructuras de control de flujo, e imprima
el valor de la respuesta al usuario.

NOTE: add docstring and tests later...
"""
from math import pi

from prototools import Menu


def _area_circulo(radio: float) -> float:
    return pi * radio ** 2


def area_bases(radio: float) -> float:
    return 2 * _area_circulo(radio)


def area_lateral(radio: float, altura: float) -> float:
    return 2 * pi * radio * altura


def area_total(radio: float, altura: float) -> float:
    return area_lateral(radio, altura) + area_bases(radio)


def volumen(radio: float, altura: float) -> float:
    return _area_circulo(radio) * altura


def main():
    menu = Menu()
    menu.add_options(
        ("Calcular el área de las bases", area_bases),
        ("Calcular el área lateral", area_lateral),
        ("Calcular el área total", area_total),
        ("Calcular el volumen", volumen),
    )
    menu.run()


if __name__ == "__main__":
    main()
