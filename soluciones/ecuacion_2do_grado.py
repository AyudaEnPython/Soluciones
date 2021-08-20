from cmath import sqrt
from typing import Tuple
from unittest import main, TestCase

def solucion(a: int, b: int, c: int) -> Tuple[float, float]:
    """Resuelve ecuaciones de 2do grado

    :param a: Coeficiente de la variable cuadrática
    :type a: int
    :param b: Coeficiente de la variable lineal
    :type b: int
    :param c: Término independiente
    :type c: int
    :return: Tupla de raices.
    :rtype: Tuple[float, float]
    """
    d = b*b - 4*a*c
    if d < 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
    return x1, x2


class TestSolucion(TestCase):

    def test_solucion(self):
        self.assertEqual(solucion(1, -5, 6), (3.0, 2.0))
        self.assertEqual(solucion(2, -7, 3), (3.0, 0.5))
        self.assertEqual(solucion(1, -2, 5), ((1+2j), (1-2j)))


if __name__ == "__main__":
    main()