"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe e implemente un algoritmo recursivo que permita calcular la suma
de los elementos impares de una lista de números.

Algunos ejemplos de diálogo de este programa serían:

    +-----------------------------------------+
    | Input: [1, 2, 3, 4, 5]                  |
    | Output: 9                               |
    +-----------------------------------------+

    +-----------------------------------------+
    | Input: [1, 1, 1, 1, 1, 1]               |
    | Output: 6                               |
    +-----------------------------------------+
"""
from unittest import main, TestCase
from typing import List


def suma_impares(arr: List[int]) -> int:
    if len(arr) == 0:
        return 0
    if arr[0] % 2 == 1:
        return arr[0] + suma_impares(arr[1:])
    return suma_impares(arr[1:])


def main_():
    a = [1, 2, 3, 4, 5]
    print("Input:", a)
    print("Output:", suma_impares(a))
    b = [1, 1, 1, 1, 1, 1]
    print("Input:", b)
    print("Output:", suma_impares(b))


class Test(TestCase):

    def test_suma_impares(self):
        self.assertEqual(suma_impares([1, 2, 3, 4, 5]), 9)
        self.assertEqual(suma_impares([1, 1, 1, 1, 1, 1]), 6)
        self.assertEqual(suma_impares([]), 0)
        self.assertEqual(suma_impares([2, 4, 6, 8]), 0)
        self.assertEqual(suma_impares([1, 3, 5, 7]), 16)


if __name__ == "__main__":
    #main() # uncomment this line and comment the next one to run test
    main_()