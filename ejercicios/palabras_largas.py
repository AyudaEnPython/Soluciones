"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe un programa que lea una cadena y un número entero k y muestre
el mensaje <<Hay palabras largas>> si alguna de las palabras de la
cadena son de longitud mayor o igual que k, y <<No hay palabras
largas>> en caso contrario.
"""
import io
from typing import Callable
from unittest import main, TestCase
from unittest.mock import patch


def f_a(s: str, n: int) -> bool:
    return any(len(e) >= n for e in s.split())


def f_b(s: str, n: int) -> bool:
    for e in s.split():
        if len(e) >= n:
            return True
    return False


def f_c(s: str, n: int) -> bool:
    return sum([True for e in s.split() if len(e) >= n])


def solver(f: Callable, s: str, n: int) -> None:
    """Evalua las palabras de una cadena de texto 's', si existe alguna
    palabra cuya longuitud es mayor o igual a 'n' imprime 'Hay palabras
    largas', de lo contrario imprime 'No hay palabras largas' 

    :param f: Función de evaluación
    :f type: Callable
    :param s: Cadena de texto a evaluar
    :s type: str
    :param n: Cantidad de caracteres
    :n type: int
    """
    print("Hay palabras largas" if f(s, n) else "No hay palabras largas")


class Test(TestCase):

    cases = (
        "This is a test",
        "  This is a test  ",
        " This    is  a   test  ",
    )
    output_true = "Hay palabras largas\n"
    output_false = "No hay palabras largas\n"

    def test_functions_true(self):
        for case in self.cases:
            self.assertTrue(f_a(case, 4))
            self.assertTrue(f_b(case, 4))
            self.assertTrue(f_c(case, 4))

    def test_functions_false(self):
        for case in self.cases:
            self.assertFalse(f_a(case, 5))
            self.assertFalse(f_b(case, 5))
            self.assertFalse(f_c(case, 5))
    
    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, f=None, args=None):
        if f and args is not None:
            f(*args)
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_solver(self):
        for f in (f_a, f_b, f_c):
            self.assert_stdout(
                self.output_true, f=solver, args=(f, "Hello World", 4)
            )


if __name__ == "__main__":
    main()
    # one-liner:
    # 
    # print(
    #   "Hay palabras largas" if any(len(e) >= 6 for e in input("> ").split())
    #   else "No hay palabras largas"
    #   )