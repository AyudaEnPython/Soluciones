"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe e implemente un algoritmo que calcule la suma de cubos de los
dígitos de un número divisible por 3. Para ello, ingrese un número
entero y determine si es divisible por 3. En caso no lo sea, pida otro
número que sea divisible por 3 hasta que se ingrese uno correcto. Luego
calcule la suma de cubos de los dígitos del número ingresado.
A continuación, calcule la suma de cubos de los dígitos del resultado
anterior. Continúe con el procedimiento hasta que el cálculo sea igual
a 153.
¿Qué observa en el resultado?
E.g., para el número 333:

    +---------------------------------------+
    | Ingres un número: 333                 |
    | La suma de cubos de 333 es: 81        |
    | La suma de cubos de 81 es: 513        |
    | La suma de cubos de 513 es: 153       |
    | La suma de cubos de 153 es: 153       |
    +---------------------------------------+

"""
from unittest import main, TestCase

# > pip install prototools
from prototools import int_input


def es_divisible(a: int, b: int) -> bool:
    """Comprueba si un número 'a' es divisible por un número 'b'

    :param a: Número a evaluar
    :a type: int
    :param b: Divisor
    :b type: int
    :return: True si es divisible, False de lo contrario
    :rtype: bool
    """
    return True if a % b == 0 else False


def suma_de_cubos(n: int) -> int:
    """Calcula la suma de cubos de los dígitos recursivamente

    :param n: Número a calcular
    :n type: int
    :return: Suma de cubos de los dígitos del número
    :rtype: int
    """
    r = sum([int(x)**3 for x in str(n) if es_divisible(n, 3)])
    print(f"La suma de cubos de {n} es: {r}")
    if r != 153:
        return suma_de_cubos(r)
    print(f"La suma de cubos de {r} es: {r}")
    return r


def calcular(): # it uses int_input from prototools library
    while True:
        n = int_input("Ingresar un número: ")
        if es_divisible(n, 3):
            break
        print("Ingresar un número divisible entre 3")
    suma_de_cubos(n)


class Test(TestCase):

    def test_divisibilidad(self):
        self.assertEqual(es_divisible(333, 3), True)
        self.assertEqual(es_divisible(81, 3), True)
        self.assertEqual(es_divisible(513, 3), True)
        self.assertEqual(es_divisible(153, 3), True)
        self.assertEqual(es_divisible(100, 3), False)
        self.assertEqual(es_divisible(1010, 3), False)
        self.assertEqual(es_divisible(17, 3), False)
        self.assertEqual(es_divisible(13, 13), True)
        self.assertEqual(es_divisible(25, 5), True)

    def test_suma_de_cubos(self):
        self.assertEqual(suma_de_cubos(333), 153)
        self.assertEqual(suma_de_cubos(102), 153)
        self.assertEqual(suma_de_cubos(999), 153)


if __name__ == "__main__":
    main()