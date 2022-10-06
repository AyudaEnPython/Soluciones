"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elabora un programa en Python que estime el tipo de cambio en el
futuro. El programa debe solicitar al usuario: el tipo de cambio
actual, la tasa de interés local, la tasa de interés extranjero y los
días a futuro. La fórmula para estimar el tipo de cambio a futuro
(forward) es la siguiente, deberás implementarla como una función.

        +-----------------------------------------------+
        | forward = tc * ((1 + til)/(1 + tie))**(n/365) |
        |                                               |
        | Donde:                                        |
        |   forward: Tipo de cambio a futuro            |
        |   tc: Tipo de cambio actual                   |
        |   til: Tasa de interés local                  |
        |   tie: Tasa de interés extranjero             |
        |   n: Número días a futuro                     |
        +-----------------------------------------------+

El sistema debe:
    1. Tener un menú de opciones para que el usuario:
        a. Cambie tasas de interés (ambas: local y extranjera).
        b. Cambie tipo de cambio actual.
        c. Cambie el número de días a futuro.
        d. Terminar el programa.

** Cada vez que cambie un dato el usuario, el programa deberá
recalcular e imprimir el forward.

Ejemplo estimación tipo de cambio:

    +----------------------------------------------------+
    | Tipo cambio spot: 20.4833 MXN/USD                  |
    | Tasa de interés local (México): 4.25%              |
    | Tasa de interés extranjera (USA): 0.25%            |
    | Dentro de: 200 días                                |
    |                                                    |
    | forward                                            |
    | = 20.4833 * ((1 + 0.0425)/(1 + 0.0025))**(200/365) |
    | = 20.4833 * (1.0399)**(0.5479)                     |
    | = 20.4833 * 1.0217 = 20.9272                       |
    +----------------------------------------------------+
"""
import unittest
from dataclasses import dataclass
# pip install prototools
from prototools import float_input, Menu


def cambio_a_futuro(tc, tiL, tiE, n):
    """Estima el tipo de cambio a futuro

    :param tc: Tipo de cambio actual
    :param til: Tasa de interés local
    :param tiE: Tasa de interés extranjero
    :param n: Número días a futuro
    """
    tiL = tiL / 100
    tiE = tiE / 100
    return round(tc * ((1 + tiL)/(1 + tiE))**(n/365), 4)


@dataclass
class Conversor:
    tc: float
    tiL: float
    tiE: float
    n: int

    def calcular(self) -> float:
        return cambio_a_futuro(self.tc, self.tiL, self.tiE, self.n)


def tasa_interes(conversor: Conversor) -> None:
    conversor.til = float_input("Tasa de interés local: ")
    conversor.tie = float_input("Tasa de interés extranjera: ")
    print(conversor.calcular())


def tipo_cambio(conversor: Conversor) -> None:
    conversor.tc = float_input("Tipo de cambio: ")
    print(conversor.calcular())


def dias_futuro(conversor: Conversor) -> None:
    conversor.n = float_input("Días a futuro: ")
    print(conversor.calcular())


def main():
    conversor = Conversor(20.4833, 4.25, 0.25, 200)
    menu = Menu("Tipo de cambio en el futuro")
    menu.add_options(
        ("Tasas de interés", lambda: tasa_interes(conversor)),
        ("Tipo de cambio actual", lambda: tipo_cambio(conversor)),
        ("Número de días a futuro", lambda: dias_futuro(conversor)),
    )
    menu.run()


class Test(unittest.TestCase):

    def test_cambio_a_futuro(self):
        self.assertEqual(cambio_a_futuro(20.4833, 4.25, 0.25, 200), 20.9272)


if __name__ == '__main__':
    # unittest.main() # uncomment/comment to run tests
    main()
