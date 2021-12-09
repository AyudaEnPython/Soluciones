"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe una función recursiva cuadrados(n) que calcule la sumatoria de
los cuadrados desde 1 hasta n.
"""
from unittest import main, TestCase


def sumatoria_cuadrados(n: int) -> int:
    """Calcula la sumatoria de los cuadrados desde 1 hasta n.

    :param n: número hasta el que se calcula la sumatoria.
    :n type: int
    :return: sumatoria de los cuadrados desde 1 hasta n.
    :rtype: int
    """
    if n == 1:
        return 1
    else:
        return n**2 + sumatoria_cuadrados(n-1)


def sumatoria_cuadrados_f(n: int) -> int:
    """Calcula la sumatoria de los cuadrados desde 1 hasta n.

    :param n: número hasta el que se calcula la sumatoria.
    :n type: int
    :return: sumatoria de los cuadrados desde 1 hasta n.
    :rtype: int
    """
    return (n*(n+1)*(2*n+1))/6


class Test(TestCase):

    expected = (1, 5, 14, 30, 55, 91, 140, 204, 285, 385)

    def test_sumatoria_cuadrados(self):
        for n in range(1, 11):
            self.assertEqual(sumatoria_cuadrados(n), self.expected[n-1])

    def test_sumatoria_cuadrados_f(self):
        for n in range(1, 11):
            self.assertEqual(sumatoria_cuadrados_f(n), self.expected[n-1])


if __name__ == "__main__":
    main()