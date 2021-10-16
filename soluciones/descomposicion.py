"""
Diseñe e implemente un algoritmo que imprima todas las posibles
descomposiciones de un número natural como suma de números menores
que él.

1 = 1
2 = 1 + 1
3 = 2 + 1
3 = 1 + 1 + 1
4 = 3 + 1
4 = 2 + 1 + 1
4 = 2 + 2
4 = 2 + 1 + 1
4 = 1 + 1 + 1 + 1
N = (n-1) + 1
N = (n-2) + 2 = (n-2) + 1 + 1

TODO: add more implementations and testcases
"""
from typing import List


def descomponer_r(n):
    if n <= 1:
        return f"{n}"
    else:
        #print(f"{descomponer_r(n-1)} + {descomponer_r(n-2)}")
        return f"{descomponer_r(n-1)} + 1"


def _combinaciones(arr: List[int], idx: int, n: int, r: int) -> None:
    """Funcion helper para hallar todas las combinaciones.

    :param arr: Arreglo
    :arr type: list
    :param idx: Indice
    :idx type: int
    :param n: Número
    :n type: int
    :param r: Número reducido
    :r type: int
    """
    if r < 0:
        return
    if r == 0:
        t = f"{str(n)} = "
        for i in range(idx):
            t += f"{str(arr[i])} + "
        print(t[:-2])
        return
    prev = 1 if (idx == 0) else arr[idx - 1]
    for k in range(prev, n+1):
        arr[idx] = k
        _combinaciones(arr, idx+1, n, r-k)


def descomponer(n: int) -> None:
    arr = [0] * n
    _combinaciones(arr, 0, n, n)


def main():
    descomponer(5)


if __name__ == "__main__":
    main()