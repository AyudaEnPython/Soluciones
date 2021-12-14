"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Suma de N elementos de serie - recursividad

Diseñe una función recursiva sumaSerie(n) que calcule la suma de los
primeros n elementos de una serie (empezando por 1), donde el elemento
i de la serie viene determinado por la siguiente fórmula:

    E_i = i^3 + 5

Por lo tanto si n = 3, el resultado de la función sería:

    suma = (1^3 + 5) + (2^3 + 5) + (3^3 + 5) = 51

O el caso en que n = 4, el resultado de la función sería:

    suma = (1^3 + 5) + (2^3 + 5) + (3^3 + 5) + (4^3 + 5) = 120

NOTE: Se opta por cambiar el nombre de la función sumaSerie por
    suma_serie (PEP8).
"""
from unittest import main, TestCase


def suma_serie(n: int) -> int:
    """Suma los elementos de la serie E_i = i^3 + 5, desde 1 hasta n.
    
    :param n: número de elementos de la serie
    :n type: int
    :return: suma de los elementos de la serie
    :rtype: int
    """
    if n == 1:
        return 6
    else:
        return (n ** 3 + 5) + suma_serie(n - 1)


def main_():
    n = int(input("Input: "))
    print(f"Output: {suma_serie(n)}")


class Test(TestCase):

    def test_suma_serie(self):
        self.assertEqual(suma_serie(3), 51)
        self.assertEqual(suma_serie(4), 120)


if __name__ == "__main__":
    #main() # uncomment this line and comment the next one to run test
    main_()