"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un entrenador debe analizar si un atleta es apto para una carrera de 5
kms. Para ello, digita los datos promedio de 10 carreras en un vector.
El atleta es apto si:
a. No hay registro superior a 18 minutos
b. El promedio de las carreras es de 15 minutos o menos.

Ejemplo 1
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|  6  |  4  |  2  |  7  |  1  |  3  | 19  | ... | ... | ... |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
Apto ?

Ejemplo 2
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|  6  |  4  |  2  |  7  |  1  |  3  | 9   | ... | ... | ... |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
Apto ?
"""
from typing import List
# pip install prototools
from prototools import show_matrix, int_input

Vector = List[float]
SIZE = 10


def promedio(data: Vector) -> float:
    return sum(data) / len(data)


def es_apto(data: Vector) -> bool:
    return all(map(lambda x: x <= 18, data)) and promedio(data) <= 15


def main():
    registro = [int_input(f"Carrera [{i}] -> ") for i in range(1, SIZE+1)]
    show_matrix(registro)
    if es_apto(registro):
        print("Apto")
    else:
        print("No apto")


if __name__ == "__main__":
    main()
