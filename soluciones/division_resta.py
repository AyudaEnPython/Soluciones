"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Crear una aplicacion para resolver el siguiente problema:

Pedir 2 numeros: en el cual el 2do numero deber ser diferente de 0
numero1 = 12
numero2 = 3

A través de una estructura repetitiva resuelva el problema de la
división con restas sucesivas:

    +---------+---------+---------+---------+
    | numero1 | numero2 | numero1 | numero2 |
    +---------+---------+---------+---------+
    |    12   |    3    |    7    |    3    |
    |     9   |    3    |    4    |    3    |
    |     6   |    3    |    1    |         |
    |     3   |    3    |         |         |
    |     0   |         |         |         |
    +---------+---------+---------+---------+

el resultado de esto:    4     2
el residuo es :          0     1
# ---------------------------------------------------------------------
"""
import unittest
from typing import Tuple


def solver(a: int, b: int) -> Tuple[int, int]:
    i = 0
    while a >= b:
        a -= b
        i += 1
    return i, a


def ingresar_numeros() -> Tuple[int, int]:
    a = int(input("Ingrese el primer numero: "))
    while True:
        try:
            b = int(input("Ingrese el segundo numero: "))
            if b != 0:
                break
            else:
                print("El segundo numero no puede ser 0")
        except ValueError:
            print("El segundo numero debe ser un entero")
    return a, b


def main():
    a, b = ingresar_numeros()
    resultado, residuo = solver(a, b)
    print(f"El cociente: {resultado}")
    print(f"El residuo es: {residuo}")


class Test(unittest.TestCase):

    def test_solver(self):
        self.assertEqual(solver(12, 3), (4, 0))
        self.assertEqual(solver(7, 3), (2, 1))


if __name__ == "__main__":
    # unittest.main()  # uncomment/comment to run tests
    main()
