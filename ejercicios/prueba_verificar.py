"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realiza un programa que almacene en una lista las respuestas de 10
preguntas de una prueba cierto y falso, en otra lista la respuesta de
un alumno. Mostrar el número de respuestas correctas e incorrectas y la
nota final sabiendo que cada respuesta correcta tiene un valor de 2
puntos.
"""
import unittest
from typing import List, Optional


def calcular_nota(
    respuestas: List[bool],
    alumno: List[bool],
    puntos: Optional[int] = 2,
) -> int:
    """Calcula la nota de un alumno.

    :param respuestas: Lista de respuestas.
    :respuestas type: List[bool]
    :param alumno: Lista de respuestas del alumno.
    :alumno type: List[bool]
    :return: Nota del alumno.
    :rtype: int
    """
    nota = correctas = incorrectas = 0
    for r, a in zip(respuestas, alumno):
        if r == a:
            correctas += 1
            nota += puntos
        else:
            incorrectas += 1
    return correctas, incorrectas, nota


def main():
    respuestas = [
        True, False, True, False, True, True, False, True, False, False
    ]
    alumno = [
        True, False, True, True, False, True, False, False, False, False
    ]
    correctas, incorrectas, nota = calcular_nota(respuestas, alumno)
    print(f"Correctas: {correctas}")
    print(f"Incorrectas: {incorrectas}")
    print(f"Nota: {nota}")


class Test(unittest.TestCase):

    def test_calcular_nota(self):
        self.assertEqual(
            calcular_nota(
                [
                    True, False, True, False, True,
                    True, False, True, False, False,
                ],
                [
                    True, False, True, True, False,
                    True, False, False, False, False,
                ]
            ),
            (7, 3, 14),
        )
        self.assertEqual(
            calcular_nota(
                [
                    True, False, True, False, True,
                    True, False, True, False, False,
                ],
                [
                    True, False, True, False, True,
                    True, False, True, False, False,
                ],
            ),
            (10, 0, 20),
        )
        self.assertEqual(
            calcular_nota(
                [
                    True, False, True, False, True,
                    True, False, True, False, False,
                ],
                [
                    False, True, False, True, False,
                    False, True, False, True, True,
                ],
            ),
            (0, 10, 0),
        )


if __name__ == '__main__':
    # unittest.main() # uncomment/comment to run the tests
    main()
