"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una función que cuente la cantidad de caracteres diferentes que
aparecen más de una vez en una cadena. Suponga que todas las cadenas se
componen unicamente de letras minúsculas del alfabeto inglés.
"""


def sol(s: str) -> int:
    """
    >>> sol("aaabccdde")
    3
    """
    d, i = {}, 0
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            i += 1 if d[c] == 1 else 0
            d[c] += 1
    return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
