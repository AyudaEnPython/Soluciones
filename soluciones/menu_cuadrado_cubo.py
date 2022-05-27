"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Debe crear un menú que permita las siguientes opciones:

1. Calcular área de un Cuadrado
2. Calcular el perímetro de un Cuadrado
3. Calcular el volumen de un Cubo
"""
# pip install prototools
from prototools import Menu, float_input


def area_cuadrado(lado: float) -> float:
    return lado * lado


def perimetro_cuadrado(lado: float) -> float:
    return lado * 4


def volumen_cubo(arista: float) -> float:
    return arista ** 3


def main():
    menu = Menu()
    menu.add_options(
        ("Área de un cuadrado",
            lambda: print(area_cuadrado(float_input("Lado: ")))),
        ("Perímetro de un cuadrado",
            lambda: print(perimetro_cuadrado(float_input("Lado: ")))),
        ("Volumen de un cubo",
            lambda: print(volumen_cubo(float_input("Arista: ")))),
    )
    menu.run()


if __name__ == "__main__":
    main()
