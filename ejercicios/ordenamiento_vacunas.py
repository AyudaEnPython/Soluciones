"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En la clínica "Tu salud SAC", se tiene 5 salas dedicadas a aplicar la
vacuna contra el Covid-19. En cada sala van ingresando los pacientes en
grupos de 10 personas y se van registrando sus edades.

Desarrolle un programa en el que considerando el diccionario con los
siguientes datos:

Ejemplo:

    +--------------------------------------------------+
    | asistentes = {                                   |
    |     1: [43, 39, 23, 52, 21, 48, 31, 26, 55, 32], |
    |     2: [51, 29, 47, 40, 32, 25, 31, 29, 51, 36], |
    |     3: [30, 43, 52, 23, 37, 51, 29, 50, 26, 35], |
    |     4: [36, 44, 49, 22, 44, 49, 55, 48, 52, 51], |
    |     5: [32, 29, 43, 32, 32, 36, 22, 48, 38, 29], |
    | }                                                |
    +--------------------------------------------------+

- Ordenar cada una de las listas de edades, asociadas al número de
    sala, en orden decreciente. Lo que marcaría en orden en el que cada
    participante sería vacunado.
- Imprima el diccionario con los datos ordenados, tal y como se indica
    en el ejemplo.
- Para realizar el ordenamiento utilice el bubble sort.

Algunos ejemplos de diálogo de este programa serían:

    +--------------------------------------------------+
    | Antes de ordenar:                                |
    | 1: [43, 39, 23, 52, 21, 48, 31, 26, 55, 32]      |
    | 2: [51, 29, 47, 40, 32, 25, 31, 29, 51, 36]      |
    | 3: [30, 43, 52, 23, 37, 51, 29, 50, 26, 35]      |
    | 4: [36, 44, 49, 22, 44, 49, 55, 48, 52, 51]      |
    | 5: [32, 29, 43, 32, 32, 36, 22, 48, 38, 29]      |
    |                                                  |
    | Después de ordenar:                              |
    | 1: [55, 52, 48, 43, 39, 32, 31, 26, 23, 21]      |
    | 2: [51, 51, 47, 40, 36, 32, 31, 29, 29, 25]      |
    | 3: [52, 51, 50, 43, 37, 35, 30, 29, 26, 23]      |
    | 4: [55, 52, 51, 49, 49, 48, 44, 44, 36, 22]      |
    | 5: [48, 43, 38, 36, 32, 32, 32, 29, 29, 22]      |
    +--------------------------------------------------+
"""
import unittest

asistentes = {
    1: [43, 39, 23, 52, 21, 48, 31, 26, 55, 32],
    2: [51, 29, 47, 40, 32, 25, 31, 29, 51, 36],
    3: [30, 43, 52, 23, 37, 51, 29, 50, 26, 35],
    4: [36, 44, 49, 22, 44, 49, 55, 48, 52, 51],
    5: [32, 29, 43, 32, 32, 36, 22, 48, 38, 29],
}


# del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/algo_bubble_sort.py

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def main():
    ordenado = dict(
        map(lambda k: (k, bubble_sort(asistentes[k])[::-1]), asistentes)
    )
    print("Antes de ordenar:")
    for k in asistentes:
        print(f"{k}: {asistentes[k]}")
    print("\nDespués de ordenar:")
    for k in ordenado:
        print(f"{k}: {ordenado[k]}")


class Test(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([4, 2, 1, 3, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort([3, 2, 4, 1, 5])[::-1], [5, 4, 3, 2, 1])


if __name__ == "__main__":
    # unittest.main() # uncomment/commnent to run test
    main()
