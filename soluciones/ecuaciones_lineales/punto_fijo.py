"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from typing import Callable

FuncionReal = Callable[[float], float]


def punto_fijo(
    f: FuncionReal,
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 100
) -> float:
    """Método de punto fijo para encontrar la raíz de una función.

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
    for _ in range(max_iter):
        x = f(x)
        if abs(f(x)) < tol:
            break
    return x


class Test(unittest.TestCase):

    def test_punto_fijo(self):
        f = lambda x: x**2 - 5*x + 2
        g = lambda x: -2 / (x - 5)
        self.assertAlmostEqual(punto_fijo(g, 1), 0.4384471871911695)


if __name__ == "__main__":
    unittest.main()
