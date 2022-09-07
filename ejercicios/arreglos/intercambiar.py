"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Entrar valores númericos en 2 vectores de 10 posiciones e intercambiar
los vectores.

Vector 1 - Inicial
+-----+-----+-----+-----+-----+-----+
|  4  |  5  |  3  |  8  | ... | ... |
+-----+-----+-----+-----+-----+-----+

Vector 2 - Inicial
+-----+-----+-----+-----+-----+-----+
|  1  |  2  |  6  |  9  | ... | ... |
+-----+-----+-----+-----+-----+-----+

Después del intercambio, los vectores deben quedar así:

Vector 1 - Final
+-----+-----+-----+-----+-----+-----+
|  1  |  2  |  6  |  9  | ... | ... |
+-----+-----+-----+-----+-----+-----+

Vector 2 - Final
+-----+-----+-----+-----+-----+-----+
|  4  |  5  |  3  |  8  | ... | ... |
+-----+-----+-----+-----+-----+-----+
"""
from typing import List
# pip install prototools
from prototools import show_matrix, int_input

Vector = List[float]
SIZE = 10


def swap_values(m: Vector, n: Vector) -> None:
    for i in range(len(m)):
        m[i], n[i] = n[i], m[i]


def show(m: Vector, n: Vector, msg: str) -> None:
    for i, v in enumerate((m, n), 1):
        print(f"Vector {i} - {msg}")
        show_matrix(v)


def main():
    print("Vector 1")
    a = [int_input(f"Vector[{i}] ->") for i in range(SIZE)]
    print("Vector 2")
    b = [int_input(f"Vector[{i}] ->") for i in range(SIZE)]
    show(a, b, "Inicial")
    swap_values(a, b)
    show(a, b, "Final")


def main_alt():
    print("Vector 1")
    a = [int_input(f"Vector[{i}] ->") for i in range(SIZE)]
    print("Vector 2")
    b = [int_input(f"Vector[{i}] ->") for i in range(SIZE)]
    show(a, b, "Inicial")
    a[:], b[:] = b[:], a[:]  # a, b = b, a
    show(a, b, "Final")


if __name__ == "__main__":
    main()
    # main_alt()
