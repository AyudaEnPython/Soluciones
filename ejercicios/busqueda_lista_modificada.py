"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe una función que reciba un array de números y un número entero a
buscar. El detalle es que los números en el array han sido movidos a la
izquierda o derecha por 1 o más posiciones. Por ejemplo, [1, 2, 3, 4]
fue transformado a [3, 4, 1, 2].
La función debe utilizar una variación de busqueda binaria para
determinar si el entero a buscar se encuentra en la lista. En caso el
entero no se encuentre en la lista retornar -1. Si el entero se
encuentra en la lista retornar la posición.

    +---------------------------------------------------+
    | Input: [45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33 |
    | Output: 8                                         |
    +---------------------------------------------------+
"""
from unittest import main, TestCase


# Tomado del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_binary_search.py
def binary_search_unsorted(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        else: # modified to handle unsorted array
            if x in arr[mid:]:
                low = mid + 1
            elif x in arr[0:mid-1]:
                high = mid - 1
            else:
                return -1


def main_():
    m = [int(x) for x in input("Array: ").split(",")]
    x = int(input("Elemento a buscar: "))
    print(f"Input: {m}, {x}")
    print(f"Output: {binary_search_unsorted(m, x)}")


class Test(TestCase):

    def test_binary_search_unsorted(self):
        self.assertEqual(
            binary_search_unsorted(
                [45, 61, 71, 72, 73, 0, 1, 21, 33, 37], 33
            ),
            8,
        )


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run tests
    main_()