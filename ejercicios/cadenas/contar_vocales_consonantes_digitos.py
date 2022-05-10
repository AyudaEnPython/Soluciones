"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algoritmo que cuente vocales, consonantes y digitos de la
siguiente forma:

- Solicite al usuario que ingrese una frase.
- Cuente y guarde en un diccionario la cantidad de vocales, de
    consonantes y de digitos que hay en la frase.
- Imprima el diccionario como en los ejemplos.

Algunos ejemplos de diálogo de este programa serían:

    +-------------------------------------------+
    | Input: estoy programado en el 2020        |
    | vocales: 8                                |
    | consonantes: 11                           |
    | digitos: 4                                |
    +-------------------------------------------+

    +-------------------------------------------+
    | Input: PRO CS1111                         |
    | vocales: 1                                |
    | consonantes: 4                            |
    | digitos: 4                                |
    +-------------------------------------------+
"""
from typing import Dict
from unittest import main, TestCase


def contar(frase: str) -> Dict[str, int]:
    """Cuenta vocales, consonantes y digitos de una frase.

    :param frase: La frase a contar.
    :frase type: str
    :return: Un diccionario con las cantidades de vocales, consonantes
        y digitos.
    :rtype: Dict[str, int]
    """
    frase: str = frase.lower()
    vocales: int = 0
    consonantes: int = 0
    digitos: int = 0
    for caracter in frase:
        if caracter in "aeiou":
            vocales += 1
        elif caracter in "bcdfghjklmnñpqrstvwxyz":
            consonantes += 1
        elif caracter in "0123456789":
            digitos += 1
    return {
        "vocales": vocales, "consonantes": consonantes, "digitos": digitos
    }


def main_():
    frase = input("Input: ")
    resultado = contar(frase)
    print(f"vocales: {resultado['vocales']}")
    print(f"consonantes: {resultado['consonantes']}")
    print(f"digitos: {resultado['digitos']}")


class Test(TestCase):

    def test_contar(self):
        self.assertEqual(
            contar("estoy programado en el 2020"),
            {"vocales": 8, "consonantes": 11, "digitos": 4}
        )
        self.assertEqual(
            contar("PRO CS1111"),
            {"vocales": 1, "consonantes": 4, "digitos": 4}
        )


if __name__ == '__main__':
    # main() # uncomment this line and comment the next one to run tests
    main_()