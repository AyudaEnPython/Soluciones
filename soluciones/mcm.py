"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Mínimo común múltiplo (MCM) de dos números naturales.
"""
import unittest
from typing import Callable

from mcd import mcd_recursivo, mcd_while, mcd_for


def mcm_usando_mcd(a: int, b: int, f: Callable = None) -> int:
    """Calcula el MCM de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :param f: Función que calcula el MCD de dos números naturales.
    :f type: Callable
    :return: MCM de los dos números.
    :rtype: int
    """
    if a == b:
        return a
    else:
        return a * b // f(a, b)


def mcm_recursivo(a: int, b: int, c: int = 1) -> int:
    """Calcula el MCM de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :return: MCM de los dos números.
    :rtype: int
    """
    if c % a == 0 and c % b == 0:
        return c
    else:
        return mcm_recursivo(a, b, c+1)


def mcm_for(a: int, b: int) -> int:
    """Calcula el MCM de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :return: MCM de los dos números.
    :rtype: int
    """
    for i in range(1, a*b+1):
        if i % a == 0 and i % b == 0:
            return i
    return 1


def mcm_while(a: int, b: int) -> int:
    """Calcula el MCM de dos números naturales.

    :param a: Primer número natural.
    :a type: int
    :param b: Segundo número natural.
    :b type: int
    :return: MCM de los dos números.
    :rtype: int
    """
    c = 1
    while c % a != 0 or c % b != 0:
        c += 1
    return c


def main():  # comment/uncomment to swtiches between mcm versions
    a = int(input('a: '))
    b = int(input('a: '))
    # mcm = mcm_usando_mcd(a, b)
    mcm = mcm_recursivo(a, b)
    # mcm = mcm_for(a, b)
    # mcm = mcm_while(a, b)
    print(f'MCM de {a} y {b} es {mcm}')


class Test(unittest.TestCase):

    data = (
        (2, 3, 6),
        (54, 24, 216),
        (40, 60, 120),
    )
    functions = mcd_recursivo, mcd_while, mcd_for

    def test_mcm_usando_mcd(self):
        for function, (a, b, expected) in zip(self.functions, self.data):
            self.assertEqual(mcm_usando_mcd(a, b, function), expected)

    def test_mcm_recursivo(self):
        for a, b, expected in self.data:
            self.assertEqual(mcm_recursivo(a, b), expected)

    def test_mcm_for(self):
        for a, b, expected in self.data:
            self.assertEqual(mcm_for(a, b), expected)

    def test_mcm_while(self):
        for a, b, expected in self.data:
            self.assertEqual(mcm_while(a, b), expected)


if __name__ == "__main__":
    # unittest.main()  # uncomment/comment to run tests
    main()
