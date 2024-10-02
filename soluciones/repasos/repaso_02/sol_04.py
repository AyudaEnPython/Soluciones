from copy import deepcopy
from random import randint
from typing import List, Tuple, Union

Matrix = List[List[int]]
MatrixNA = List[List[Union[int, str]]]
Vector = List[int]
Position = Tuple[int, int]


def generar_matriz(r: int, c: int) -> Matrix:
    return [[randint(-10, 10) for _ in range(c)] for _ in range(r)]


def encontrar_maximo(m: Matrix) -> Tuple[int, Position]:
    max_valor = float("-inf")
    max_pos = 0, 0
    for i, r in enumerate(m):
        for j, v in enumerate(r):
            if v > max_valor:
                max_valor = v
                max_pos = i, j
    return max_valor, max_pos


def maximos_por_col(m: Matrix) -> Vector:
    return [max(c) for c in zip(*m)]


def generar_matriz_pares(m: Matrix) -> MatrixNA:
    return [[x if x % 2 == 0 else "NA" for x in r] for r in m]


def columna_con_mas_negativos(m: Matrix) -> Tuple[int, int]:
    negativos = [sum(1 for r in m if r[j] < 0) for j in range(len(m[0]))]
    maximos = max(negativos)
    col_idx = negativos.index(maximos)
    return col_idx, maximos


def intercambiar_cols(m: Matrix) -> Matrix:
    if not m or len(m[0]) < 2:
        return deepcopy(m)
    m_ = deepcopy(m)
    for r in m_:
        r[0], r[-1] = r[-1], r[0]
    return m_


def mostrar_matriz(m: Union[Matrix, MatrixNA], titulo: str = "") -> None:
    if titulo:
        print(f"{titulo}")
    for r in m:
        print("[" + "".join(f"{str(x):^5}" for x in r) +"]")


def main():
    N, M = 3, 4
    A = generar_matriz(N,  M)
    mostrar_matriz(A, "Matriz A original:")
    max_valor, (max_r, max_c) = encontrar_maximo(A)
    print(f"\nMáximo elemento: {max_valor} | Posición: ({max_r}, {max_c})")
    maximos = maximos_por_col(A)
    print(f"Maximos por columna: {maximos}")
    B = generar_matriz_pares(A)
    mostrar_matriz(B, "\nMatriz B (impares reemplazados por NA):")
    col_idx, negativos = columna_con_mas_negativos(A)
    print(f"\nMayor cantidad de números negativos en la columna: {col_idx}")
    print(f"cantidad de números negativos: {negativos}")
    mostrar_matriz(intercambiar_cols(A), "\nMatriz A (Columnas intercambiadas)")


if __name__ == "__main__":
    main()
