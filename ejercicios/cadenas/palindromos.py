"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una cadena de caracteres, imprimir todas las palabras que sean
palíndromos.

NOTE: add docstring and tests.
"""


def es_palindromo_naive(s: str) -> str:
    return s == s[::-1]


def es_palindromo_alt(s: str) -> str:
    s = s.replace(" ", "").lower().replace(",", "")
    return s == s[::-1]


def main():
    s = (
        '  Anita   lava   la tina'
        '    Anita LaVa la Ti nA',
        'No lemon, no melon',
        'Red rum, sir, is murder',
        'Sé verlas al revés',
        'estandarte',
    )
    for i in s:
        if es_palindromo_alt(i):
            print(i)


if __name__ == "__main__":
    main()