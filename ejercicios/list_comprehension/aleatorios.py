"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Usando listas de comprensión, implemente un programa que genere 10
números decimales aleatorios con dos decimales entre 10 y 20.

    +-------------------------------------------+
    | respuesta: [                              |
    |     19.42, 18.09, 14.46, 14.11, 14.09,    |
    |     15.41, 13.14, 18.13, 19.18, 12.77,    |
    | ]                                         |
    +-------------------------------------------+
"""
from random import uniform, seed
from typing import List
import unittest


def generar_decimales(min: int, max: int, n: int, r: int = 2) -> List[float]:
    """Genera 'n' números aleatorios entre 'min' y 'max' con 'r'
    decimales. Por defecto, 'r' es 2.

    :param min: Mínimo valor
    :min type: int
    :param max: Máximo valor
    :max type: int
    :param n: Número de números aleatorios
    :n type: int
    :param r: Número de decimales
    :r type: int
    :return: Lista con 'n' números aleatorios
    :return type: List[float]
    """
    return [round(uniform(min, max), r) for _ in range(n)]


def main():
    print("respuesta: ", generar_decimales(10, 20, 10))


class Test(unittest.TestCase):

    def test_generar_decimales(self):
        seed(1)
        self.assertEqual(
            generar_decimales(10, 20, 10),
            [
                11.34, 18.47, 17.64, 12.55, 14.95,
                14.49, 16.52, 17.89, 10.94, 10.28,
            ]
        )
        seed(100)
        self.assertEqual(
            generar_decimales(10, 20, 10),
            [
                11.46, 14.55, 17.71, 17.06, 17.32,
                14.34, 18.0, 15.33, 10.8, 14.56,
            ]
        )


if __name__ == "__main__":
    # unittest.main()
    main()
