"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolle una función que reciba tres argumentos: una lista
de nombres, una de notas y un parámetro de umbral f.
Evaluar las notas mayores de f y retornar dos listas: nombres
y notas de las que coincidieron. Además, el promedio de las
notas que superaron el umbral.
"""
from typing import List, Tuple
from unittest import main, TestCase

data =  Tuple[List[str], List[int], float]


def evaluar(nombres: List[str], notas: List[int], umbral: int) -> data:
    """Evalúa las notas que superan el umbral.

    :param nombres: Lista de nombres.
    :nombres type: List[str]
    :param notas: Lista de notas.
    :notas type: List[int]
    :param umbral: Umbral.
    :umbral type: int
    :return: Tupla listas de nombres y notas que superan el umbral.
    :rtype: Tuple[List[str], List[int], float]
    """
    notas_, nombres_ = [], []
    for i, nota in enumerate(notas):
        if nota >= umbral:
            notas_.append(nota)
            nombres_.append(nombres[i])
    promedio = sum(notas_) / len(notas_)
    return nombres_, notas_, promedio


class Test(TestCase):

    nombres = ["John", "Paul", "George", "Ringo"]
    notas = [6, 9, 10, 7]
    umbral = 9

    def test_evaluar(self):
        self.assertEqual(
            evaluar(self.nombres, self.notas, self.umbral),
            (["Paul", "George"], [9, 10], 9.5),
        )


if __name__ == '__main__':
    main()
