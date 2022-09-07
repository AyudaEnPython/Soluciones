"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Permutaciones - Recursividad

Escribe una función que reciba un array de enteros únicos (no hay
repetidos) de tamaño n y retorne una matriz con todas las permutaciones
del array, sin nigún orden en particular.
"""
import unittest
from typing import List


def permutar(arr: List[int]) -> List[List[int]]:
    """Devuelve todas las permutaciones del array.

    :param arr: Lista de enteros únicos.
    :arr type: List[int]
    :return: Lista de permutaciones.
    :rtype: List[List[int]]
    """
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    t = []
    for i in range(len(arr)):
        r = arr[:i] + arr[i+1:]
        for p in permutar(r):
            t.append([arr[i]] + p)
    return t


def main():
    indicacion = "Ingresar elementos separados por coma (,): "
    arr = list(map(int, input(indicacion).split(",")))
    print(f"Input: {arr}")
    print(f"Output: {permutar(arr)}")


class Test(unittest.TestCase):

    def test_permutar(self):
        self.assertEqual(
            permutar([1, 2, 3]),
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ]
        )


if __name__ == "__main__":
    # unittest.main()
    main()
