"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import math
import unittest


def simpson_1_3(f, a, b, n):
    h = (b - a) / n
    k = f(a) + f(b)
    for i in range(1, n):
        if i % 2 == 0:
            k += 2 * f(a + i * h)
        else:
            k += 4 * f(a + i * h)
    return (h / 3) * k


class Test(unittest.TestCase):

    cases = (
        (lambda x: math.log(x), (4, 5.2, 6), 1.827847257950486),
        (lambda x: 1/(1 + x**2), (0.0, 1.0, 10), 0.7853981534848037),
    )

    def test_simpson(self):
        for f, (a, b, n), expected in self.cases:
            self.assertAlmostEqual(simpson_1_3(f, a, b, n), expected)


if __name__ == "__main__":
    unittest.main()
