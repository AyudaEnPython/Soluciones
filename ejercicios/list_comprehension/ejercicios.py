"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Los siguientes problemas resolverlos con listas por compresión.

- Implementar una función llamada funcion1 que reciba como parámetro un
    texto, y devuelva en una lista las palabras contenidas del texto.

- Implementar una función llamada funcion2 que reciba como parámetro
    una matriz, su número de columnas, su número de filas y un número n
    y devuelva 2 listas conteniendo los elementos mayores a n y la otra
    lista los elementos menores a n.

- Implementar una función llamada funcion3 que reciba como parámetro
    dos listas de números enteros (lista A y lista B) y devuelva la
    intersección de esas listas.

Algunos ejemplos de diálogo de este programa serían:

    >>> funcion1('hola como estas')
    ['hola', 'como', 'estas']
    >>> funcion1('A quien madruga Dios lo ayuda')
    ['A', 'quien', 'madruga', 'Dios', 'lo', 'ayuda']
    >>> funcion2([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3, 5)
    ([1, 2, 3, 4], [6, 7, 8, 9])
    >>> funcion2([[10, 2, 13], [14, 15, 8], [9, 21, 23], [7, 18, 46]], 3, 4, 20)
    ([10, 2, 13, 14, 15, 8, 9, 7, 18], [21, 23, 46])
    >>> funcion3([1, 2, 3, 4, 5], [10, 4, 5, 6])
    [4, 5]

# ---------------------------------------------------------------------
Nota: El enunciado no esta bien redactado, la funcion2 no necesita el
    numero de filas ni columnas.
"""
from typing import List
from unittest import main, TestCase


def funcion1(s: str) -> List[str]:
    return s.split()


def funcion2(m: List[List[int]], n: int) -> List[List[int]]:
    menores = [x for fila in m for x in fila if x < n]
    mayores = [x for fila in m for x in fila if x > n]
    return menores, mayores


def funcion3(a: List[int], b: List[int]) -> List[int]:
    return [x for x in a if x in b]


class Test(TestCase):

    def test_funcion1(self):
        self.assertEqual(
            funcion1(
                'hola como estas'),
                ['hola', 'como', 'estas'],
            )
        self.assertEqual(
            funcion1(
                'A quien madruga Dios lo ayuda'),
                ['A', 'quien', 'madruga', 'Dios', 'lo', 'ayuda'],
            )
    
    def test_funcion2(self):
        self.assertEqual(
            funcion2(
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5),
                ([1, 2, 3, 4], [6, 7, 8, 9],
                )
            )
        self.assertEqual(
            funcion2(
                [[10, 2, 13], [14, 15, 8], [9, 21, 23], [7, 18, 46]], 20),
                ([10, 2, 13, 14, 15, 8, 9, 7, 18], [21, 23, 46],
                )
            )

    def test_funcion3(self):
        self.assertEqual(funcion3([1, 2, 3, 4, 5], [10, 4, 5, 6]), [4, 5])


if __name__ == '__main__':
    main()