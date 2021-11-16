"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar un programa que lea un número entero N y calcule el
resultado de la siguiente serie:

    +---------------------------------------------------------+
    | R = 1 + 1/(2)**2 + 1/(3)**2 + 1/(4)**2 + ... + 1/(N)**2 |
    +---------------------------------------------------------+
"""
from functools import lru_cache
from unittest import main, TestCase


def r(n: int) -> float:
    """
    Calcula el resultado de la serie.

    :param n: número entero positivo mayor o igual a 1.
    :return: resultado de la serie.
    """
    return sum(1 / (i**2) for i in range(1, n+1)) 


@lru_cache(maxsize=None)
def rr(n: int) -> float:
    """
    Calcula el resultado de la serie.

    :param n: número entero positivo mayor o igual a 1.
    :return: resultado de la serie.
    """
    if n == 1:
        return 1
    else:
        return 1 / (n**2) + rr(n - 1)


class Test(TestCase):

    def test_r(self):
        self.assertEqual(r(1), 1)
        self.assertEqual(r(2), 1.25)
        self.assertEqual(r(3), 1 + 1/(2**2) + 1/(3**2))
        self.assertEqual(r(5), 1.4636111111111112)

    def test_rr(self):
        self.assertEqual(rr(1), 1)
        self.assertEqual(rr(2), 1.25)
        self.assertEqual(rr(3), 1 + 1/(2**2) + 1/(3**2))
        self.assertEqual(rr(5), 1.4636111111111112)

    def test_r_and_rr(self):
        self.assertEqual(r(1), rr(1))
        self.assertEqual(r(5), rr(5))


if __name__ == '__main__':
    main()