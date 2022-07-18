"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que lea la hora en notación de 24 horas y que
imprima en notación de 12; por ejemplo, si la entrada es 13:45, la
salida será 1:45 PM. El programa debe solicitar al usuario que 
introduzca exactamente cinco caracteres para especificar una hora; por
ejemplo, las 9 en punto se debe introducir así: 09:00.
"""
import unittest


def convertir(hora: str) -> str:
    """Convierte una hora en notación de 24 horas a 12 horas.

    :param hora: Hora a convertir
    :hora type: str
    :return: Hora en notación de 12 horas
    :rtype: str
    """
    hora_24 = int(hora[:2])
    hora_12 = 12 if hora_24 % 12 == 0 else hora_24 % 12
    return f"{hora_12}:{hora[3:]} {'AM' if hora_24 < 12 else 'PM'}"


def main():
    hora = input("Ingrese una hora en formato de 24 horas: ")
    print(convertir(hora))


class Test(unittest.TestCase):

    def test_convertir(self):
        self.assertEqual(convertir("13:45"), "1:45 PM")
        self.assertEqual(convertir("09:00"), "9:00 AM")
        self.assertEqual(convertir("23:00"), "11:00 PM")
        self.assertEqual(convertir("00:00"), "12:00 AM")
        self.assertEqual(convertir("00:01"), "12:01 AM")
        self.assertEqual(convertir("12:00"), "12:00 PM")
        self.assertEqual(convertir("12:01"), "12:01 PM")


if __name__ == "__main__":
    # unittest.main() # uncomment this line and comment the next one to run tests
    main()
