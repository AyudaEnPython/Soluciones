"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un grupo de científicos está analizando una forma de vida inteligente
extraterrestre en la reconocida área 52. Han descubierto que,
sorprendentemente, estos usan las mismas letras que nosotros (26
letras, excluyendo la ñ) aunque su alfabeto posee un orden distinto.
Se nos encomienda la tarea de reordenar un diccionario en español para
que los extraterrestres puedan buscar palabras en nuestra lengua más
fácilmente. Diseñar un algoritmo que dada un string que representa
todas las letras del alfabeto ordenadas según los extraterrestres y una
lista de palabras, devuelva una lista de palabras ordenadas (en el
orden que entiendan los extraterrestres)

Ejemplo:

lista = ["miel", "extraterrestre", "al", "automovil", "auto", "revestir"]
alfabeto = "zyxwvutsrqponmlkjihgfedcba"

ordenada = ["revestir", "miel", "extraterrestre", "auto", "automovil", "al"]

NOTE: La lista ordenada del ejemplo tiene un error.
"""
from typing import List

palabras = ["miel", "extraterrestre", "al", "automovil", "auto", "revestir"]


def f(arr: List[str]) -> List[str]:
    return sorted(arr, reverse=True)


def main():
    print(f(palabras))


if __name__ == "__main__":
    main()
