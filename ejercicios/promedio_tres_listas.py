"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente una función que reciba como parámetros tres listas y
devuelva una nueva lista con el promedio de las otras tres,
elemento por elemento.
"""
from itertools import zip_longest
from math import floor
from random import randint, sample
from typing import List
from unittest import main, TestCase


def random_list():
    return list(sample(range(1, 100), randint(1, 10)))


def promedio(a: List[int], b: List[int], c: List[int]) -> List[int]:
    """Calcula el promedio de los elementos de tres listas de
    diferentes tamaños.
    :param a: Lista de números enteros
    :a type: List[int]
    :param b: Lista de números enteros
    :b type: List[int]
    :param c: Lista de numeros enteros
    :c type: List[int]
    :return: Lista con el promedio de los elementos de las tres listas
    :rtype: List[int]
    """
    def avg(x: int) -> int:
        x = [n for n in x if n is not None]
        return floor((sum(x) / len(x)) + 0.5)
    return list(map(avg, zip_longest(a, b, c)))


def main_():
    a = random_list()
    b = random_list()
    c = random_list()
    p = promedio(a, b, c)
    print(a, b, c, sep='\n')
    print(p)


class Test(TestCase):

    data = (
        (
            [12, 9, 28, 11, 2, 35],
            [2, 8, 95, 12],
            [24, 81, 64, 35, 67, 18, 94],
            [13, 33, 62, 19, 35, 27, 94]),
        (
            [1, 4, 7],
            [2, 5],
            [3, 6, 9, 10],
            [2, 5, 8, 10]),
    )

    def test_promedio(self):
        for a, b, c, expected in self.data:
            self.assertEqual(promedio(a, b, c), expected)


if __name__ == '__main__':
    main()