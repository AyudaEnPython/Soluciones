"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que lea una lista de palabras ingresada por el
usuario y luego devuelva en pantalla la palabra que contenga más
vocales.

TODO: add testcases
"""
from typing import Dict

# utilizar cualquier función para contar vocales de:
# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/contar_vocales.py
# y modificar la función para que devuelva el total de vocales 


def contar_vocales_dc(s: str) -> Dict[str, int]:
    result = {vocal: s.lower().count(vocal) for vocal in "aeiou"}
    return sum(result.values())


def main():
    palabras = input(
        "Ingrese una lista de palabras separadas por espacios: "
    ).split()
    max_ = 0
    for i, palabra in enumerate(palabras):
        if contar_vocales_dc(palabra) >= max_:
            max_ = i
    print(f"La palabra con más vocales es: {palabras[max_]}")


if __name__ == "__main__":
    main()