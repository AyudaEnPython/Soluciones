"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un programa que pida una letra e indique si es una vocal o no.

NOTE: add docstrings and tests.
"""


def es_vocal(s: str) -> bool:
    return s in "aeiouAEIOU"


def main():
    s = input("Ingrese una letra: ")
    if es_vocal(s):
        print("La letra ingresada es una vocal.")
    else:
        print("La letra ingresada no es una vocal.")


if __name__ == "__main__":
    main()