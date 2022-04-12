"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Genere una matriz de 25 x 40 con números decimales al azar entre 0 y 1.
Mostrar los numeros del perimetro y calcularlo.
"""
from random import random

from prototools import show_matrix


def solver_a():
    """
    >>> solver_a()
    [1, 2, 3, 4, 5, 16, 17, 18, 19, 20, 6, 11, 10, 15]
    147
    """
    #arr = [[random() for _ in range(40)] for _ in range(25)]
    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],

    ]
    r_arr = list(map(list, zip(*arr)))
    perimetro = [*arr[0], *arr[-1], *r_arr[0][1:-1], *r_arr[-1][1:-1]]
    print(perimetro)
    print(sum(perimetro))


def solver_b():
    arr = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],

    ]
    r_arr = list(map(list, zip(*arr)))
    perimetro = [*arr[0], *arr[-1], *r_arr[0][1:-1], *r_arr[-1][1:-1]]
    t = [[0 for _ in range(5)] for _ in range(4)]
    t[0] = arr[0]
    t[-1] = arr[-1]
    for i in range(1, len(t[0]) - 1):
        t[i][0] = r_arr[0][i]
        t[i][-1] = r_arr[-1][i]
    show_matrix(t)
    print(sum(perimetro))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # solver_a()
    # solver_b()
