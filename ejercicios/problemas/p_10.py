"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import pi
from typing import Tuple
# pip install prototools
from prototools import Menu, float_input

AreaPerimetro = Tuple[float, float]


def _circulo(radio: float) -> AreaPerimetro:
    return pi * (radio ** 2), pi * 2 * radio


def _paralelogramo(b: float, h: float) -> AreaPerimetro:
    return b * h, 2 * (b + h)


def _trapecio(B: float, b: float, h: float, c: float) -> AreaPerimetro:
    return (B + b)/2 * h, (B + b) + 2 * c


def _rombo(d1: float, d2: float, a: float) -> AreaPerimetro:
    return (d1 * d2)/2, 4*a


class App(Menu):

    def __init__(self):
        super().__init__()
        self.add_options(
            ("Circulo", self.circulo),
            ("Paralelogramo", self.paralelogramo),
            ("Trapecio", self.trapecio),
            ("Rombo", self.rombo),
        )

    def circulo(self):
        radio = float_input("Ingrese el radio del circulo: ")
        area, perimetro = _circulo(radio)
        print(f"El area del circulo es: {area}")
        print(f"El perimetro del circulo es: {perimetro}")

    def paralelogramo(self):
        b = float_input("Ingrese el valor de la base: ")
        h = float_input("Ingrese el valor de la altura: ")
        area, perimetro = _paralelogramo(b, h)
        print(f"El area del paralelogramo es: {area}")
        print(f"El perimetro del paralelogramo es: {perimetro}")

    def trapecio(self):
        B = float_input("Ingrese el valor de la base mayor: ")
        b = float_input("Ingrese el valor de la base menor: ")
        h = float_input("Ingrese el valor de la altura: ")
        c = float_input("Ingrese el valor del lado de la base: ")
        area, perimetro = _trapecio(B, b, h, c)
        print(f"El area del trapecio es: {area}")
        print(f"El perimetro del trapecio es: {perimetro}")

    def rombo(self):
        d1 = float_input("Ingrese el valor de la diagonal mayor: ")
        d2 = float_input("Ingrese el valor de la diagonal menor: ")
        a = float_input("Ingrese el valor del angulo: ")
        area, perimetro = _rombo(d1, d2, a)
        print(f"El area del rombo es: {area}")
        print(f"El perimetro del rombo es: {perimetro}")


if __name__ == "__main__":
    app = App()
    app.run()
