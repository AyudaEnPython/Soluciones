"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir una función que genere una lista de números enteros aleatorios
(debe ingresar el número de valores a generar) y que devuelva las
siguientes salidas: Una lista ordenada con los números pares, una lista
ordenada con los números impares y la cantidad de cada lista final.
"""
from random import randint
from typing import List


def generar_aleatorios(
    size: int,
    min: int = 1,
    max: int = 100,
) -> List[int]:
    return [randint(min, max) for _ in range(size)]


def obtener_pares(xs: List[int]) -> List[int]:
    return sorted([x for x in xs if x % 2 == 0])


def obtener_impares(xs: List[int]) -> List[int]:
    return sorted([x for x in xs if x % 2 != 0])


def main():
    n = int(input("Cantida de números: "))
    numeros = generar_aleatorios(n)
    pares = obtener_pares(numeros)
    impares = obtener_impares(numeros)
    print("Numeros pares:", *pares)
    print(f"Cantidad de pares: {len(pares)}")
    print("Numeros impares:", *impares)
    print(f"Cantidad de impares: {len(impares)}")


if __name__ == "__main__":
    main()
