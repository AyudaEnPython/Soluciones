"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente una función para ordenar los datos que hay en una lista de
listas, con la siguiente estructura: Nombre, nota del curso 1 y nota
del curso 2; la función debe tomar dos parámetros: la lista de listas y
la columna por cual ordenar.

Un ejemplo de diálogo de este programa sería:

    +-----------------------------------+
    | datos = [                         |
    |     ["Maria", 14, 18],            |
    |     ["Kike", 11, 16],             |
    |     ["Roberto", 13, 14],          |
    |     ["Carlos", 12, 20],           |
    |     ["Jimena", 17, 15],           |
    |     ["Lucero", 17, 17],           |
    | ]                                 |
    +-----------------------------------+

Realice el siguiente proceso:

- Escriba la matriz de datos en el programa.
- Solicite al usuario que ingrese la columna por cual ordenar: Nombre,
    curso1, curso2.
- Ordenar los datos de forma ascendente, por la columna elegida.
- Imprimir los datos ordenados en forma de tabla.

Algunos ejemplos de diálogo de este programa serían:

    +-----------------------------------+
    | Ordenar por la columna: nombre    |
    | Carlos, 12, 20                    |
    | Jimena, 17, 15                    |
    | Kike, 11, 16                      |
    | Lucero, 17, 17                    |
    | Maria, 14, 18                     |
    | Roberto, 13, 14                   |
    +-----------------------------------+

    +-----------------------------------+
    | Ordenar por la columna: curso1    |
    | Kike, 11, 16                      |
    | Carlos, 12, 20                    |
    | Roberto, 13, 14                   |
    | Maria, 14, 18                     |
    | Jimena, 17, 15                    |
    | Lucero, 17, 17                    |
    +-----------------------------------+
"""
import unittest
from typing import List, Union

matrix = List[List[Union[str, int]]]
datos: matrix = [
    ["Maria", 14, 18],
    ["Kike", 11, 16],
    ["Roberto", 13, 14],
    ["Carlos", 12, 20],
    ["Jimena", 17, 15],
    ["Lucero", 17, 17],
]


def ordenar(arr: matrix, x: str) -> matrix:
    """Ordena los datos de forma ascendente por la columna elegida.

    :param arr: Lista de datos.
    :arr type: List[List[Union[str, int]]]
    :param x: Columna a seleccionar.
    :x type: int
    :return: Datos ordenados de forma ascendente.
    :rtype: List[List[Union[str, int]]]
    """
    col = {"nombre": 0, "curso1": 1, "curso2": 2}
    return sorted(arr, key=lambda y: y[col[x]])


def main():
    columna: str = input("Ordenar por la columna: ")
    resultado: matrix = ordenar(datos, columna)
    for fila in resultado:
        print(", ".join(str(x) for x in fila))


class Test(unittest.TestCase):

    def test_ordenar(self):
        self.assertEqual(
            ordenar(datos, "nombre"),
            [
                ["Carlos", 12, 20],
                ["Jimena", 17, 15],
                ["Kike", 11, 16],
                ["Lucero", 17, 17],
                ["Maria", 14, 18],
                ["Roberto", 13, 14],
            ]
        )
        self.assertEqual(
            ordenar(datos, "curso1"),
            [
                ["Kike", 11, 16],
                ["Carlos", 12, 20],
                ["Roberto", 13, 14],
                ["Maria", 14, 18],
                ["Jimena", 17, 15],
                ["Lucero", 17, 17],
            ]
        )


if __name__ == "__main__":
    # unittest.main() # uncomment/comment to run tests
    main()
