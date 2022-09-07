"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente una función, utilizando el algoritmo de búsqueda binaria,
para buscar datos que están en una lista de diccionarios sobre
películas, con la siguiente estructura: título y año. Note que la lista
no esta ordenada. La función debe tomar un parámetro (el año a buscar)
y debe devolver el título de la película.

Un ejemplo de la lista sería:

    +------------------------------------------------------+
    | peliculas = [                                        |
    |     {"titulo": "Shrek", "anio": 2001},               |
    |     {"titulo": "El viaje de Chihiro", "anio": 2002}, |
    |     {"titulo": "WALL-E", "anio": 2008},              |
    |     {"titulo": "Up", "anio": 2009},                  |
    |     {"titulo": "Buscando a Nemo", "anio": 2003},     |
    |     {"titulo": "Los Increíbles", "anio": 2004},      |
    |     {"titulo": "Wallace y Gromit", "anio": 2005},    |
    |     {"titulo": "Valiente", "anio": 2012},            |
    |     {"titulo": "Frozen", "anio": 2013},              |
    |     {"titulo": "Grandes Héroes", "anio": 2014},      |
    |     {"titulo": "Happy Feet", "anio": 2006},          |
    |     {"titulo": "Ratatouille", "anio": 2007},         |
    |     {"titulo": "Toy Story 3", "anio": 2010},         |
    |     {"titulo": "Rango", "anio": 2011},               |
    | ]                                                    |
    +------------------------------------------------------+

Considere, que los datos ya están en el programa, no necesita la lista
de películas y realize el siguiente proceso:

- Solicite al usuario que ingrese un año.
- Buscar la película por el año, utilizando la función implementada.
- Imprimir el título de la película.

    +----------------------------------------------+
    | Ingrese año: 2002                            |
    | Película: El viaje de Chihiro                |
    +----------------------------------------------+

    +----------------------------------------------+
    | Ingrese año: 2013                            |
    | Película: Frozen                             |
    +----------------------------------------------+

NOTE: En el enunciado original la lista se llama 'peliculas', cuando el
    mejor nombre para esa lista debería de ser 'ganadores'.
"""
# Mismo ejercicio que:
# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/busqueda_premios.py
import unittest

peliculas = [
    {"titulo": "Shrek", "anio": 2001},
    {"titulo": "El viaje de Chihiro", "anio": 2002},
    {"titulo": "WALL-E", "anio": 2008},
    {"titulo": "Up", "anio": 2009},
    {"titulo": "Buscando a Nemo", "anio": 2003},
    {"titulo": "Los Increíbles", "anio": 2004},
    {"titulo": "Wallace y Gromit", "anio": 2005},
    {"titulo": "Valiente", "anio": 2012},
    {"titulo": "Frozen", "anio": 2013},
    {"titulo": "Grandes Héroes", "anio": 2014},
    {"titulo": "Happy Feet", "anio": 2006},
    {"titulo": "Ratatouille", "anio": 2007},
    {"titulo": "Toy Story 3", "anio": 2010},
    {"titulo": "Rango", "anio": 2011},
]


# del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_binary_search.py
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]["anio"] == x:
            return mid
        elif arr[mid]["anio"] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    data = sorted(peliculas, key=lambda x: x["anio"])
    anio = input("Ingresar año: ")
    pos = binary_search(data, int(anio))
    if pos != -1:
        print(data[pos]["titulo"])
    else:
        print("No se encontró el año")


class Test(unittest.TestCase):

    data = sorted(peliculas, key=lambda x: x["anio"])

    def test_binary_search(self):
        self.assertEqual(binary_search(self.data, 2002), 1)
        self.assertEqual(binary_search(self.data, 2021), -1)
        self.assertEqual(binary_search(self.data, 2013), 12)


if __name__ == "__main__":
    # unittest.main() # uncomment/comment to run tests
    main()
