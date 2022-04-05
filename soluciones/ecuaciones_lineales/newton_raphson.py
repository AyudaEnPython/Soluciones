"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from math import sin, cos
from typing import Callable

FuncionReal = Callable[[float], float]


def newton_raphson(
    f: FuncionReal,
    df: FuncionReal,
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 100
) -> float:
    """Método de Newton-Raphson para encontrar la raíz de una función.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :param df: derivada de la función f.
    :df type: Callable
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
    for _ in range(max_iter):
        x = x - f(x) / df(x)
        if abs(f(x)) < tol:
            break
    return x


class Test(unittest.TestCase):

    results = (
        (
            lambda x: x**2 - 5*x + 2,
            lambda x: 2*x - 5,
            0.4,
            0.4384471871911695
        ),
        (
            lambda x: x**2 - 5,
            lambda x: 2*x,
            0.1,
            2.23606797749979,
        ),
        (
            lambda x: sin(x),
            lambda x: cos(x),
            2,
            3.1415926536808043,
        )
    )

    def test_newton_raphson(self):
        for f, df, x0, expected in self.results:
            self.assertAlmostEqual(newton_raphson(f, df, x0), expected)


if __name__ == "__main__":
    unittest.main()
