"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import logging
import unittest

logging.basicConfig(level=logging.INFO)


def raiz_cubica(x: int, e: float = 0.01) -> float:
    s = 1
    while abs(((2/3)*s + (1/3)*x/(s**2))**3 - x) >= e:
        s = (2/3)*s + (1/3)*x/(s**2)  # == (1/3)*(2*s + x/(s**2))
        logging.info(f"s = {s}")
    return s


def raiz_cuadrada(b: int, r: int = 1, e: float = 0.00001) -> float:
    h = b
    while abs(h**2 - b) >= e:
        h = (h + b/h) / 2
        logging.info(f"h = {h}")
    return h


class Test(unittest.TestCase):

    def test_raiz_cubica(self):
        f = lambda x: x**(1./3.) if x > 0 else -(-x)**(1./3.)  # noqa: E731
        self.assertAlmostEqual(raiz_cubica(235), f(235), delta=0.1)
        self.assertAlmostEqual(raiz_cubica(-91.6), f(-91.6), delta=0.1)

    def test_raiz_cuadrada(self):
        from math import sqrt
        f = raiz_cuadrada
        self.assertAlmostEqual(f(4590), sqrt(4590), delta=0.000001)
        self.assertAlmostEqual(f(32323), sqrt(32323), delta=0.000001)


if __name__ == "__main__":
    unittest.main()
