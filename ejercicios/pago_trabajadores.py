"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una empresa desea sistematizar el pago de sus trabajadores, para ello
se conoce la cantidad de horas trabajadas, el tipo de trabajador y los
años laborados. Considera lo siguiente:

- El pago por hora depende del tipo de trabajador (tiempo completo o
    tiempo parcial) por lo que crea una función que devuelva dicho
    valor según el tipo de trabajador. Propón los montos.
- El trabajador recibe una bonificación por los años laborados, para
    ello realiza una función que considere 3 intervalos de años para
    devolver el monto propuesto.
- El pago será la cantidad de horas laboradas, multiplicada por el
    precio, agregando el monto de la bonificación.
- Muestra en la salida los resultados: pago por hora, bonificación,
    pago total.

NOTE: Se opta por mejorar el diseño, por ello el tipo pasa a ser un
    diccionario.
"""
import unittest
# pip install prototools
from prototools import int_input, menu_input

TIPO = {"completo": 20, "parcial": 12}


def calcular_bonificacion(año: int) -> float:
    rango = {
        año < 3: 1000,
        3 <= año < 5: 1500,
        5 <= año < 10: 2000,
        10 <= año: 5000,
    }
    return rango[True]


def monto(horas, tipo, años):
    return horas * TIPO[tipo] + calcular_bonificacion(años)


def main_():
    horas = int_input("Horas trabajadas: ")
    tipo = menu_input(tuple(TIPO.keys()), numbers=True)
    años = int_input("Años laborados: ", min=0)
    print(f"Pago por hora: {TIPO[tipo]}")
    print(f"Bonificación: {calcular_bonificacion(años)}")
    print(f"Pago total: {monto(horas, tipo, años)}")


class Test(unittest.TestCase):

    def test_tipo(self):
        self.assertEqual(TIPO["completo"], 20)
        self.assertEqual(TIPO["parcial"], 12)

    def test_calcular_bonificacion(self):
        self.assertEqual(calcular_bonificacion(2), 1000)
        self.assertEqual(calcular_bonificacion(4), 1500)
        self.assertEqual(calcular_bonificacion(9), 2000)
        self.assertEqual(calcular_bonificacion(12), 5000)

    def test_monto(self):
        self.assertEqual(monto(120, "completo", 2), 3400)
        self.assertEqual(monto(80, "parcial", 4), 2460)


if __name__ == "__main__":
    # unittest.main() # uncomment/comment to run tests
    main_()
