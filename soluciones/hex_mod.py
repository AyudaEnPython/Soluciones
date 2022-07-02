"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from unittest import main, TestCase


def solucion(source: str, target: str, steps: int = 6, take: int = 2) -> str:
    """Toma una cantidad determinada de valores de una cadena fuente
    y las inserta en un número determinado de posiciones de la cadena 
    destino.

    :param source: Cadena de texto fuente de la cual tomar valores
    :type source: str
    :param target: Cadena de texto de destino a insertar valores
    :type target: str
    :param steps: Cantidad de pasos (posiciones)
    :type target: int
    :param take: Cantidad de valores a tomar
    :type take: int
    :return: Cadena destino con los valores de la fuente insertados
    :rtype: str

    :Example:

    >>> resultado = solucion("E4F7", "FFD7FFA3EE5D")
    >>> print(resultado)
    FFD7FFE4A3EE5DF7

    .. note:: Cambiar el nombre de la función a uno mas apropiado
    """
    return "".join(
        [target[pos*steps:pos*steps+steps] + source[pos*take:pos*take+take]
        for pos in range(len(target)//steps)]
    )


class Test(TestCase):

    def test_solucion(self):
        self.assertEqual(
            solucion(
                "0000fe0f90af6e2fd04e000000000000",
                ("000000ffffffd7d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7d7"
                "d7d7d7d7d7d7000000000000000000000000000000000000")
            ),
            ("00000000ffffff00d7d7d7fed7d7d70fd7d7d790d7d7d7afd7d7d76ed7d7d72f"
            "d7d7d7d0d7d7d74e000000000000000000000000000000000000000000000000")
        )
        self.assertEqual(
            solucion("F7E24E", "00AFEA55E97A", steps=4, take=2),
            "00AFF7EA55E2E97A4E"
        )
        self.assertEqual(
            solucion("e4f7e9a8", "000000000", steps=3, take=4),
            "000e4f7000e9a8000"
        )
        self.assertEqual(
            solucion("e4b2", "ffff", steps=1, take=1),
            "fef4fbf2"
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
