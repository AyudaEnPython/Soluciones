"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import List


# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/generar_aleatorios.py
def generar_aleatorios(
    min: int = 1,
    max: int = 100,
    size: int = 20
) -> List[int]:
    return [randint(min, max) for _ in range(size)]


def main():
    n = int(input("Cantidad de números: "))
    numeros = generar_aleatorios(100, 251, n)
    print(sum(map(lambda x: x**2, numeros)))


if __name__ == "__main__":
    main()
