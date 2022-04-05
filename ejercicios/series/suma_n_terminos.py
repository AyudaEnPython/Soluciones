"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Obtener la suma de los primeros N términos de la serie:
2, 5, 7, 10, 12, 15, 17... (se obtiene agregando 3 y 2 alternadamente)
"""
from itertools import cycle


def serie(n):
    arr = [2]
    prev = arr[0]
    for i, c in zip(range(1, n), cycle([3, 2])):
        arr.append(prev + c)
        prev = arr[i]
    return arr


def main():
    n = int(input("Ingrese el número de términos: "))
    print(f"Suma de los primeros {n} términos de la serie: {sum(serie(n))}")


if __name__ == "__main__":
    main()
