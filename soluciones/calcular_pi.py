"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolle un programa para estimar el valor de pi usando la siguiente
suma infinita:

pi = 4(1 - 1/3 + 1/5 - 1/7 ...)

La entrada del programa debe ser un número entero n que indique cuántos
términos de la suma se utilizará.

Entrada:
5

Salida:
El valor de pi es: 3.3396825396825403

TODO: add other ways to implement it and write docstrings.
"""
from unittest import main, TestCase
from itertools import cycle


def pi_a(n: int) -> float:
    pi = 0
    sign = 1
    for i in range(1, n*2, 2):
        sign *= -1
        pi += (sign * -1) * (1/i)
    return pi * 4


def pi_b(n: int) -> float:
    return sum([j*(1/i) for i, j in zip(range(1, n*2, 2), cycle((1, -1)))])*4


def pi_c(n: int) -> float:
    if n == 1:
        return 4
    return 4 * (-1)**(n+1) * (1/(2*n - 1)) + pi_c(n-1)


class Test(TestCase):

    def test_pi(self):
        self.assertEqual(pi_a(5), 3.3396825396825403)
        self.assertEqual(pi_b(5), 3.3396825396825403)
        self.assertEqual(pi_c(5), 3.3396825396825403)


if __name__ == "__main__":
    main()