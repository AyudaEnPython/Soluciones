"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List

TAG_SOL = ""


def numeros_enteros(inicio: int, cantidad: int) -> List[int]:
    """
    >>> numeros_enteros(10, 5)
    [10, 11, 12, 13, 14]
    """
    return [
        inicio + i for i in range(cantidad)
    ]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
