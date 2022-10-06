"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import exp
from typing import Callable
import unittest

FuncionReal = Callable[[float], float]


def secante(
    f: FuncionReal,
    lower: float,
    upper: float,
    repeats: int,
) -> float:
    """Método de la secante para encontrar la raíz de una función.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :parma lower: límite inferior.
    :lower type: float
    :parma upper: límite superior.
    :upper type: float
    :parma repeats: número de iteraciones.
    :repeats type: int
    :return: raíz de la función.
    :rtype: float
    """
    x0, x1 = lower, upper
    for _ in range(repeats):
        x0, x1 = x1, x0 - f(x0) * (x1 - x0) / (f(x1) - f(x0))
    return x1


class Test(unittest.TestCase):

    def test_secante(self):
        f = lambda x: 8*x - 2 * exp(-x)  # noqa: E731
        self.assertAlmostEqual(secante(f, 1, 3, 2), 0.2139409276214589)


if __name__ == "__main__":
    unittest.main()
