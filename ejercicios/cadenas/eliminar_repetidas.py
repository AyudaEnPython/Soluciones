"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una cadena de caracteres, eliminar las palabras que se repiten más
de tres veces e imprimir el resto.

NOTE: add tests.
"""


def eliminar_repetidas(cadena: str) -> str:
    """Elimina las palabras que se repiten más de tres veces.

    :param cadena: cadena de caracteres.
    :cadena type: str
    :return: cadena sin las palabras repetidas más de tres veces.
    :rtype: str
    """
    return " ".join([i for i in cadena.split() if cadena.count(i) <= 3])


def main():
    cadena = "aaa bb aaa bb cc aaa ddd bbb eee aaa"
    print(eliminar_repetidas(cadena))  # output: bb bb cc ddd bbb eee


if __name__ == "__main__":
    main()
