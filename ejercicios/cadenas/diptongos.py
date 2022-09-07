"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una cadena de caracteres, imprimir todas las palabras que no sean
diptongos.

NOTE: add docstring and tests.
"""
import re


def es_diptongo(s: str, n: int = 2) -> bool:
    """Determina si una cadena es un diptongo (n=2).

    :param s: cadena de caracteres
    :s type: str
    :param n: longitud, por defecto 2 (diptongo)
    :n type: int
    :return: True si es diptongo (n=2), False si no lo es
    """
    regex = n * "[aeiou]"
    return re.search(regex, s) is not None


def main():
    s = ("baile", "ejemplo", "auto", "veinte", "cadena", "hielo", "color")
    for i in s:
        if not es_diptongo(i):
            print(i)


if __name__ == "__main__":
    main()
