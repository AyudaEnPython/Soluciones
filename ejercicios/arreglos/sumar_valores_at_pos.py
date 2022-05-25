"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Construya una función que admita el ingreso de dos tuplas de distinto
tamaño y con valores reales y permita sumar los valores, que
correspondan a a la misma posición. La posición será ingresada por
teclado.

Aclaración: Si la posición no existe en alguna de las tuplas se emitirá
el mensaje "Error, elemento inexistente".
"""
from typing import Tuple
# pip install prototools
from prototools import int_input

Data = Tuple[float, ...]


def sol(position: int, x: Data, y: Data) -> float:
    try:
        return x[position] + y[position]
    except IndexError:
        return "Error, elemento inexistente"


def main():
    x = (1.0, 2.0, 3.0, 4.0)
    y = (5.0, 6.0, 7.0, 8.0, 9.0)
    pos = int_input("Ingrese la posición: ")
    print(sol(pos, x, y))


if __name__ == "__main__":
    main()
