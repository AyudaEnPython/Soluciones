"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un algoritmo que imprima el promedio de los primeros N números
positivos que son divisibles entre 3 y 5 comenzando con el número 0.
Recuerde validadr N. Recuerde que puede utilizar el operador %.

1. Cálculo del promedio
2. Validar la variable N
3. Documentación

Por ejemplo, para N=100, el promedio es 45.0
El promedio es = 0 + 15 + 30 + 45 + 60 + 75 + 90 = 315/7 = 45.0

Datos de prueba:
N:100  Promedio: 45.0
N:3500 Promedio: 1747.5
N:10   Promedio: 0.0
N:500  Promedio: 247.5
"""
from typing import Optional
from unittest import main, TestCase
from unittest.mock import patch


def es_divisible_3_y_5(n: int) -> bool:
    """Comprueba si el número es divisible entre 3 y 5

    :param n: Número a evaluar.
    :n type: int
    :return: True si es divisible entre 3 y 5, False de lo contrario
    :rtype: bool
    """
    if n % 3 == 0 and n % 5 == 0:
        return True
    return False


def validar_entrada(msg: Optional[str] = "n: ") -> int:
    """Devuelve un valor númerico entero.

    :param msg: Indicación al momento de ingresar una entrada.
    :msg type: str, optional
    :return: Valor númerico entero
    :rtype: int
    """
    while True:
        try:
            s = input(msg)
            if int(s) >= 0:
                return int(s)
            else:
                print("No se admiten negativos")
        except ValueError:
            print("Solo se admiten números enteros positivos")


def main_():
    n = validar_entrada()
    t, i = 0, 0
    for x in range(n+1):
        if es_divisible_3_y_5(x):
            i += 1
            t += x
    return t / i


class Test(TestCase):

    inputs = ("100", "3500", "10", "500")
    results = (45.0, 1747.5, 0.0, 247.5)

    def test_divisibilidad(self):
        self.assertEqual(es_divisible_3_y_5(15), True)
        self.assertFalse(es_divisible_3_y_5(10))

    @patch("builtins.input", side_effect=("-1", "10.5", "20"))
    def test_entrada(self, mocked_input):
        result = validar_entrada()
        self.assertEqual(result, 20)

    @patch("builtins.input", side_effect=inputs)
    def test_main(self, mocked_input):
        for result in self.results:
            response = main_()
            self.assertEqual(response, result)


if __name__ == "__main__":
    main()
