"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from math import sqrt
from typing import Callable

FuncionReal = Callable[[float], float]
H = 1e-7


def f_(f: FuncionReal, x: float) -> float:
    return (f(x + H) - f(x)) / H


def f__(f: FuncionReal, x: float) -> float:
    return (f_(f, x + H) - f_(f, x)) / H 


def laguerre(
    f: FuncionReal,
    x0: float,
    n: int,
    tol: float = 1e-7,
    max_iter: int = 100
) -> float:
    """Método de Laguerre para encontrar la raíz de una función.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :parma x0: valor inicial.
    :x0 type: float
    :param tol: tolerancia.
    :tol type: float
    :return: raíz de la función.
    :rtype: float
    """
    xk = x0
    for _ in range(max_iter):
        if abs(f(xk)) < tol:
            break
        g = f_(f, xk) / f(xk)
        h = g ** 2 - (f__(f, xk) / f(xk))
        sq = sqrt(abs((n - 1) * (n * h - g**2)))
        dx = n / max([g + sq, g - sq], key=abs)
        xk -= dx
    return xk


class Test(unittest.TestCase):

    def test_laguerre(self):
        f = lambda x: 144 - 352.8*x + 324.8*x**2 - 147*x**3 + 35*x**4 - 4.2*x**5 + 0.2*x**6
        self.assertAlmostEqual(
            laguerre(f, 10, 6),
            6.000000012018115,
        )


if __name__ == "__main__":
    unittest.main()
