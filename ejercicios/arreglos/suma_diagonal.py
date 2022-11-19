"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que capture los valores de una matriz 3x3 e
imprima en pantalla la suma de la diagonal.
"""


def f(arr):
    return sum(arr[i][i] for i in range(len(arr)))


def ingresar_valores(n=3):
    return [
        [int(input(f"[{i}][{j}] -> ")) for j in range(n)]
        for i in range(n)
    ]


def main():
    arr = ingresar_valores()
    print("Matriz:")
    for row in arr:
        print(*row)
    print(f"Suma de la diagonal principal: {f(arr)}")


if __name__ == "__main__":
    main()
