"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from doctest import testmod


def contar(cadena: str) -> int:
    """Retorna la cantidad de caracteres alfabéticos distintos en la
    cadena ingresada sin ditinguir mayúsculas, minúsculas ni caracteres
    con tilde.

    :param cadena: cadena de caracteres
    :cadena type: str
    :return: cantidad de caracteres
    :rtype: int

    >>> contar("Aaaaáb")
    2
    >>> contar("$_12 3*")
    0
    >>> contar("Algoritmos y Programación 1")
    13
    >>> contar("Hola mundo")
    8
    >>> contar("")
    0
    """
    return len([
        c for c in set(cadena.lower()) if c.isalpha() and c not in "áéíóú"
    ])


if __name__ == "__main__":
    testmod()
