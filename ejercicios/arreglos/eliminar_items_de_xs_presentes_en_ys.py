"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que permita crear dos listas de palabras y que, a
continuación elimine de la primera lista los nombres de la segunda
lista.

NOTE: No es aconsejable remover elementos de una lista mientras esta
    se esta iterando sobre ella.
"""
from random import sample, randint
from string import ascii_lowercase
from typing import List


def crear_lista_de_palabras(n: int) -> List[str]:
    """Retorna una lista con n palabras aleatorias.

    :param n: Número de palabras
    :type n: int
    :return: Lista de palabras
    :rtype: List[str]
    """
    return sample(ascii_lowercase, n)


def eliminar(xs: List[str], ys: List[str]) -> List[str]:
    """Elimina de la primera lista los nombres de la segunda lista.

    :param xs: Primera lista de palabras
    :type xs: List[str]
    :param ys: Segunda lista de palabras
    :type ys: List[str]
    :return: Lista de palabras sin nombres de la segunda lista
    :rtype: List[str]
    """
    return [x for x in xs if x not in ys]


def main():
    a = crear_lista_de_palabras(randint(5, 12))
    b = crear_lista_de_palabras(randint(5, 12))
    print(eliminar(a, b))


if __name__ == "__main__":
    main()
