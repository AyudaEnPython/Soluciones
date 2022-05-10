"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import re
import unittest


PATTERN = re.compile(
    r"^(3[01]|[12][0-9]|0[1-9])/"
    r"(1[0-2]|0[1-9])/"
    r"(?:[0-9]{2})?[0-9]{2}$"
)


def validar_fecha(fecha):
    return True if re.search(PATTERN, fecha) else False


def main():
    fecha = input("Introduce una fecha (dd/mm/aaaa): ")
    if validar_fecha(fecha):
        print("La fecha es válida")
    else:
        print("La fecha es inválida")


class Test(unittest.TestCase):

    def test_validar_fecha(self):
        self.assertEqual(validar_fecha("0/0/0000"), False)
        self.assertEqual(validar_fecha("00/00/00"), False)
        self.assertEqual(validar_fecha("31/31/2022"), False)
        self.assertEqual(validar_fecha("99/99/9999"), False)
        self.assertEqual(validar_fecha("35/12/2020"), False)
        self.assertEqual(validar_fecha("32/02/2020"), False)
        self.assertEqual(validar_fecha("01/01/22"), True)
        self.assertEqual(validar_fecha("01/01/2022"), True)
        self.assertEqual(validar_fecha("11/01/2022"), True)
        self.assertEqual(validar_fecha("31/01/2022"), True)
        self.assertEqual(validar_fecha("01/02/2022"), True)


if __name__ == '__main__':
    #unittest.main()
    main()
