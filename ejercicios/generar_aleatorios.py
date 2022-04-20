"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Original
--------
Generar una lista (el tamaño de la lista debe de generarse de manera
automática y aleatoriamente entre 1 y 20) con números generados de
manera automática aleatoriamente entre 1 y 100.
Enviar esa lista creada a una funcion para que esta halle el valor 
total de los los números de la lista generada.


Reformulado
-----------
Generar de forma automática una lista de tamaño aleatorio (entre 1 y
20) compuesto por números aleatorios (entre 1 y 100).
Crear una funcion que evalue la lista creada anteriormente y halle la
suma de todos los numeros de dicha lista.

TODO: add testcases
"""
from random import randint
from typing import List
from unittest import main, TestCase


def generar_aleatorios(
    min: int = 1,
    max: int = 100,
    size: int = 20
) -> List[int]:
    """
    Genera numeros aleatorios de tamaño variable

    :param min: Número aleatorio mínimo
    :min type: int
    :param max: Número aleatorio máximo
    :max type: int
    :param size: Tamaño máximo de la lista
    :size type: int
    :return: Lista de números enteros
    :rtype: List[int]
    """
    return [randint(min, max) for _ in range(size)]


def suma(numeros: List[int]) -> int:
    """Suma los elemntos de una lista

    :param numeros: Lista de números
    :numeros type: List[int]
    :return: Suma de los elemntos de la lista
    :rtype: int
    """
    return sum(numeros)


class Test(TestCase):

    def test_generar_aleatorios(self):
        return NotImplemented()


if __name__ == "__main__":
    main()