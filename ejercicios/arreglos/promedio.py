"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar 5 notas de un estudiante en un vector, calcular el promedio y
mostrar cual es la calficación más alta con su posición, la más baja
del grupo con su posición y cuantas notas son superior al promedio del
grupo.

Notas
+-----+-----+-----+-----+
| 4.0 | 4.5 | 3.0 | 5.0 |
+-----+-----+-----+-----+

Promedio = 4.12
Calificación más alta : 5.0 Posición = 3
Calificación más baja : 3.0 Posición = 1
Notas superior al promedio = 2
"""
from typing import Callable, List, Tuple
# pip install prototools
from prototools import show_matrix, float_input

Vector = List[float]
SIZE = 4


def promedio(data: Vector) -> float:
    return sum(data) / len(data)


def superior_promedio(data: Vector) -> float:
    return len([nota for nota in data if nota > promedio(data)])


def helper(data: Vector, f: Callable) -> Tuple[float, int]:
    return f(data), data.index(f(data))


def main():
    notas = [float_input(f"Nota[{i}] -> ") for i in range(1, SIZE+1)]
    print("Notas")
    show_matrix(notas, index=True)
    print(f"Promedio = {promedio(notas)}")
    min_, max_ = helper(notas, min), helper(notas, max)
    for (x, y), z in zip((max_, min_), ("alta", "baja")):
        print(f"Calificación más {z} : {x} Posición = {y}")
    print(f"Notas superior al promedio = {superior_promedio(notas)}")


if __name__ == "__main__":
    main()
