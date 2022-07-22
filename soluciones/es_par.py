"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar dos números y mostrar cual de ellos es par o si ambos lo son.
"""
import unittest


def es_par(numero: int) -> bool:
    """Determina si un número es par o no.
    
    :param numero: Número a evaluar.
    :type numero: int
    :return: True si el número es par, False si no lo es.
    :rtype: bool
    """
    return numero % 2 == 0


def main():
    x = int(input("Ingrese un número: "))
    y = int(input("Ingrese otro número: "))

    if es_par(x) and es_par(y):
        print("Ambos son pares")
    elif es_par(x):
        print("El primero es par")
    elif es_par(y):
        print("El segundo es par")
    else:
        print("Ninguno es par")


class Test(unittest.TestCase):

    def test_es_par(self):
        self.assertTrue(es_par(2))
        self.assertTrue(es_par(4))
        self.assertFalse(es_par(3))
        self.assertFalse(es_par(5))


if __name__ == "__main__":
    # unittest.main() # uncomment this line and comment the next one to run tests
    main()
