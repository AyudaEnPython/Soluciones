"""
Desarrollar una función que reciba una cadena de texto y que retorne la misma
cadena sin letras en mayúscula.

>>> f('Nuestro planeta debe cuidarse. Hagámoslo HOY.')
'uestro planeta debe cuidarse. agámoslo .'
"""
from unittest import main, TestCase


mensaje = "Nuestro planeta debe cuidarse. Hagámoslo HOY."


def solucion_a(texto: str) -> str:
    """Devuelve el texto ingresado sin mayúsculas.

    :param texto: Texto
    :type texto: str
    :return: Texto ingresado sin mayúsculas
    :rtype: str
    """
    resultado = ""
    for letra in texto:
        if not letra.isupper():
            resultado += letra
    return resultado


def solucion_b(texto: str) -> str:
    """Devuelve el texto ingresado sin mayúsculas.

    :param texto: Texto
    :type texto: str
    :return: Texto ingresado sin mayúsculas
    :rtype: str
    """
    return "".join([letra for letra in texto if not letra.isupper()])


class Test(TestCase):

    def test_solucion(self):
        self.assertEqual(solucion_a(mensaje), "uestro planeta debe cuidarse. agámoslo .")
        self.assertEqual(solucion_b(mensaje), "uestro planeta debe cuidarse. agámoslo .")


if __name__ == "__main__":
    main()