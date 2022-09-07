"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolle un programa que lea como dato un número "n" mayor a 10 y
luego genere de manera aleatorio una lista con "n" números cuyo rango
de valores estén entre 1 y 99.

Luego permita al usuario leer el dato a buscar y a través del algoritmo
de la búsqueda binaria determine si el dato se encuentra o no en la
lista.

Diseñe el programa usando funciones.
"""
from random import randint
from typing import List

MIN, MAX = 1, 99


def binary_search(arr: List[int], x: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        else:
            if x in arr[mid:]:
                low = mid + 1
            elif x in arr[0:mid-1]:
                high = mid - 1
            else:
                return -1


def generar_aleatorios(n: int, min_: int = MIN, max_: int = MAX) -> List[int]:
    return [randint(min_, max_) for _ in range(n+1)]


# def generar_aleatorios(
#     n: int, min_: int = MIN, max_: int = MAX
# ) -> List[int]:
#     aleatorios = []
#     for _ in range(n+1):
#         aleatorios.append(randint(min_, max_))
#     return aleatorios


def ingresar_n(msg: str) -> int:
    while True:
        try:
            n = int(input(msg))
            if n >= 10:
                return n
            else:
                print("El número debe ser mayor a 10")
        except ValueError:
            print("Debe ingresar un número")


def main():
    N = ingresar_n("Cantidad de elementos: ")
    data = generar_aleatorios(N)
    n = int(input("> "))
    idx = binary_search(data, n)
    if idx == -1:
        print(f"No se encuentra {n}")
    else:
        print(f"{n} se encuentra en la posición {idx}")


if __name__ == "__main__":
    main()
