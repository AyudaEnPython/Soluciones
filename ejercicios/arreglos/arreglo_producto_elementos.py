"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un algoritmo que permita leer un vector de 10 números en un
arreglo A de 10 elementos, lo mismo para un arreglo B; calcular e
imprimir el producto de A x B. Para obtener el producto de dos vectores
se multiplica el elemento 1 del vector A por el elemento del vector B,
el 2 de A por el 2 de B y así sucesivamente, obteniéndose la sumatoria
de los productors; el resultado no es un vector, sino un valor simple.
"""
from typing import List
from random import randint

N = 10
MIN, MAX = 1, 100


def get_data() -> List[int]:
    return [randint(MIN, MAX) for _ in range(N)]


def main():
    a = get_data()
    b = get_data()
    print(sum([a[i] * b[i] for i in range(10)]))


if __name__ == "__main__":
    main()
