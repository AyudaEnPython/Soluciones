"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado un número y su base, determine si el número pertenece a la base
ingresada; recuerde que un número pertenece a una base si sus digitos
son menores a la misma.

Ejemplo:
número = 101010 y base = 2. Como todos los dígito del número son
menores a 2, entonces: número pertenece a la base 2 (binario).
"""


def pertenece_a_base(ns: str, b: int) -> bool:
    """Determina si un número pertenece a una base dada.

    :param ns: Número a evaluar.
    :type ns: str
    :param b: Base a evaluar.
    :type b: int
    :return: True si pertenece a la base, False en caso contrario.
    >>> pertenece_a_base('35235', 6)
    True
    >>> pertenece_a_base('35235', 5)
    False
    """
    for n in ns:
        if int(n) >= b:
            return False
    return True


def main():
    n = input('Ingrese un número: ')
    b = int(input('Ingrese la base: '))
    if pertenece_a_base(n, b):
        print(f'El número {n} pertenece a la base {b}')
    else:
        print(f'El número {n} no pertenece a la base {b}')


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main()
