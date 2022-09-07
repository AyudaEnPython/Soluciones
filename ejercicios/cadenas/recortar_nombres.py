"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Definir una función denominada “recorta_nombres” que reciba por
parámetro una lista de cadenas de caracteres. Deberá recortar cada
cadena de la lista a la longitud de la última cadena de caracteres de
dicha lista.

NOTE: El enunciado no es claro, no especifica que parte (izquierda o
    derecha) de la cadena de caracteres se recorta.
"""
import unittest
from typing import List


def recortar_nombres(nombres: List[str]) -> List[str]:
    """Recorta los nombres de la lista a la longitud de la última
    cadena de caracteres.

    :param nombres: Lista de cadenas de caracteres.
    :nombres type: List[str]
    :return: Lista de cadenas de caracteres recortadas.
    :rtype: List[str]
    """
    n = len(nombres[-1])
    return [nombre[:n] for nombre in nombres]  # [n:] recortar a la derecha


def main():
    nombres = ["abcdef", "abc", "ab", "abcd"]
    print(f"Nombres recortados: {recortar_nombres(nombres)}")


class Test(unittest.TestCase):

    def test_recortar_nombres(self):
        self.assertEqual(
            recortar_nombres(["Alejandra", "Pedro"]),
            ["Aleja", "Pedro"],
        )
        self.assertEqual(recortar_nombres(["Margarita"]), ["Margarita"])


if __name__ == "__main__":
    # unittest.main()
    main()
