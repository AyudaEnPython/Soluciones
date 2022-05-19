"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se darán dos vectores X e Y de tamaños N y M, se pide obtener un vector
que contenga los elementos que aparecen en AMBOS vectores sin
repeticiones. (Si no exisitiese ningún elemento que cumpla esto mostrar
un vector vacío "[]" como respuesta)

N = 7, X =  [14, 78, 59, 1, 3, 8, 7]
M = 8, Y =  [1, 0, 14, 14, 3, 3, 3, 10]        -> Respuesta: [14, 1, 3]

N = 9, X =  [73, 195, 61, 146, 167, 84, 109, 55, 195]
M = 5, Y =  [195, 64, 134, 36, 78]             -> Respuesta: [195]

N = 8, X =  [1, 2, 3, 4, 5, 6, 7, 2]
M = 5, Y =  [2, 4, 6, 8, 10]                   -> Respuesta: [2, 4, 6]
"""
from typing import List

Vector = List[int]


def sin_repeticion(x: Vector, y: Vector) -> Vector:
    """Retorna un vector con los elementos que aparecen en ambos vectores
    sin repeticiones. Si no existe ningún elemento en común retorna un
    vector vacío.

    :param x: primer vector
    :x type: Vector
    :param y: segundo vector
    :y type: Vector
    :return: vector con elementos en común
    :rtype: Vector

    >>> sin_repeticion([14, 78, 59, 1, 3, 8, 7], [1, 0, 14, 14, 3, 3, 3, 10])
    [1, 3, 14]
    >>> sin_repeticion( \
        [73, 195, 61, 146, 167, 84, 109, 55, 195], [195, 64, 134, 36, 78] \
    )
    [195]
    >>> sin_repeticion([1, 2, 3, 4, 5, 6, 7, 2], [2, 4, 6, 8, 10])
    [2, 4, 6]
    >>> sin_repeticion([1, 2], [3, 4])
    []
    """
    return list(set(x) & set(y))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
