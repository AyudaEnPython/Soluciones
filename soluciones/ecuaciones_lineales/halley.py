"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from typing import Callable

FuncionReal = Callable[[float], float]
H = 1e-7


def f_(f: FuncionReal, x: float) -> float:
    return (f(x + H) - f(x)) / H


def f__(f: FuncionReal, x: float) -> float:
    return (f_(f, x + H) - f_(f, x)) / H


def halley(
    f: FuncionReal,
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 100
) -> float:
    """Método de Halley para encontrar la raíz de una función.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :parma x0: valor inicial.
    :x0 type: float
    :param tol: tolerancia.
    :tol type: float
    :parma max_iter: número máximo de iteraciones.
    :max_iter type: int
    :return: raíz de la función.
    :rtype: float
    """
    x = x0
    fpx = f_(f, x)
    fppx = f__(f, x + H)
    for _ in range(max_iter):
        x = x - (2 * f(x) * fpx) / (2 * fpx**2 - f(x) * fppx)
        if abs(f(x)) < tol:
            break
    return x


class Test(unittest.TestCase):

    def test_halley(self):
        f = lambda x: x**2 - 5*x + 2  # noqa: E731
        self.assertAlmostEqual(halley(f, 1), 0.4384471871911695)


if __name__ == "__main__":
    unittest.main()
