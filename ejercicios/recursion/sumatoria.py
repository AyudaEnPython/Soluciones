"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algoritmo, usando una función recursiva, que resuelva la
siguiente sumatoria:

    K(n, p) = p + 2*p + 3*p + 4*p + ... + n*p

- El programa debe pedir al usuario que ingrese un número n, y un
    número d.
- Luego debe calcular el valor de K(n, p) usando una función recursiva.
- Debe imprimir el resultado de K(n, p).

Algunos ejemplos del diálogo de este programa serían:

    +-----------------------------------------+
    | Input n: 5                              |
    | Input p: 2                              |
    | Output: 30                              |
    +-----------------------------------------+

    +-----------------------------------------+
    | Input n: 6                              |
    | Input p: 3                              |
    | Output: 63                              |
    +-----------------------------------------+
"""
import unittest
# pip install prototools
from prototools import int_input


def K(n: int, p: int) -> int:
    if n == 1:
        return p
    else:
        return n*p + K(n-1, p)


def main():
    n = int_input("Input n: ")
    p = int_input("Input p: ")
    print(f"Output: {K(n, p)}")


class Test(unittest.TestCase):

    def test_K(self):
        self.assertEqual(K(5, 2), 30)
        self.assertEqual(K(6, 3), 63)


if __name__ == '__main__':
    # unittest.main()
    main()
