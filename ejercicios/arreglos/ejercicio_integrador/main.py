# pip install prototools
from prototools import int_input, matrix, show_matrix, flatten, textbox


def fill(arr):
    return [[
        int_input(f"Valor para ({i}, {j}): ")
        for j in range(len(arr[0]))
    ] for i in range(len(arr))]


def max_value(arr):
    return max(flatten(arr))


def get_col(arr, j):
    return [arr[i][j] for i in range(len(arr))]


def report(arr, max_value):
    _ = "El valor máximo {} se encuentra en la columna N° {}"
    return "\n".join([
        _.format("si", i) if max_value in col else _.format("no", i)
        for i, col in enumerate([get_col(arr, j) for j in range(len(arr[0]))])
        ])



def main():
    n = int_input("Ingresar número de filas: ", lang="es")
    m = int_input("Ingresar número de columnas: ", lang="es")
    matriz = fill(matrix(n, m))
    textbox("Matriz ingresada")
    show_matrix(matriz)
    print(f"El valor máximo es: {max_value(matriz)}")


if __name__ == "__main__":
    main()
