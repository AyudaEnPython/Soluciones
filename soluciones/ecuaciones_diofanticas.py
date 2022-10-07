"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Cree una rutina en Python que solucione ecuaciones diofánticas de la
forma:
        ax + by = c     a, b, c E Z

El programa debe:
- Chequear si la ecuación ingresada tiene solución.
- Encontrar la solución.
- Ofrecer al usuario encontrar más soluciones.

TODO: add docstrings and more testcases.
"""
import unittest
from typing import Tuple
# pip install prototools
from prototools import main_loop
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/mcd.py
from mcd import mcd_while


def solver(a: int, b: int, c: int) -> Tuple[int, int]:
    q, r = divmod(a, b)
    if r == 0:
        return 0, c/b
    else:
        sol = solver(b, r, c)
        u = sol[0]
        v = sol[1]
        return v, u - q*v


def dio(a: int, b: int, c: int) -> bool:
    assert c % mcd_while(a, b) == 0
    (d, x, y) = ex_mcd(a, b)
    r = c / d
    return (r*x, r*y)


def ex_mcd(a: int, b: int) -> Tuple[int, int, int]:
    assert a >= 0 and b >= 0
    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = ex_mcd(b, a % b)
        x = q
        y = p - q * (a // b)
    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return d, x, y


def dio_all(a: int, b: int, c: int, n: int = 2) -> None:
    (x0, y0) = dio(a, b, c)
    d = mcd_while(a, b)
    p = a // d
    q = b // d
    for i in range(n):
        x = x0 + i * q
        y = y0 - i * p
        print(x, y)


def main():
    a, b, c = [int(x) for x in input("> ").split(",")]
    # print(dio(a, b, c))  # uncomment/comment to switch versions
    dio_all(a, b, c)


class Test(unittest.TestCase):

    def test_mcd_while(self):
        self.assertEqual(mcd_while(121, 11), 11)

    def test_solver(self):
        self.assertEqual(solver(12345, 54321, 3), (3617, -822))
        self.assertEqual(solver(5, 17, 103), (721, -206))


if __name__ == '__main__':
    # unittest.main()  # uncomment / comment to run tests
    main_loop(main)
