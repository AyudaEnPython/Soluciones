"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar los métodos Python para:

1. Ingrese 12 números en un arreglo bidimensional (matriz) de 4x3 y
    obtenga la suma de cada fila

    # Ejemplo:
    #                     suma
    #   |  45 25  -10   | = 60
    # A |  15 38    0   | = 53
    #   | -20 15.5 10.8 | = 6.3
    #   |  30 41    4   | = 75

2. Generar la siguiente matriz de orden NxN

    # Ejemplo:
    #       | 1 0 1 0 |
    # Mat = | 1 0 1 0 |
    #       | 1 0 1 0 |
    #       | 1 0 1 0 |

3. Crear la matriz "vibora" orden NxN

    # Ejemplo:
    #     |  1  2  3  4 |
    # V = |  8  7  6  5 |
    #     |  9 10 11 12 |
    #     | 16 15 14 13 |

4. Ordenar las filas de una matriz de tamaño NxN por la segunda columna
    ascendentemente.

    # Ejemplo:
    #       | 90 -20  30 |                    | 90 -20 30 |
    # Mat = | 55  45  35 | -> Mat(ordenada) = |  0  -5 78 |
    #       |  0  -5  78 |                    | 55  45 35 |
    #
    # Sugerencia: Emplear la función argsort() de Numpy

5. Obtener la solución de un sistema de ecuaciones lineales. Desarrolle
    el método.

    # Ejemplo:
    #                x + 2y +  3z = 1
    #               3x + 5y + 10z = 2
    #              -5x - 2y -  4z = 3
    #
    #     | 1  2  3 |   | 1 |
    # A = | 3  5 10 |   | 2 |
    #     |-5 -2 -4 |   | 3 |
    #
    # La solución: [-1. 1. 0]
    # Sugerencia: Use la función solve() de la librería Numpy
"""
import numpy as np


def main():
    # Ejercicio 1
    A = np.array([[45, 25, -10], [15, 38, 0], [-20, 15.5, 10.8], [30, 41, 4]])
    print(A.sum(axis=1))

    # Ejercicio 2
    n = 4
    M = np.zeros((n, n))
    for i in range(n):
        for j in range(0, n, 2):
            M[i, j] = 1
    print(M)

    # Ejercicio 3
    n = 4
    V = np.array(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    )
    for i in range(n):
        if i % 2 != 0:
            V[i] = V[i][::-1]
    print(V)

    # Ejercicio 4
    n = 4
    M = np.array(
        [[90, -20, 30], [55, 45, 35], [0, -5, 78]]
    )
    print(M[M[:, 1].argsort()])

    # Ejercicio 5
    A = np.array([[1, 2, 3], [3, 5, 10], [-5, -2, -4]])
    b = np.array([1, 2, 3])
    print(np.linalg.solve(A, b))


if __name__ == "__main__":
    main()
