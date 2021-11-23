"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada la siguiente matriz, de letras y números:

        +-----+-----+-----+-----+
        |  P  |  O  |  P  |  B  |
        +-----+-----+-----+-----+
        |  E  |  4  |  E  |  2  |
        +-----+-----+-----+-----+
        |  R  |  R  |  T  |  3  |
        +-----+-----+-----+-----+
        |  I  |  5  |  F  |  L  |
        +-----+-----+-----+-----+
        |  C  |  L  |  5  |  G  |
        +-----+-----+-----+-----+
        |  A  |  J  |  3  |  0  |
        +-----+-----+-----+-----+

Implemente un algoritmo que realice lo siguiente:

- Escriba la matriz de datos en el programa principal.
- Solicite al usuario que ingrese un número de fila y el programa debe
    concatenar e imprimir los caracteres de la fila ingresada.
- Solicite al usuario que ingrese un caracter (letra o número), y el
    programa debe imprimir la posición o posiciones (fila, columna) de
    ese caracter.

Algunos ejemplos de diálogo de este programa serían:

    +-----------------------+
    | Ingrese fila: 2       |
    | Fila 2: RRT3          |
    | Ingrese caracter: L   |
    | Output: (3, 3) (4, 1) |
    +-----------------------+

    +-----------------------+
    | Ingrese fila: 4       |
    | Fila 2: CL5G          |
    | Ingrese caracter: 3   |
    | Output: (2, 3) (5, 2) |
    +-----------------------+
"""
import io
from textwrap import dedent
from typing import Any, List
from unittest import main, TestCase
from unittest.mock import patch
# pip install prototools
from prototools import Menu, show_matrix
from prototools.colorize import red

m = [
    ['P', 'O', 'P', 'B'],
    ['E', '4', 'E', '2'],
    ['R', 'R', 'T', '3'],
    ['I', '5', 'F', 'L'],
    ['C', 'L', '5', 'G'],
    ['A', 'J', '3', '0'],
]

def _user_input(s, f) -> str:
    """Interfaz para capturar datos de usuario."""
    s = input(s)
    f(m, s)


def show_row(m: List[List[Any]], row: int):
    """Muestra la fila indicada."""
    row = int(row)
    print('Fila {}: {}'.format(row, ''.join(m[row])))


def find_char(m: List[List[Any]], char: str) -> None:
    """Busca la posición de un caracter en la matriz."""
    t = ""
    for row in range(len(m)):
        for col in range(len(m[row])):
            if m[row][col] == char:
                t += f" ({row}, {col})"
    print(f'Output:{t}')


def main_():
    menu = Menu(red("Matrix"), arrow_keys=True)
    menu.add_options(
        ("Mostrar matriz", show_matrix, m),
        ("Mostrar matriz con indices",
        lambda: show_matrix(m, show_index=True)),
        ("Mostrar fila",
        lambda: _user_input("Ingrese fila: ", show_row)),
        ("Buscar caracter",
        lambda: _user_input("Ingrese caracter: ", find_char)),
    )
    menu.run()


class Test(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_show_row(self):
        self.assert_stdout("Fila 2: RRT3\n", function=lambda: show_row(m, 2))

    def test_find_char(self):
        self.assert_stdout(
            "Output: (2, 3) (5, 2)\n",
            function=lambda: find_char(m, '3'),
        )


if __name__ == '__main__':
    # main() # uncomment this line and comment the next one to run tests
    main_()