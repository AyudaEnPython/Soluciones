"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Hacer un programa que pueda calcular el perímetro y el área de
cualquier polígono regular, pero que le pregunte al usuario qué
desea calcular.
"""
from math import pi, tan
from unittest import main, TestCase
# pip install prototools
from prototools import Menu, int_input, float_input


def perimetro(n: int, l:float) -> float:
    """Calcula el perimetro de un poligono regular.

    :param n: Numero de lados del poligono.
    :n type: int
    :param l: Longitud de un lado.
    :l type: float
    :return: Perimetro del poligono.
    """
    return n * l


def area(n: int, l:float):
    """Calcula el área de un polígono regular.
    
    :param l: longitud de un lado
    :l type: float
    :param n: numero de lados
    :n type: int
    :return: area del poligono
    :rtype: float
    """
    return ((l**2) * n)/(4 * tan(pi/n))


def main_():
    menu = Menu()
    menu.add_options(
        ("Perimetro", 
            lambda: print(perimetro(
                int_input("Numero de lados: "),
                float_input("Longitud de un lado: ")))),
        ("Area",
            lambda: print(area(
                int_input("Numero de lados: "),
                float_input("Longitud de un lado: ")))),
    )
    menu.run()


class Test(TestCase):

    def test_perimetro(self):
        self.assertEqual(perimetro(3, 1), 3)
        self.assertEqual(perimetro(4, 2), 8)
        self.assertEqual(perimetro(5, 3), 15)

    def test_area(self):
        self.assertEqual(round(area(3, 5), 2), 10.83)
        self.assertEqual(round(area(4, 6), 2), 36.00)
        self.assertEqual(round(area(5, 7), 2), 84.30)


if __name__ == "__main__":
    # main_() uncomment this and comment the next line to run tests
    main()