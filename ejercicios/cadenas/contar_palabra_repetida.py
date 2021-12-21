"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una cadena de caracteres y una palabra, contar cuántas veces se
repite dentro de la cadena.

NOTE: add docstring and tests.
"""


def contar_palabra(linea: str, palabra: str) -> int:
    return linea.count(palabra)


def contar_palabra_no_builtin(linea: str, palabra: str) -> int:
    i = 0
    for elemento in linea.split():
        if elemento == palabra:
            i += 1
    return i


def main():
    cadena = "La casa de la esquina tiene la puerta roja y la ventana"
    palabra = "la"
    print(contar_palabra(cadena, palabra)) # output: 3
    #print(contar_palabra_no_builtin(cadena, palabra)) # output: 3


if __name__ == "__main__":
    main()