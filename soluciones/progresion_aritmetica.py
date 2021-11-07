"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Optional, Tuple
from unittest import main, TestCase


def solucion(
    a:int , d: int, n: int, t: Optional[int] = None
) -> Tuple[int, float]:
    """Encuentra el n-ésimo termino y calcula suma de los 'n' terminos
    de una progresión aritmética.

    :param a: Primer termino de la progresión aritmética
    :type a: int
    :param diferencia: Diferencia constante de la progresión aritmética
    :type diferencia: int
    :param n: Número de terminos de la progresión aritmética
    :type n: int
    :param t: Último termino de la progresión aritmética
    :type t: int, optional
    :return: Tupla (n-ésimo termino, suma de la progresión) 
    :rtype: Tuple[int, float]

    >>> solucion(1, 1, 100)
    (100, 5050.0)
    >>> solucion(9, 12, 20)
    (237, 2460.0)
    >>> solucion(1, 2, None, t=19)
    (19, 100.0)
    """
    if t and n is None:
        a_n = t
        n = (t - a + d) / d
        s = ((a+a_n) * n) / 2
    else:
        a_n = a + (n-1) * d
        s = (n/2) * (2*a + (n-1)*d)
    return a_n, s


class TestSolucion(TestCase):

    def test_solucion(self):
        self.assertEqual(solucion(1, 2, 5), (9, 25))
        self.assertEqual(solucion(2, 2, 5), (10, 30))
        self.assertEqual(solucion(2.5, 1.5, 20), (31, 335))
        self.assertEqual(solucion(-8, -7, 60), (-421, -12870.0))
        self.assertEqual(solucion(-5, 2, 60), (113, 3240))
        self.assertEqual(solucion(40, 8, None, 3152), (3152, 622440.0))
        self.assertEqual(solucion(80, 8, None, 2072), (2072, 269000.0))


if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    main()