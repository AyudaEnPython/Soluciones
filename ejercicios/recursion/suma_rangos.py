"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir una función recursiva que reciba como input dos números y
devuelva como resultado la suma de todos los números desde el inicio
del rango (número menor) hasta el final del rango (número mayor).

Ejemplos:

    +-----------------------------------------+
    | Ingrese un número: 30                   |
    | Ingrese un número: 35                   |
    | Resultado: 195                          |
    +-----------------------------------------+

    +-----------------------------------------+
    | Ingrese un número: 51                   |
    | Ingrese un número: 25                   |
    | Resultado: 1026                         |
    +-----------------------------------------+

"""
import unittest
# pip install prototools
from prototools import int_input


def suma(a: int, b: int) -> int:
    """Suma los números desde el inicio del rango (número menor) hasta
    el final del rango (número mayor).

    :param a: Número menor.
    :a type: int
    :param b: Número mayor.
    :b type: int
    :return: Suma de los números.
    :rtype: int
    """
    if a > b:
        b, a = a, b
    if a == b:
        return a
    else:
        return a + suma(a + 1, b)


def main():
    a = int_input("Ingrese un número: ")
    b = int_input("Ingrese un número: ")
    print(f"Resultado: {suma(a, b)}")


class Test(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(30, 35), 195)
        self.assertEqual(suma(51, 25), 1026)


if __name__ == "__main__":
    # unittest.main()
    main()
