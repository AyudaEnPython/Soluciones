"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa en el que se pida al usuario el tamaño (n) de una
matriz. Forme una matriz tridiagonal. Si por ejemplo, el usuario
ingreso n = 6, se debería presentar la siguiente matriz:

    Ingrese el tamaño de la matriz: 6
    [
        [ 2.  1.  0.  0.  0.  0.]
        [-1.  4.  2.  0.  0.  0.]
        [ 0. -2.  6.  3.  0.  0.]
        [ 0.  0. -3.  8.  4.  0.]
        [ 0.  0.  0. -4. 10.  5.]
        [ 0.  0.  0.  0. -5. 12.]
    ]
"""
# pip install prototools
from prototools import matrix, show_matrix
from prototools.colorize import magenta, cyan, yellow


def f(m, d, color):
    for i in range(len(m)):
        m[i][i] = d(str(i*2 + 2))
    for i in range(len(m)-1):
        m[i][i+1] = color(str(i + 1))
    for i in range(len(m)-1):
        m[i+1][i] = color(str((i + 1) * -1))


if __name__ == "__main__":
    n = 6
    m = matrix(n, n, (0, 0))
    f(m, yellow, cyan)
    show_matrix(m, width=5,color=magenta)
