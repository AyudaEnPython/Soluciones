"""
Eliminar de una lista o arreglo, el elemento que está en la posición
media. Si la dimensión del arreglo es par, sacar el elemento previo
al punto medio.
"""
from typing import Any
from unittest import main, TestCase


def eliminar(arr: list, tmp: Any = None) -> list:
    """Elimina el elemento en la posicion media. Si el tamaño es
    par, elimina el elemento previo al punto medio.

    :param arr: Secuencia de elementos
    :arr type: list
    :param tmp: Ultimo elemento de la secuencia
    :tmp type: Any
    :return: Secuencia sin el elemento de la posicion media
    :rtype: list

    >>> eliminar([1, 2, 3])
    [1, 3]
    >>> eliminar([1, 2, 3, 4])
    [1, 3, 4]
    >>> eliminar(['x', 'y'])
    ['y']
    >>> eliminar(['a'])
    []
    """
    if len(arr) <= 2:
        arr.pop(0)
        return arr
    elif len(arr) % 2 == 1:
        arr.pop(len(arr)//2)
        if tmp is not None:
            arr.append(tmp)
        return arr
    else:
        tmp = arr.pop(-1)
        return eliminar(arr, tmp=tmp)


class Test(TestCase):

    def test_eliminar(self):
        self.assertEqual(eliminar([True, False]), [False])
        self.assertEqual(eliminar([True]), [])
        self.assertEqual(eliminar([1, 2, 3, 4, 5]), [1, 2, 4, 5])
        self.assertEqual(eliminar([1, 2, 3, 4, 5, 6]), [1, 2, 4, 5, 6])
        self.assertEqual(eliminar(["1", "2", "3"]), ["1", "3"])
        self.assertEqual(eliminar(["a", "b", "c", "d"]), ["a", "c", "d"])
        self.assertEqual(eliminar(["a", "b", "c", "d", "e"]), ["a", "b", "d", "e"])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()