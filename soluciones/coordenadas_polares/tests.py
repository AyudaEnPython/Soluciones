"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import random
from unittest import main, TestCase

from modelos import Punto
from utils import crear_coordenadas, mostrar


class TestCoordenadas(TestCase):

    def test_punto(self):
        punto = Punto()
        self.assertEqual(punto.x, 0)
        self.assertEqual(punto.y, 0)

    def test_punto_representacion(self):
        p = Punto(1, 1)
        self.assertEqual(repr(p), "(1, 1)")

    def test_cuadrante(self):
        p = Punto(1, 1)
        self.assertEqual(
            p.cuadrante(), "(1, 1) se encuentra en el I° cuadrante."
        )
        p = Punto(-1, 1)
        self.assertEqual(
            p.cuadrante(), "(-1, 1) se encuentra en el II° cuadrante."
        )
        p = Punto(-1, -1)
        self.assertEqual(
            p.cuadrante(), "(-1, -1) se encuentra en el III° cuadrante."
        )
        p = Punto(1, -1)
        self.assertEqual(
            p.cuadrante(), "(1, -1) se encuentra en el IV° cuadrante."
        )
        p = Punto(0, 1)
        self.assertEqual(
            p.cuadrante(), "(0, 1) se encuentra en el eje Y."
        )
        p = Punto(1, 0)
        self.assertEqual(
            p.cuadrante(), "(1, 0) se encuentra en el eje X."
        )
        p = Punto(0, 0)
        self.assertEqual(
            p.cuadrante(), "(0, 0) se encuentra en el origen."
        )


class TestUtils(TestCase):

    def test_crear_coordenadas_valores(self):
        random.seed(1337)
        punto = crear_coordenadas(Punto, n=1)[0]
        self.assertEqual(punto.x, 9)
        self.assertEqual(punto.y, 7)

    def test_crear_coordenadas_longuitud(self):
        coordenadas = crear_coordenadas(Punto)
        self.assertEqual(len(coordenadas), 4)

    def test_crear_coordenadas_parametros(self):
        coordenadas = crear_coordenadas(Punto, n=3)
        self.assertEqual(len(coordenadas), 3)
        rango = (-2, 2)
        punto = crear_coordenadas(Punto, rango=rango, n=1)[0]
        self.assertNotEqual(punto.x, random.randint(3, 10))
        self.assertNotEqual(punto.y, random.randint(-10, -3))


if __name__ == "__main__":
    main()
