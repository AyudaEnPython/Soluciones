"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Dado un n leer una matriz de NxN se pide mostrar su transpuesta

#     | 1  2  3 |           | 1  4  7 |
# A = | 4  5  6 |  ->  At = | 2  5  8 |
#     | 7  8  9 |           | 3  6  9 |

2. Ingrese los elementos de una matriz de tamaño NxM generar una nueva
matriz donde un elementos es la suma de los dígitos de la misma
posición en la matriz original.

#     | 11  12   1 |             | 2 3 1 |
# A = |  2   3   5 | resultado = | 2 3 5 |
#     |  8  13  21 |             | 8 4 3 |

TODO: add typing later...
"""


def input_data(cuadrada=True):
    if cuadrada:
        n = int(input("N: "))
        m = n
    else:
        n = int(input("N: "))
        m = int(input("M: "))
    arr = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            arr[i][j] = int(input(f"[{i}, {j}]: "))
    return arr


def show_result(a, b, msg):
    print("Matriz original")
    print(a)
    print(f"Matriz {msg}")
    print(b)


def transpuesta(arr):
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]


def ex_1():
    arr = input_data()
    arr_t = transpuesta(arr)
    show_result(arr, arr_t, "transpuesta")


def ex_2():
    f = lambda n: sum([int(i) for i in str(n)])  # noqa: E731
    arr = input_data(False)
    n_arr = list(map(lambda x: list(map(f, x)), arr))
    show_result(arr, n_arr, "resultado")


if __name__ == "__main__":
    ex_1()
    ex_2()
