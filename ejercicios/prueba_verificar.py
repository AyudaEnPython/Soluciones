"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realiza un programa que almacene en una lista las respuestas de 10
preguntas de una prueba cierto y falso, en otra lista la respuesta de
un alumno. Mostrar el número de respuestas correctas e incorrectas y la
nota final sabiendo que cada respuesta correcta tiene un valor de 2
puntos.
"""
from typing import List, Optional
from unittest import main, TestCase


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
    return sum(puntos if r == a else 0 for r, a in zip(respuestas, alumno))


def main_():
    respuestas = [True, False, True, False, True, True, False, True, False, False]
    alumno     = [True, False, True, True, False, True, False, False, False, False]

    nota = calcular_nota(respuestas, alumno)
    print(f"Nota: {nota}")


class Test(TestCase):
    
    def test_calcular_nota(self):
        self.assertEqual(
            calcular_nota(
                [True, False, True, False, True, True, False, True, False, False],
                [True, False, True, True, False, True, False, False, False, False]
            ),
            14
        )
        self.assertEqual(
            calcular_nota(
                [True, False, True, False, True, True, False, True, False, False],
                [True, False, True, False, True, True, False, True, False, False],
            ),
            20
        )
        self.assertEqual(
            calcular_nota(
                [True, False, True, False, True, True, False, True, False, False],
                [False, True, False, True, False, False, True, False, True, True],
            ),
            0
        )


if __name__ == '__main__':
    main()