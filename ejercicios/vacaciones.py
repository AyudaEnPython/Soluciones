"""
Una empresa necesita un programa el cual los empleados se puedan
registrar con un nombre y una contraseña, tambien que introduzcan los
años que llevan trabajando, y si lleva de 1 a 5 años puede tomar 10
dias de vacaciones, si tiene de 5 a 10 años tiene derecho a 15 dias de
vacaciones, y si tiene de 10 a 20 años tiene derecho a un mes de
vacaciones.
"""
import hashlib
import hmac
import os
from typing import Tuple 
from unittest import main, TestCase
from unittest.mock import patch

# opcional
empleados = []

# opcional
def hash_contraseña(s: str) -> Tuple[bytes, bytes]:
    salt = os.urandom(16)
    h = hashlib.pbkdf2_hmac("sha256", s.encode(), salt, 1000)
    return salt, h


def registrar() -> Tuple[str, str]:
    nombre = input("Nombre y Apellido: ")
    while True:
        contraseña = input("contraseña: ")
        confirmar = input("Confirmar contraseña: ")
        if contraseña == confirmar:
            print("Confirmacion de contraseña correcta!")
            break
        else:
            print("Digitar nuevamente la contraseña!")
    return nombre, contraseña


def tiempo_servicio() -> int:
    while True:
        años = input("años de servicio: ")
        try:
            años = int(años)
            if 0 <= años <= 20:
                return años
        except ValueError:
            print("Digitar nuevamente los años de servicios")


def dias(años: int) -> int:
    vacaciones = {1 < años <= 5: 10, 5 < años <= 10: 15, 10 < años <= 20: 30}
    return vacaciones[True]


def main_app():
    nombre, contraseña = registrar()
    años = tiempo_servicio()
    print(f"{nombre} tiene derecho a {dias(años)} dias de vacaciones")
    
    #opcional
    s, k = hash_contraseña(contraseña)
    empleados.append([nombre, s+k, años])


class Test(TestCase):
    
    inputs = ("john doe", "1234", "123", "1234", "1234")
    seniority = ("30", "40", "4")

    def test_hash(self):
        s, k = hash_contraseña("laviejaconfiable1234")
        self.assertTrue(
            hmac.compare_digest(
                k, hashlib.pbkdf2_hmac(
                    "sha256", "laviejaconfiable1234".encode(), s, 1000
                )
            )
        )

    @patch("builtins.input", side_effect=inputs)
    def test_registrar(self, mock_input):
        response = registrar()
        self.assertEqual(response, ("john doe", "1234"))
    
    @patch("builtins.input", side_effect=seniority)
    def test_tiempo_servicio(self, mock_input):
        response = tiempo_servicio()
        self.assertEqual(response, 4)

    def test_dias(self):
        self.assertEqual(dias(2), 10)
        self.assertEqual(dias(5), 10)
        self.assertEqual(dias(7), 15)
        self.assertEqual(dias(10), 15)
        self.assertEqual(dias(12), 30)
        self.assertEqual(dias(20), 30)


if __name__ == "__main__":
    # main() # uncomment this line and comment the next one to run the tests
    main_app()
