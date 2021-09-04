"""
Calcular el cuadrado de un número si este es impar o el cubo
si el número es par.

Por ejemplo, para 4 deberá retornar 64 y para 3 retornar 9.
"""
from unittest import main, TestCase

def solucion(n: int) -> int:
    """Devuelve n^3 si 'n' es par y n^2 si 'n' es impar.

    :param n: Número
    :type n: int
    :return: Número elevada a al cubo o al cuadrado
    :rtype: int
    
    >>> solucion(3)
    9
    >>> solucion(4)
    64
    """
    if n % 2 != 0:
        return n**2
    else:
        return n**3


class Test(TestCase):

    def test_solucion(self):
        self.assertEqual(solucion(5), 25)
        self.assertEqual(solucion(6), 216)
        self.assertEqual(solucion(12), 1728)
        self.assertEqual(solucion(13), 169)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()