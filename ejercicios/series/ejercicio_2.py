"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar un programa que dado los valores introducidos de x y n,
calcule:

    +------------------------------------------------------------+
    | F(x, n) = ((x-1)**n)/1 + ((x-2)**n)/2 + ... + ((x-n)**n)/n |
    +------------------------------------------------------------+
"""
from functools import lru_cache
from unittest import main, TestCase


def f(x: int, n: int) -> float:
    """
    Calcula el resultado de la serie.
    """
    return sum([((x - i) ** n) / i for i in range(1, n + 1)])


@lru_cache(maxsize=None)
def rf(x: int, n: int, i: int) -> float:
    if i == 1:
        return (x - 1) ** n
    return ((x - i) ** n) / i + rf(x, n, i - 1)


class Test(TestCase):

    def test_f(self):
        self.assertEqual(f(2, 3), 0.6666666666666667)
        self.assertEqual(f(2, 4), 5.3333333333333333)

    def test_rf(self):
        self.assertEqual(rf(2, 3, 3), 0.6666666666666667)
        self.assertEqual(rf(2, 4, 4), 5.3333333333333333)


if __name__ == '__main__':
    main()