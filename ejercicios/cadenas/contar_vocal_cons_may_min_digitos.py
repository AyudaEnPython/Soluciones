"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crea una función que reciba un texto y mediante una estructura
repetitiva, lea el contenido y muestre letra por letra el contenido,
al terminar, deberá mostrar además 2 de las siguientes acciones:

- Cantidad de vocales
- Cantidad de consonantes
- Cantidad de mayúsculas
- Cantidad de minúsculas
- Cantidad de números contenidos en el texto

NOTE: Se opta por ejecutar todas las acciones.
"""
import unittest
from time import sleep
from typing import Dict
# Similar al ejercicio (con variaciones mínimas):
# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/contar_vocales_consonantes_digitos.py


def contar(frase: str) -> Dict[str, int]:
    """Cuenta vocales, consonantes, mayúsculas, minúsculas y digitos de
    una frase.

    :param frase: La frase a contar.
    :frase type: str
    :return: Un diccionario con las cantidades de vocales, consonantes
        y digitos.
    :rtype: Dict[str, int]
    """
    frase: str = frase
    vocales: int = 0
    consonantes: int = 0
    mayusculas: int = 0
    minusculas: int = 0
    digitos: int = 0
    for caracter in frase:
        if caracter in "aeiouáéíóú" or caracter in "AEIOUÁÉÍÓÚ":
            vocales += 1
        if caracter in "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ":
            consonantes += 1
        if caracter in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ":
            mayusculas += 1
        if caracter in "abcdefghijklmnñopqrstuvwxyzáéíóú":
            minusculas += 1
        if caracter in "0123456789":
            digitos += 1
    return {
        "vocales": vocales, "consonantes": consonantes,
        "mayusculas": mayusculas, "minusculas": minusculas,
        "digitos": digitos,
    }


def mostrar(s: str) -> None:
    """Muestra una frase letra por letra."""
    for c in s:
        print(c, end="", flush=True)
        sleep(0.5)
    print()


def main():
    frase = input("Input: ")
    mostrar(frase)
    resultado = contar(frase)
    print(f"vocales: {resultado['vocales']}")
    print(f"consonantes: {resultado['consonantes']}")
    print(f"mayusculas: {resultado['mayusculas']}")
    print(f"minusculas: {resultado['minusculas']}")
    print(f"digitos: {resultado['digitos']}")


class Test(unittest.TestCase):

    def test_contar(self):
        self.assertEqual(
            contar("estoy programado en el 2020"),
            {
                "vocales": 8, "consonantes": 11,
                "mayusculas": 0, "minusculas": 19,
                "digitos": 4,
            }
        )
        self.assertEqual(
            contar("PRO CS1111"),
            {
                "vocales": 1, "consonantes": 4,
                "mayusculas": 5, "minusculas": 0,
                "digitos": 4,
            }
        )
        self.assertEqual(
            contar("Hola, ¿qué tal?"),
            {
                "vocales": 5, "consonantes": 5,
                "mayusculas": 1, "minusculas": 9,
                "digitos": 0,
            }
        )


if __name__ == '__main__':
    # unitttest.main()
    main()
