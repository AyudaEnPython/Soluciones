"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from cmath import sqrt
from typing import Tuple, Union
from unittest import main, TestCase


def solve(
    a: Union[int, float], 
    b: Union[int, float], 
    c: Union[int, float]
) -> Tuple[float, float]:
    """Resuelve ecuaciones de 2do grado.

    :param a: Coeficiente de la variable cuadrática
    :type a: Union[int, float]
    :param b: Coeficiente de la variable lineal
    :type b: Union[int, float]
    :param c: Término independiente
    :type c: Union[int, float]
    :return: Tupla de raices
    :rtype: Tuple[float, float]
    """
    d = b**2 - 4*a*c
    if d < 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
    elif d == 0:
        x1 = x2 = -b / (2*a)
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
    return x1, x2


class Test(TestCase):

    def test_solver(self):
        self.assertEqual(solve(1, -5, 6.0), (3.0, 2.0))
        self.assertEqual(solve(2.0, -7, 3), (3.0, 0.5))
        self.assertEqual(solve(1, -2, 1), (1.0, 1))

    def test_complex(self):
        self.assertEqual(solve(1, 0, 1), ((1j), (-1j)))
        self.assertEqual(solve(1, 0, 4), ((2j), (-2j)))
        self.assertEqual(solve(1, -2, 5), ((1+2j), (1-2j)))


if __name__ == "__main__":
    main()
