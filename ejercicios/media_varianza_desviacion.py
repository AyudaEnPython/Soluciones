"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir una función que reciba una muestra de números en una lista y
devuelva un diccionario con su media, varianza y desviación estándar.
"""
from typing import Dict, List
from unittest import main, TestCase
from statistics import mean, pvariance, pstdev


def media_varianza_desviacion(numeros: List[float]) -> Dict[str, float]:
    """Calcula la media, varianza y desviación estándar de una muestra
    de números.

    :param numeros: Lista de números.
    :numeros type: List[float]
    :return: Tupla con la media, varianza y desviación estándar.
    :rtype: Dict[str, float]
    """
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    desviacion = varianza ** 0.5
    return {"media": media, "varianza": varianza, "desviacion": desviacion}


def main_():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    datos = media_varianza_desviacion(numeros)
    print(f"Media: {datos['media']}")
    print(f"Varianza: {datos['varianza']}")
    print(f"Desviación estándar: {datos['desviacion']}")


class Test(TestCase):

    def test_media_varianza_desviacion(self):
        n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        data = media_varianza_desviacion(n)
        self.assertEqual(data["media"], mean(n))
        self.assertEqual(data["varianza"], pvariance(n))
        self.assertEqual(data["desviacion"], pstdev(n))


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run tests
    main_()