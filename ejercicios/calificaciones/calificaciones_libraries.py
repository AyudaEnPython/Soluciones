"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
# pip install prototools
from prototools import int_input, main_loop

PESOS = 0.1, 0.5, 0.4


def promediar(notas: List[int]) -> float:
    return sum(map(lambda x, y: x * y, notas, PESOS))


def main():
    nombre = input("Ingrese nombre: ")
    notas = [int_input("Ingrese nota: ", min=0, max=10) for _ in range(3)]
    print(f"{nombre} tiene una nota de {promediar(notas)}")


if __name__ == "__main__":
    main_loop(main)