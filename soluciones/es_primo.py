from math import sqrt
from typing import Iterable
from unittest import main, TestCase

def es_primo(n: int) -> bool:
    """Verifica si el número es primo o no.

    :param n: Número a verificar
    :type n: int
    :return: True si es primo, False si no lo es
    :rtype: bool

    >>> es_primo(2)
    True
    >>> es_primo(1)
    False
    """
    if 1 < n < 4:
        return True
    elif n < 2 or not n % 2:
        return False
    impares: Iterable = range(3, int(sqrt(n) + 1), 2)
    return not any(not n % i for i in impares)


class Test(TestCase):

    def test_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(3))
        self.assertTrue(es_primo(5))
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(11))
    
    def test_no_primos(self):
        self.assertFalse(es_primo(-19))
        self.assertFalse(es_primo(0))
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(3*5))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()