"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Suma de N elementos de serie - recursividad

Utilizando la misma formula del ejercicio anterior:

    E_i = i^3 + 5

Elabore una función que le permita construir de forma recursiva una
lista con los elementos de la serie de 1 hasta N. Algunos ejemplos de
diálogo de este programa serían (funcion sugerida):

    +------------------------------------------------------------+
    | lista = []                                                 |
    | listaSerie(lista, 1, 5)                                    |
    | print(lista) # [6, 13, 32, 69, 130]                        |
    +------------------------------------------------------------+                 

    +------------------------------------------------------------+
    | lista = []                                                 |
    | listaSerie(lista, 2, 10)                                   |
    | print(lista) # [13, 32, 69, 130, 221, 348, 517, 734, 1005] |
    +------------------------------------------------------------+

NOTE: Se opta por cambiar el nombre de la función y la variable (PEP8).
"""
from unittest import main, TestCase
from typing import List


def serie_recursiva(arr: List[int], a: int, b: int) -> List[int]:
    """Devuelve la serie E_i = i^3 + 5, desde 1 hasta n.
    
    :param arr: Lista vacía.
    :arr type: List[int]
    :param a: Inicio de la serie.
    :a type: int
    :param b: Fin de la serie.
    :b type: int
    :return: Arreglo con los elementos de la serie.
    :rtype: List[int]
    """
    if a > b:
        return arr
    arr.append(a**3 + 5)
    return serie_recursiva(arr, a+1, b)


def main_():
    serie = []
    a = int(input("Inicio de la serie: "))
    b = int(input("Fin de la serie: "))
    serie_recursiva(serie, a, b)
    print(f"Output: {serie}")


class Test(TestCase):

    def test_serie_recursiva(self):
        self.assertEqual(
            serie_recursiva([], 1, 5),
            [6, 13, 32, 69, 130]
        )
        self.assertEqual(
            serie_recursiva([], 2, 10),
            [13, 32, 69, 130, 221, 348, 517, 734, 1005]
        )


if __name__ == "__main__":
    #main() # uncomment this line and comment the next one to run test
    main_()