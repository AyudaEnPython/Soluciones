"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una lista de nombres de alumnos:

    +---------------------------------------------------------------+
    | alumnos = ["Ana", "Luis", "Pedro", "Maria", "Nerea", "Pablo"] |
    +---------------------------------------------------------------+

Usando listas de comprensión implementa un programa que cree una lista
con las iniciales de cada nombre.

    +-------------------------------------------+
    | respuesta: ["A", "L", "P", "M", "N", "P"] |
    +-------------------------------------------+
"""
import unittest
from typing import List

alumnos = ["Ana", "Luis", "Pedro", "Maria", "Nerea", "Pablo"]


def solver(alumnos: List[str]) -> List[str]:
    """Devuelve las iniciales de cada nombre.

    :param alumnos: Lista de nombres de alumnos
    :alumnos type: List[str]
    :return: Lista con las iniciales de cada nombre
    :return type: List[str]
    """
    return [s[0] for s in alumnos]


def main():
    print("respuesta: ", solver(alumnos))


class Test(unittest.TestCase):

    def test_solver(self):
        self.assertEqual(solver(alumnos), ["A", "L", "P", "M", "N", "P"])
        self.assertEqual(solver(["Pedro", "Paco", "Luis"]), ["P", "P", "L"])
        self.assertEqual(
            solver(["Paul", "Ringo", "George", "John"]),
            ["P", "R", "G", "J"]
        )


if __name__ == "__main__":
    # unittest.main()
    main()
