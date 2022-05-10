"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Find the key - búsqueda lineal y binaria

Se le solicita que desarrolle una función que reciba como parámetro un
diccionario y un valor númerico (key) de búsqueda.
El diccionario contiene la información de los usuarios de un sistema,
cada uno con un código único (la llave del diccionario) y con una lista
de claves numéricas, diferentes todas entre sí. Es decir, ningun
usuario tiene alguna clave igual al de otro usuario. Se solicita que
implemente dos búsquedas:
- Una búsqueda binaria para encontrar la clave de búsqueda en la lista
    de claves de cada usuario.
- Una búsqueda lineal para encontrar el usuario que contiene la clave
    de búsqueda. Esta búsqueda depende de la búsqueda previa.

Por último, su función findTheKey deberá retornar el código + nombre
del usuario que contiene la clave.

    +-----------------------------------------------------------+
    | {                                                         |
    |     0: {                                                  |
    |         "nombre": "Mirabel",                              |
    |         "claves": [13, 24, 26, 33, 9, 44, 3, 19, 27, 48]  |
    |     },                                                    |
    |     1: {                                                  |
    |         "nombre": "Camilo",                               |
    |         "claves": [32, 46, 50, 30, 22, 35, 8, 15, 14, 7]  |
    |     },                                                    |
    |     2: {                                                  |
    |         "nombre": "Agustín",                              |
    |         "claves": [1, 12, 36, 37, 42, 47, 34, 10, 39]     |
    |     },                                                    |
    | }                                                         |
    +-----------------------------------------------------------+

Si se invoca a la función findTheKey con la clave de búsqueda 14,
deberá retornar (1, "Camilo") ya que Camilo es el usuario que tiene la
clave de búsqueda 14 en su lista de claves.
Recuerde utilizar búsqueda binaria al menos para encontrar la clave en
la lista de claves de cada usuario. Utilice funciones.

NOTE: Se opta por cambiar findTheKey por find_key (PEP8).
"""
from unittest import main, TestCase
from typing import Dict, List, Tuple

data = {
    0: {
        "nombre": "Mirabel",
        "claves": [13, 24, 26, 33, 9, 44, 3, 19, 27, 48]
    },
    1: {
        "nombre": "Camilo",
        "claves": [32, 46, 50, 30, 22, 35, 8, 15, 14, 7]
    },
    2: {
        "nombre": "Agustín",
        "claves": [1, 12, 36, 6, 37, 42, 47, 34, 10, 39]
    }
}


# tomado del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_binary_search.py
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def ordenar(arr: List[Dict[str, List[int]]]) -> List[Dict[str, List[int]]]:
    data = arr
    for k in arr:
        arr[k]["claves"].sort()
    return data


def find_key(
    arr: Dict[int, Dict[str, List[int]]], key: int,
) -> Tuple[int, str]:
    """
    :param arr: Diccionario de usuarios
    :param key: Clave de búsqueda
    :return: Tupla con el código de usuario y el nombre
    :rtype: Tuple[int, str]
    """
    arr = ordenar(arr)
    for k, v in arr.items():
        if binary_search(v["claves"], key) != -1:
            return k, v["nombre"]
    return -1, "No se encontró el usuario"


def main_():
    clave = int(input("Ingresar clave de búsqueda: "))
    print(find_key(data, clave))


class Test(TestCase):

    def test_ordenar(self):
        self.assertEqual(
            ordenar(data),
            {
                0: {
                    "nombre": "Mirabel",
                    "claves": [3, 9, 13, 19, 24, 26, 27, 33, 44, 48]
                },
                1: {
                    "nombre": "Camilo",
                    "claves": [7, 8, 14, 15, 22, 30, 32, 35, 46, 50]
                },
                2: {
                    "nombre": "Agustín",
                    "claves": [1, 6, 10, 12, 34, 36, 37, 39, 42, 47]
                }
            }
        )

    def test_find_key(self):
        self.assertEqual(find_key(data, 14), (1, "Camilo"))
        self.assertEqual(find_key(data, 1), (2, "Agustín"))
        self.assertEqual(find_key(data, 48), (0, "Mirabel"))
        self.assertEqual(find_key(data, 50), (1, "Camilo"))
        self.assertEqual(find_key(data, 3), (0, "Mirabel"))
        self.assertEqual(
            find_key(data, -1), (-1, "No se encontró el usuario")
        )


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run tests
    main_()
