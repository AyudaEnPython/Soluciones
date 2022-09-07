"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Premios - Búsquedas

Implemente una función, utilizando el algoritmo de búsqueda binaria,
para buscar datos que están en una lista de diccionarios sobre
ganadores de premios nobel, con la siguiente estructura: año y
ganadores. La función debe tomar un parámetro: el año a buscar y debe
devolver los ganadores.

Un ejemplo sería, la lista de ganadores de premios noble de Física:

+----------------------------------------------------------------------+
| peliculas = [                                                        |
|     {"anio": 2010, "nombre": "Andre Geim y Konstantín Novosiólov"},  |
|     {"anio": 2011, "nombre": "Perlmutter, Schmidt y Adasm Riess"},   |
|     {"anio": 2012, "nombre": "Serge Haroche y David Wineland"},      |
|     {"anio": 2013, "nombre": "Peter Higgs y François Englert"},      |
|     {"anio": 2014, "nombre": "Akasaki, Hiroshi Amano y Nakamura"},   |
|     {"anio": 2015, "nombre": "Takaaki Kajita y Arthur B. McDonald"}, |
|     {"anio": 2016, "nombre": "Thoulesss, Haldane y Kosterlitz"},     |
|     {"anio": 2017, "nombre": "Rainer Weiss, Barry Barish y Thorne"}, |
|     {"anio": 2018, "nombre": "Donna Strickland, Mourou y Ashkin"},   |
|     {"anio": 2019, "nombre": "James Peebles, Mayor y Queloz"},       |
| ]                                                                    |
+----------------------------------------------------------------------+

Considere, que los datos ya están en el programa, no necesita la lista
y realize el siguiente proceso:

- Solicite al usuario que ingrese un año.
- Buscar en la lista de diccionarios por año, utilizando la función
    implementada.
- Imprimir los nombres de los ganadores.

    +----------------------------------------------+
    | Ingrese año: 2011                            |
    | Ganadores: Perlmutter, Schmidt y Adasm Riess |
    +----------------------------------------------+

    +----------------------------------------------+
    | Ingrese año: 2018                            |
    | Ganadores: Donna Strickland, Mourou y Ashkin |
    +----------------------------------------------+

NOTE: En el enunciado original la lista se llama 'peliculas', cuando el
    mejor nombre para esa lista debería de ser 'ganadores'.
"""
import unittest

peliculas = [
    {"anio": 2010, "nombre": "Andre Geim y Konstantín Novosiólov"},
    {"anio": 2011, "nombre": "Perlmutter, Schmidt y Adasm Riess"},
    {"anio": 2012, "nombre": "Serge Haroche y David Wineland"},
    {"anio": 2013, "nombre": "Peter Higgs y François Englert"},
    {"anio": 2014, "nombre": "Akasaki, Hiroshi Amano y Nakamura"},
    {"anio": 2015, "nombre": "Takaaki Kajita y Arthur B. McDonald"},
    {"anio": 2016, "nombre": "Thoulesss, Haldane y Kosterlitz"},
    {"anio": 2017, "nombre": "Rainer Weiss, Barry Barish y Thorne"},
    {"anio": 2018, "nombre": "Donna Strickland, Mourou y Ashkin"},
    {"anio": 2019, "nombre": "James Peebles, Mayor y Queloz"},
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
    anio = input("Ingresar año: ")
    pos = binary_search(peliculas, int(anio))
    if pos != -1:
        print("Ganadores:", peliculas[pos]["nombre"])
    else:
        print("No se encontró el año")


class Test(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(binary_search(peliculas, 2010), 0)
        self.assertEqual(binary_search(peliculas, 2021), -1)
        self.assertEqual(binary_search(peliculas, 2019), 9)


if __name__ == "__main__":
    # unittest.main() # uncomment/comment to run tests
    main()
