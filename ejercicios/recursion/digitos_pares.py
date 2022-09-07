"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe e implemente un algoritmo recursivo que permita contar cuántos
dígitos pares hay en un número entero. Considere que el cer es par.

Algunos ejemplos de diálogo de este programa serían:

    +-----------------------------------------+
    | Input: 123456                           |
    | Output: 3                               |
    +-----------------------------------------+

    +-----------------------------------------+
    | Input: 111                              |
    | Output: 0                               |
    +-----------------------------------------+

    +-----------------------------------------+
    | Input: 2220                             |
    | Output: 4                               |
    +-----------------------------------------+
"""
import unittest
# pip install prototools
from prototools import int_input


def contar_digitos_pares(n: int) -> int:
    """Cuenta los dígitos pares de un número entero.

    :param n: número entero
    :n type: int
    :return: cantidad de dígitos pares
    :rtype: int
    """
    if n < 10:
        return 1 if n % 2 == 0 else 0
    if n % 10 % 2 == 0:
        return 1 + contar_digitos_pares(n // 10)
    else:
        return contar_digitos_pares(n // 10)


def main():
    n = int_input('Ingrese un número entero: ')
    print(f"Input: {n}")
    print(f"Output: {contar_digitos_pares(n)}")


class Test(unittest.TestCase):

    def test_contar_digitos_pares(self):
        self.assertEqual(contar_digitos_pares(101), 1)
        self.assertEqual(contar_digitos_pares(100), 2)
        self.assertEqual(contar_digitos_pares(123456), 3)
        self.assertEqual(contar_digitos_pares(2220), 4)
        self.assertEqual(contar_digitos_pares(111), 0)
        self.assertEqual(contar_digitos_pares(22), 2)
        self.assertEqual(contar_digitos_pares(0), 1)
        self.assertEqual(contar_digitos_pares(1), 0)


if __name__ == "__main__":
    # unittest.main()
    main()
