"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Autor de la publicación:

array = [16, 17, 4, 3 ,5, 2]
arr=[]
for i in range ( len (array) - 1 ):
    if array[i] > array[ i + 1 ]:
    arr.append ( array [i])
print(arr)

Debo realizar una impresión de un arreglo que me contenga
solo los números de un segundo arreglo que sean mayor en su
posición e índice a todos los siguientes a su derecha.

Input = [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2] y no [17, 4, 5]

NOTE: Falta el enunciado original del ejercicio.
TODO: add tests later...
"""
from typing import List


def solve(arr: List[int]) -> List[int]:
    return [
        x for i, x in enumerate(arr)
        if x > max(arr[i+1:], default=0)
    ]


def main():
    array = [16, 17, 4, 3 ,5, 2]
    sol = solve(array)
    print(sol)


if __name__ == "__main__":
    main()
