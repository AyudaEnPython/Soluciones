"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Encontrar la suma de los primos entre a y b.
"""
from math import sqrt
from typing import Iterable
from unittest import main, TestCase


# función "es_primo" del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
def es_primo(n: int) -> bool:
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


def sumatoria_primos(a: int, b: int) -> int:
    """Suma los primos entre a y b.

    :param a: Limite inferior
    :type a: int
    :param b: Limite superior
    :type b: int
    :return: Suma de los primos entre a y b
    :rtype: int
    """
    return sum(i for i in range(a, b + 1) if es_primo(i))


def main_():
    a = int(input("a: "))
    b = int(input("b: "))
    print(sumatoria_primos(a, b))


class Test(TestCase):

    def test_sumatoria_primos(self):
        self.assertEqual(sumatoria_primos(1, 10), 17)
        self.assertEqual(sumatoria_primos(1, 100), 1060)
        self.assertEqual(sumatoria_primos(1, 1000), 76127)


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run the tests
    main_()
