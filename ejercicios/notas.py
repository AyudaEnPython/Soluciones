"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algoritmo que solicite al usuario ingresar las notas de
las prácticas calificadas. Se termina de ingresar con un número
negativo y debe crear e imprimir un diccionario con los siguientes
cálculos:

- Cantidad de notas
- Cantidad de notas mayores e iguales a 11
- Cantidad de notas menores a  11
- Promedio de notas

Algunos ejemplos de diálogo de este programa serían:

    +---------------------------+
    | Nota 1: 12                |
    | Nota 2: 10                |
    | Nota 3: 6                 |
    | Nota 4: 15                |
    | Nota 5: 11                |
    | Nota 6: -1                |
    |                           |
    | Cantidad de notas: 5      |
    | Mayores a 11: 3           |
    | Menores a 11: 2           |
    | Promedio: 10.8            |
    +---------------------------+

NOTE: Se opta por añadir un control errores para el rango de notas.
"""
from typing import Dict, List 
from unittest import main, TestCase
# ejercicio similar a 
# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/aprobados_desaprobados.py


def ingresar_notas(min_: int = 0, max_: int = 20) -> List[int]:
    """Pide al usuario las notas de las prácticas.

    :param min_: Valor mínimo de la nota.
    :min type: int
    :param max_: Valor máximo de la nota.
    :max type: int
    :return: Lista con las notas.
    :rtype: List[int]
    """
    notas = []
    i = 1
    while True:
        try:
            nota = int(input(f'Nota {i}: '))
            if nota < 0:
                break
            if min_ <= nota <= max_:
                notas.append(nota)
                i += 1
            else:
                print('Nota fuera de rango')
        except ValueError:
            print('La nota debe ser un número.')
            continue
    return notas


def resultados(arr: List[int]) -> Dict[str, float]:
    """Devuelve un diccionario con los resuldatos de la notas.

    :param arr: Lista con las notas.
    :arr type: List[int]
    :return: Diccionario con los resultados.
    :rtype: Dict[str, float]
    """
    llaves = ("cantidad", "mayores", "menores", "promedio")
    return {
        k:v for k, v in zip(
            llaves, (
                len(arr),
                len(list(filter(lambda x: x >= 11, arr))),
                len(list(filter(lambda x: x < 11, arr))),
                sum(arr) / len(arr)
            )
        )
    }


def main_():
    notas = ingresar_notas()
    datos = resultados(notas)
    print(f"\nCantidad de notas: {datos['cantidad']}")
    print(f"Mayores a 11: {datos['mayores']}")
    print(f"Menores a 11: {datos['menores']}")
    print(f"Promedio: {datos['promedio']}")


class Test(TestCase):

    data = [12, 10, 6, 15, 11]

    def test_resultados(self):
        self.assertEqual(resultados(self.data), {
            "cantidad": 5,
            "mayores": 3,
            "menores": 2,
            "promedio": 10.8
        })


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run tests
    main_()