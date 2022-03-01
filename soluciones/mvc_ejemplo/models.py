"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from utils import aleatorios, Aleatorios


class Modelo:

    def __init__(self) -> None:
        self.numeros = aleatorios()

    def pares(self) -> Aleatorios:
        return [n for n in self.numeros if n % 2 == 0]

    def impares(self) -> Aleatorios:
        return [n for n in self.numeros if n % 2 != 0]

    def generar(self, size: int, min: int, max: int) -> None:
        self.numeros = aleatorios(size, min, max)
