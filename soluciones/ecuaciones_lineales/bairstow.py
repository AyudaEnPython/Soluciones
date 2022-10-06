"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: needs better implementation and refactor
"""
import unittest
from math import sqrt
from typing import Callable, List

FuncionReal = Callable[[float], float]
H = 1e-7


def solve(coef):
    s = [0]*4
    delta = coef[1]**2 - 4 * (coef[0] * coef[2])
    s[0] = -coef[1] / 2 / coef[2]
    s[2] = s[0]
    if delta < 0:
        s[1] = sqrt(-delta) / 2 / coef[2]
        s[3] = -s[1]
    else:
        s[1] = 0
        s[3] = 0
        s[0] = s[0] + sqrt(delta) / 2 / coef[2]
        s[2] = s[2] - sqrt(delta) / 2 / coef[2]
    return s


def bairstow(
    a: List[float],
    r: float,
    s: float,
) -> float:
    n = len(a)
    b = [0] * n
    c = [0] * n
    res = []
    while n > 3:
        b[n-1] = 1
        b[n-2] = 1
        while (abs(b[n-1]) + abs(b[n-2])) > 1e-6:
            b[0] = a[0]
            b[1] = a[1] + r * b[0]
            for i in range(2, n):
                b[i] = a[i] + r * b[i-1] + s * b[i-2]
            c[0] = b[0]
            c[1] = b[1] + r * c[0]
            for i in range(2, n-1):
                c[i] = b[i] + r * c[i-1] + s * c[i-2]
            h = (
                (-b[n-2] * c[n-3] + b[n-1] * c[n-4]) /
                (c[n-3] * c[n-3] - c[n-2] * c[n-4])
            )
            k = (
                (-b[n-1] * c[n-3] + b[n-2] * c[n-2]) /
                (c[n-3] * c[n-3] - c[n-2] * c[n-4])
            )
            r += h
            s += k
        res += solve([-s, -r, 1])
        a = b[:n-2]
        n = len(a)
        if n == 3:
            res += solve(a[::-1])
        res = [x for x in res if x > 0]
    return res


class Test(unittest.TestCase):

    def test_bairstow(self):
        self.assertAlmostEqual(
            bairstow(
                [0.2, -4.2, 35, -147, 324.8, -352.8, 144],
                1,
                1,
            ),
            [
                6.00000000000003,
                1.0000000000000004,
                4.999999999993942,  # 4.999999999993989,
                2.0000000000022604,  # 2.000000000002254,
                3.99999999999877,  # 3.9999996927379287,
                3.000000000003743,  # 3.0000001971795074,
            ],
        )


if __name__ == "__main__":
    unittest.main()
