"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir una función que reciba una muestra de números en una lista y
devuelva un diccionario con su media, varianza y desviación estándar.
"""
import unittest
from statistics import mean, pvariance, pstdev, stdev
from typing import Dict, List


def media_varianza_desviacion(numeros: List[float]) -> Dict[str, float]:
    """Calcula la media, varianza y desviación estándar de una población.

    :param numeros: Lista de números.
    :numeros type: List[float]
    :return: Tupla con la media, varianza y desviación estándar de una
        población.
    :rtype: Dict[str, float]
    """
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desviacion = varianza ** 0.5
    return {"media": media, "varianza": varianza, "desviacion": desviacion}


def stdev_(numeros: List[float]) -> float:
    """Calcula la desviación estándar de una muestra de números.

    :param numeros: Lista de números.
    :numeros type: List[float]
    :return: Desviación estándar de la muestra.
    :rtype: float
    """
    return (
        sum((x - (sum(numeros) / len(numeros))) ** 2 for x in numeros) /
        (len(numeros) - 1)
    ) ** 0.5


def main_():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    datos = media_varianza_desviacion(numeros)
    print(f"Media: {datos['media']}")
    print(f"Varianza: {datos['varianza']}")
    print(f"Desviación estándar: {datos['desviacion']}")


class Test(unittest.TestCase):

    def test_media_varianza_desviacion(self):
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = media_varianza_desviacion(n)
        self.assertEqual(data["media"], mean(n))
        self.assertEqual(data["varianza"], pvariance(n))
        self.assertEqual(data["desviacion"], pstdev(n))

    def test_media(self):
        n = [1, 2, 3, 4.5, 5.6, 6, 7, 8, 9, 10]
        self.assertEqual(sum(n)/len(n), 5.61)

    def test_stdev(self):
        n = [1, 2, 3, 4.5, 5.6, 6, 7, 8, 9, 10]
        self.assertEqual(stdev_(n), 2.9979437397434037)
        self.assertEqual(stdev_(n), stdev(n))


if __name__ == "__main__":
    unittest.main()  # uncomment/comment to run tests
    # main_()
