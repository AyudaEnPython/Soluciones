"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

sinx = x - (x**3)/3! + (x**5)/5! - (x**7)/7! + ...
cosx = 1 - (x**2)/2! + (x**4)/4! - (x**6)/6! + ...
tanx = x - (x**3)/3! + (2*(x**5))/15 - (17*(x**7))/315 + ...
arcsinx = x + 1/6*(x**3) + 3/40*(x**5) + 15/336*(x**7) + ...
"""
import math
from fractions import Fraction as Fr
from math import factorial as f
import unittest

N = 10


def _b(n):
    A = [0] * (n+1)
    for m in range(n+1):
        A[m] = Fr(1, m+1)
        for j in range(m, 0, -1):
            A[j-1] = j*(A[j-1] - A[j])
    return float(A[0])


def sinx(x, n=N):
    return sum((-1)**k * x**(2*k + 1) / f(2*k + 1) for k in range(n + 1))


def cosx(x, n=N):
    return sum((-1)**k * x**(2*k) / f(2*k) for k in range(n + 1))


def tanx(x, n=N):
    return sum(
        _b(2*k) / f(2*k) * ((-4)**k) * (1 - (4**k)) * (x**(2*k - 1))
        for k in range(1, n + 1)
    )


def arcsinx(x, n=N):
    return sum(
        f(2*k) * x**(2*k + 1) / ((4**k) * (f(k)**2) * (2*k + 1))
        for k in range(n + 1)
    )


class Test(unittest.TestCase):

    def test_sinx(self):
        self.assertAlmostEqual(math.sin(1), sinx(1), places=N)

    def test_cosx(self):
        self.assertAlmostEqual(math.cos(1), cosx(1), places=N)

    def test_tanx(self):
        self.assertAlmostEqual(math.tan(1), tanx(1), delta=0.001)
        self.assertAlmostEqual(math.tan(1), sinx(1)/cosx(1), delta=0.001)
        self.assertAlmostEqual(tanx(1), sinx(1)/cosx(1), delta=0.001)

    def test_arcsinx(self):
        self.assertAlmostEqual(math.asin(0.5), arcsinx(0.5), delta=0.001)
        self.assertAlmostEqual(math.asin(1), arcsinx(1), delta=0.18)


if __name__ == "__main__":
    unittest.main()
