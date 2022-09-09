"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir una función que calcula el área de un círculo y otra que
calcule el volumen de un cilindro usando la primera función.
"""
import unittest
from math import pi


def area_circulo(radio: float) -> float:
    """Calcula el área de un círculo.

    :param radio: Radio del círculo.
    :type radio: float
    :return: Área del círculo.
    :rtype: float
    """
    return pi * radio ** 2


def volumen_cilindro(radio: float, altura: float) -> float:
    """Calcula el volumen de un cilindro.

    :param radio: Radio del cilindro.
    :type radio: float
    :param altura: Altura del cilindro.
    :type altura: float
    :return: Volumen del cilindro.
    :rtype: float
    """
    return area_circulo(radio) * altura


def main():
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área del círculo: {area_circulo(radio)}")
    altura = float(input("Ingrese la altura del cilindro: "))
    print(f"Volumen del cilindro: {volumen_cilindro(radio, altura)}")


class Test(unittest.TestCase):

    def test_area_circulo(self):
        self.assertEqual(area_circulo(2), 12.566370614359172)

    def test_volumen_cilindro(self):
        self.assertEqual(volumen_cilindro(5, 10), 785.3981633974483)


if __name__ == "__main__":
    # unittest.main()
    main()
