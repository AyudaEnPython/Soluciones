"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from typing import Callable

FuncionReal = Callable[[float], float]


def bisection(
    f: FuncionReal,
    lower: float,
    upper: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> float:
    """Método de bisección para encontrar la raíz de una función.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :parma lower: límite inferior.
    :lower type: float
    :parma upper: límite superior.
    :upper type: float
    :parma tol: tolerancia.
    :tol type: float
    :parma max_iter: número máximo de iteraciones.
    :max_iter type: int
    :return: raíz de la función.
    :rtype: float
    """
    a, b = float(lower), float(upper)
    if a == b:
        raise ValueError("a y b deben ser diferentes")
    if a > b:
        a, b = b, a
    for _ in range(max_iter):
        c = (a + b) / 2
        if abs(c - a) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise RuntimeError("Número máximo de iteraciones alcanzado")


class Test(unittest.TestCase):

    def test_bisection(self):
        f = lambda x: x**3 - 1
        df = lambda x: 3*x**2
        self.assertAlmostEqual(bisection(f, -5, 5), 1.0000000149011612)


if __name__ == "__main__":
    unittest.main()
