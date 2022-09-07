"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Usando una lista por comprensión implementa un programa, que resuelva
lo siguiente:

- Pida al usuario un número, luego crea e imprime una lista con los
    múltiplos del número ingresado desde el cero hasta el cien.
- Dada una lista de ciudades:
    ciudades = [
        "Lima", "Arequipa", "Trujillo", "Cusco", "Tacna", "Iquitos"
    ]
    Pida al usuario una vocal y cree una lista solo con las frutas que
    tienen esa vocal en su nombre.
- Usando la matriz:

        +---+---+---+---+
        | 4 | 5 | 6 | 3 |
        +---+---+---+---+
        | 1 | 4 | 6 | 7 |
        +---+---+---+---+
        | 8 | 2 | 3 | 6 |
        +---+---+---+---+
        | 3 | 5 | 4 | 9 |
        +---+---+---+---+
        | 3 | 4 | 5 | 3 |
        +---+---+---+---+

    Pida al usuario ingresar par o impar, si ingresó par, entonces cree
    una lista con los números pares de la matriz, si ingresó impar,
    cree una lista con los números impares.

Algunos ejemplos de diálogo de este programa serían:

    +--------------------------------------------------------+
    | numero = 20                                            |
    | multiplos = [20, 40, 60, 80, 100]                      |
    |                                                        |
    | vocal: i                                               |
    | respuesta: ["Lima", "Arequipa", "Trujillo", "Iquitos"] |
    |                                                        |
    | Par/Impar: par                                         |
    | respuesta: [4, 6, 4, 6, 8, 2, 6, 4, 4]                 |
    +--------------------------------------------------------+

# ---------------------------------------------------------------------
Nota: El enunciado no esta bien redactado, en el punto 2 deberia ser
    una lista con las ciudades que contienen esa vocal en su nombre.
"""
from typing import List
from unittest import main, TestCase
from unittest.mock import patch

ciudades = ["Lima", "Arequipa", "Trujillo", "Cusco", "Tacna", "Iquitos"]


def multiplos(n: int) -> List[int]:
    """
    >>> multiplos(20)
    [20, 40, 60, 80, 100]
    >>> multiplos(25)
    [25, 50, 75, 100]
    """
    return [i * n for i in range(1, 101//n + 1)]


def vocales_en(ciudades: list, vocal: str) -> List[str]:
    """
    >>> ciudades = [ \
        "Lima", "Arequipa", "Trujillo", "Cusco", "Tacna", "Iquitos" \
    ]
    >>> vocales_en(ciudades, 'i')
    ['Lima', 'Arequipa', 'Trujillo', 'Iquitos']
    >>> vocales_en(ciudades, 'a')
    ['Lima', 'Arequipa', 'Tacna']
    """
    return [ciudad for ciudad in ciudades if vocal in ciudad]


def pares_impares(matriz: List[List[int]], s: str) -> List[int]:
    """
    >>> matriz = [ \
        [4, 5, 6, 3], \
        [1, 4, 6, 7], \
        [8, 2, 3, 6], \
        [3, 5, 4, 9], \
        [3, 4, 5, 3] \
    ]
    >>> pares_impares(matriz, 'par')
    [4, 6, 4, 6, 8, 2, 6, 4, 4]
    """
    if s == 'par':
        return [x for fila in matriz for x in fila if x % 2 == 0]
    elif s == 'impar':
        return [x for fila in matriz for x in fila if x % 2 != 0]
    else:
        return []


class Test(TestCase):

    matriz = [
        [4, 5, 6, 3],
        [1, 4, 6, 7],
        [8, 2, 3, 6],
        [3, 5, 4, 9],
        [3, 4, 5, 3],
    ]

    def test_multiplos(self):
        self.assertEqual(multiplos(20), [20, 40, 60, 80, 100])
        self.assertEqual(multiplos(25), [25, 50, 75, 100])

    def test_vocales_en(self):
        self.assertEqual(
            vocales_en(ciudades, 'i'),
            ['Lima', 'Arequipa', 'Trujillo', 'Iquitos'],
        )
        self.assertEqual(
            vocales_en(ciudades, 'a'),
            ['Lima', 'Arequipa', 'Tacna'],
        )

    def test_pares_impares(self):
        self.assertEqual(
            pares_impares(self.matriz, 'par'),
            [4, 6, 4, 6, 8, 2, 6, 4, 4],
        )
        self.assertEqual(
            pares_impares(self.matriz, 'impar'),
            [5, 3, 1, 7, 3, 3, 5, 9, 3, 5, 3],
        )

    @patch('builtins.input', side_effect=['par', 'impar'])
    def test_pares_impares_input(self, input):
        self.assertEqual(
            pares_impares(self.matriz, input()),
            [4, 6, 4, 6, 8, 2, 6, 4, 4],
        )
        self.assertEqual(
            pares_impares(self.matriz, input()),
            [5, 3, 1, 7, 3, 3, 5, 9, 3, 5, 3],
        )


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
