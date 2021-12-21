"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Definir una función denominada “recorta_nombres” que reciba por
parámetro una lista de cadenas de caracteres. Deberá recortar cada
cadena de la lista a la longitud de la última cadena de caracteres de
dicha lista.

NOTE: El enunciado no es claro, no especifica que parte (izquierda o
    derecha) de la cadena de caracteres se recorta.
"""
from typing import List
from unittest import main, TestCase


def recortar_nombres(nombres: List[str]) -> List[str]:
    """Recorta los nombres de la lista a la longitud de la última
    cadena de caracteres.

    :param nombres: Lista de cadenas de caracteres.
    :nombres type: List[str]
    :return: Lista de cadenas de caracteres recortadas.
    :rtype: List[str]
    """
    n = len(nombres[-1])
    return [nombre[:n] for nombre in nombres] # [n:] para recortar a la derecha


def main_():
    nombres = ["abcdef", "abc", "ab", "abcd"]
    print(f"Nombres recortados: {recortar_nombres(nombres)}")


class Test(TestCase):

    def test_recortar_nombres(self):
        self.assertEqual(
            recortar_nombres(["Steve", "Yngwie", "Joe"]),
            ["Ste", "Yng", "Joe"],
        )


if __name__ == "__main__":
    #main()
    main_()