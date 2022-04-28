"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. A través de la función ord_seleccion, escriba el código de una
    aplicación que permita buscar el mayor de todos los elementos de la
    lista de 3 elementos ingresados por el usuario.

2. Escriba una función que permita identificar si los elementos de una
    lista son positivos o negativos.

3. Escribir una función recursiva para replicar los elementos de una
    lista una cantidad `n` de veces. Por ejemplo, replicar
    ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])
    El segundo parámetro de replicar indica las veces que se debe
    repetir.

NOTA: el apartado 2 no es muy claro.
"""
from typing import List


def mayor(arr: List[int]) -> int:
    """
    >>> mayor([1, 3, 3, 7])
    7
    """
    return max(arr)


def es_positivo_o_negativo(arr: List[int]):
    """
    >>> es_positivo_o_negativo([1, 3, 3, 7])
    'Todos son positivos'
    """
    if all(x > 0 for x in arr):
        return "Todos son positivos"
    elif all(x < 0 for x in arr):
        return "Todos son negativos"
    else:
        return "Hay al menos uno positivo y uno negativo"


def duplicar(arr: List[int], n: int) -> List[int]:
    """
    >>> duplicar([1, 3, 3, 7], 2)
    [1, 3, 3, 7, 1, 3, 3, 7]
    """
    if n == 0:
        return []
    return arr + duplicar(arr, n - 1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
