"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un algoritmo que permita leer 15 números en un arreglo, que
pregunte si se desea introducir un nuevo número en lugar de cualquiera
de los que están en el arreglo; entonces leer el número a introducir y
el lugar del elemento por el que se cambiará, hacer el cambio e
imprimir el arreglo antes y después del cambio.
"""
from typing import List

N = 4


def get_array() -> List[int]:
    arr = [0] * N
    for i in range(N):
        arr[i] = int(input(f"Ingrese el elemento {i+1}: "))
    return arr


def modificar(arr: List[int]) -> List[int]:
    t = [e for e in arr]
    nuevo = int(input("Nuevo elemento > "))
    idx = int(input("Posicion > "))
    t[idx-1] = nuevo
    return t


def main():
    arr = get_array()
    print("Introducir un nuevo elemento? (s/n)")
    opcion = input("Opcion > ").lower()
    if opcion == "s":
        n_arr = modificar(arr)
        print("Arreglo original:")
        print(arr)
        print("Arreglo modificado:")
        print(n_arr)
    else:
        print("No se realizaron cambios")
        print("Arreglo:")
        print(arr)


if __name__ == "__main__":
    main()
