"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un arreglo bidimensional que solicite el tamaño de la matriz y
los números. Calcule el total de las filas, el total de las columnas y
el total de toda la matriz.
"""
from typing import List


def total_columnas(matriz, x: int) -> int:
    return sum(matriz[i][x] for i in range(len(matriz)))


def total_filas(matriz, x: int) -> int:
    return sum(matriz[x][i] for i in range(len(matriz[0])))


def total_matriz(matriz) -> int:
    return sum(sum(
        matriz[i][j] for i in range(len(matriz)))
        for j in range(len(matriz[0])
    ))


def ingresar_numeros(n: int, m: int) -> List[List[int]]:
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(int(input(f"matriz[{i}][{j}] -> " )))
    return matriz


def main():
    n = int(input("Cantidad de filas: "))
    m = int(input("Cantidad de columnas: "))
    matriz = ingresar_numeros(n, m)
    for i in range(n):
        print(f"Total de fila {i} = {total_filas(matriz, i)}")
    for j in range(m):
        print(f"Total de columna {j} = {total_columnas(matriz, j)}")
    print(f"Total de la matriz = {total_matriz(matriz)}")


if __name__ == "__main__":
    main()
