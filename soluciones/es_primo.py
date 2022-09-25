"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import sqrt
from typing import Iterable
import unittest


def es_primo_naive(numero: int) -> bool:
    primo = True
    if numero == 2 or numero == 3:
        primo = True
    elif numero % 2 == 0 or numero < 2:
        primo = False
    else:
        for i in range(3, int(numero**0.5)+1, 2):
            if numero % i == 0:
                primo = False
    return primo


def es_primo(n: int) -> bool:
    """Determina si el número es primo o no.

    :param n: Número a verificar
    :type n: int
    :returns: True si es primo, False si no lo es
    :rtype: bool

    >>> es_primo_(2)
    True
    >>> es_primo_(1)
    False
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def es_primo_(n: int) -> bool:
    """Verifica si el número es primo o no.

    :param n: Número a verificar
    :type n: int
    :return: True si es primo, False si no lo es
    :rtype: bool

    >>> es_primo_(2)
    True
    >>> es_primo_(1)
    False
    """
    if 1 < n < 4:
        return True
    elif n < 2 or not n % 2:
        return False
    impares: Iterable = range(3, int(sqrt(n) + 1), 2)
    return not any(not n % i for i in impares)


class Test(unittest.TestCase):

    true_cases = 2, 3, 5, 7, 11, 13
    false_cases = 1, 10, 33, -19, 0, 3*5
    functions = es_primo, es_primo_, es_primo_naive

    def test_primos(self):
        for f in self.functions:
            for n in self.true_cases:
                self.assertTrue(f(n))

    def test_no_primos(self):
        for f in self.functions:
            for n in self.false_cases:
                self.assertFalse(f(n))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    unittest.main()
