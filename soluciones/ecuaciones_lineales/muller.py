"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from math import sqrt, floor
from typing import Callable

FuncionReal = Callable[[float], float]


def muller(
    f: FuncionReal,
    a: float,
    b: float,
    c: float,
    max_iter: int = 100
) -> float:
    """Método de muller para encontrar la raíz de una función.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :parma a: Valor inicial 1.
    :a type: float
    :parma b: Valor inicial 2.
    :b type: float
    :parma c: Valor inicial 3.
    :c type: float
    :parma max_iter: número máximo de iteraciones.
    :max_iter type: int
    """
    r = i = 0
    while True:
        f1, f2, f3 = f(a), f(b), f(c)
        d1, d2 = f1 - f3, f2 - f3
        h1, h2, a0 = a - c, b - c, f3
        a1 = ((d2 * pow(h1, 2)) - (d1 * pow(h2, 2))) / ((h1 * h2) * (h1 - h2))
        a2 = ((d1 * h2) - (d2 * h1)) / ((h1 * h2) * (h1 - h2))
        x = (-2 * a0) / (a1 + abs(sqrt(a1 * a1 - 4 * a0 * a2)))
        y = (-2 * a0) / (a1 - abs(sqrt(a1 * a1 - 4 * a0 * a2)))
        r = x + c if x >= y else y + c
        m, n = floor(r * 100), floor(c * 100)
        if m == n:
            break
        a, b, c = b, c, r
        if i > max_iter:
            break
        i += 1
    if i <= max_iter:
        return r


class Test(unittest.TestCase):

    def test_muller(self):
        self.assertAlmostEqual(
            muller(
                lambda x: ((x-3)**3)/6 - ((x-2)**2)/4 + x - 5,
                6,
                6.5,
                7,
            ),
            5.482324992229876
        )


if __name__ == "__main__":
    unittest.main()
