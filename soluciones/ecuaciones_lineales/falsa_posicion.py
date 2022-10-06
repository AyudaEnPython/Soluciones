"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from typing import Callable

FuncionReal = Callable[[float], float]


def falsa_posicion(
    f: FuncionReal,
    a: float,
    b: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> float:
    """Método de falsa posición.

    :parma f: función a la cual se le aplica el método.
    :f type: Callable
    :parma a: límite inferior.
    :a type: float
    :parma b: límite superior.
    :b type: float
    :parma tol: tolerancia.
    :tol type: float
    :parma max_iter: número máximo de iteraciones.
    :max_iter type: int
    :return: raíz de la función.
    :rtype: float
    """
    a = float(a)
    b = float(b)
    if a == b:
        raise ValueError("a y b deben ser diferentes")
    if a > b:
        a, b = b, a
    for _ in range(max_iter):
        c = a - f(a) * (b - a) / (f(b) - f(a))
        if abs(c - a) < tol:
            return c
        a, b = b, c
    raise RuntimeError("Número máximo de iteraciones alcanzado")


class Test(unittest.TestCase):

    def test_falsa_posicion(self):
        f = lambda x: x**2 - 5*x + 2  # noqa: E731
        self.assertAlmostEqual(falsa_posicion(f, 0.4, 0.5), 0.4384471871911695)


if __name__ == "__main__":
    unittest.main()
