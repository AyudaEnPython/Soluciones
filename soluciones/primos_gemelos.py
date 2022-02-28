"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe un programa que pida al usuario dos números enteros positivos y
que imprima por pantalla todos los números primos gemelos comprendidos
entre dichos números. Los números primos gemelos son una pareja de
números primos con una diferencia entre sí de exactamente dos unidades.
Por ejemplo, 3 y 5 son números primoes gemelos.
"""
from math import sqrt
from typing import Iterable, List, Tuple
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


def primos_gemelos(n1: int, n2: int) -> List[Tuple[int, int]]:
    """Devuelve una lista de tuplas con los primos gemelos entre n1 y n2.

    :param n1: Primer número
    :type n1: int
    :param n2: Segundo número
    :type n2: int
    :return: Lista de tuplas de primos gemelos
    :rtype: list
    """
    primos: Iterable = (i for i in range(n1, n2 + 1) if es_primo(i))
    return [(i, i + 2) for i in primos if es_primo(i + 2)]


def main_():
    a = int(input("a: "))
    b = int(input("b: "))
    print(primos_gemelos(a, b))


class Test(TestCase):

    data = (
        ((1, 10), [(3, 5), (5, 7)]),
        ((10, 20), [(11, 13), (17, 19)]),
        ((20, 70), [(29, 31), (41, 43), (59, 61)]),
        ((70, 140), [(71, 73), (101, 103), (107, 109), (137, 139)]),
    )

    def test_f(self):
        for arg, expected in self.data:
            self.assertEqual(primos_gemelos(*arg), expected)


if __name__ == "__main__":
    # main() # umcomment this line and comment the next one to run tests
    main_()
