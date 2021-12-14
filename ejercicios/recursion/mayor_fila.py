"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Mayor fila - Recursividad

Escriba una función recursiva en Python que permita determinar la fila
con mayor cantidad de números impares en una matriz.

    +------------------------------------------------------------+
    | M = [                                                      |
    |    [1, 2, 3, 4],                                           |
    |    [5, 7, 9, 10],                                          |
    |    [1, 4, 6],                                              |
    |    [2, 8, 10],                                             |
    | ]                                                          |
    | Output: La fila 1 tiene mayor cantidad de números impares. |
    +------------------------------------------------------------+

    +------------------------------------------------------------+
    | M = [                                                      |
    |    [1, 2, 3, 4],                                           |
    |    [5, 6, 7, 8],                                           |
    |    [10, 11, 12],                                           |
    |    [14, 15, 16],                                           |
    | ]                                                          |
    | Output: La fila 0 tiene mayor cantidad de números impares. |
    +------------------------------------------------------------+
"""
from typing import List
from unittest import main, TestCase


def contar_impares(arr: List[int]) -> int: # helper function
    """Determina la cantidad de números impares en una lista.

    :param arr: Lista de números enteros.
    :arr type: List[int]
    :return: Cantidad de números impares en la lista.
    :rtype: int
    """
    return len([x for x in arr if x % 2 != 0])


def mayor_fila(arr: List[List[int]], pos: int = 0) -> int:
    """Determina la fila con la mayor cantidad de números impares
    usando recursion.

    :param arr: Lista de números enteros.
    :arr type: List[List[int]]
    :param pos: Posición actual en la lista.
    :pos type: int
    :return: Fila con la mayor cantidad de números impares.
    :rtype: int
    """
    if len(arr) - 1 == pos:
        return pos
    i = mayor_fila(arr, pos+1)
    if contar_impares(arr[i]) > contar_impares(arr[pos]):
        return i
    return pos


def main_():
    m = []
    n = int(input("Cantidad de filas: "))
    print("Ingresar elementos de cada fila separados por comas (,)")
    print("Ejemplo: 1, 2, 3, 4\n")
    for i in range(n):
        m.append([int(x) for x in input("Fila {}: ".format(i)).split(",")])
    print(f"\nM = [")
    for fila in m:
        print(f"  {fila},")
    print(f"]")
    print(
        f"Output: La fila {mayor_fila(m)}"
        f" tiene mayor cantidad de números impares."
    )


class Test(TestCase):

    def test_mayor_fila(self):
        self.assertEqual(
            mayor_fila([
                [1, 2, 3, 4,],
                [5, 7, 9, 10, 3, 3, 3, 3],
                [1, 4, 6],
                [8, 7, 1, 3, 5],
            ]),
            1
        )
        self.assertEqual(
            mayor_fila([
                [1, 2, 3, 4],
                [5, 7, 9, 10],
                [1, 4, 6],
                [2, 8, 10],
            ]),
            1
        )
        self.assertEqual(
            mayor_fila([
                [1, 2, 4],
                [5, 6, 8],
                [11, 13, 15],
                [14, 16, 18],
            ]),
            2
        )
        self.assertEqual(
            mayor_fila([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [10, 11, 12],
                [14, 15, 16],
            ]),
            0
        )


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run tests
    main_()