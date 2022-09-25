"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una pirámide se apila de acuerdo con un principio simple: cada capa
inferior contiene un bloque más que la capa superior.

#           +---+
#           |   |
#         +---+---+
#         |   |   |
#       +---+---+---+
#       |   |   |   |
#       +---+---+---+

Escribir un programa que lea la cantidad de bloques que tiene los
constructores y generar la altura de la pirámide que se puede construir
utilizando estos bloques.

Nota: la altura se mide por el número de capas completas: si los
constructores no tienen la cantidad suficiente de bloques y no pueden
completar la siguiente capa, terminan su trabajo inmediatamente.
"""
from unittest import main, TestCase


def solucion_a(bloques: int) -> int:
    """Devuelve la altura de la piramide

    :param bloques: Bloques disponibles
    :bloques type: int
    :return: Altura de la pirámide
    :rtype: int

    .. Nota::

        +---+   +---+---+     +-----+-----+
        | i |   | c | b | ->  | c+1 | b-c |
        +---+   +---+---+     +-----+-----+
        | 1 |   | 0 | 8 |     |  1  |  7  |
        | 2 |   | 1 | 7 |     |  2  |  5  |
        | 3 |   | 2 | 5 |     |  3  |  2  |
        | 4 |   | 3 | 2 |     |     |     |
        +---+   +---+---+     +-----+-----+
    """
    capas = 0
    while bloques > capas:
        capas += 1
        bloques -= capas
    return capas


def solucion_b(bloques: int) -> int:
    """Devuelve la altura de la piramide

    :param bloques: Bloques disponibles
    :bloques type: int
    :return: Altura de la pirámide
    :rtype: int

    .. Nota::

        b = (h*(h+1))/2
        h^2 + h -2b = 0
        h = (-1 + (1 + 8*b)^(1/2))*(1/2)
    """
    return (-1 + ((1 + 8*bloques)**(0.5))) // 2


class Test(TestCase):

    def test_solucion_a(self):
        self.assertEqual(solucion_a(3), 2)
        self.assertEqual(solucion_a(6), 3)
        self.assertEqual(solucion_a(8), 3)
        self.assertEqual(solucion_a(10), 4)

    def test_solucion_b(self):
        self.assertEqual(solucion_b(3), 2)
        self.assertEqual(solucion_b(6), 3)
        self.assertEqual(solucion_b(8), 3)
        self.assertEqual(solucion_b(10), 4)


if __name__ == "__main__":
    main()
