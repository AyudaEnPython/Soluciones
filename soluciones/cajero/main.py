"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original ------------------------- 
Se pide desarrollar en Python un programa para la siguiten situación:
Se trata de desarrollar un sistema que emule el funcionamiento de un
cajero automático con las siguientes funciones:

1. Al inicio el usuario introduce su número de cuenta (o tarjeta) y el
    NIP, el sistema debe validar que el NIP sea correcto.
2. El usuario tiene las siguientes opciones que el cajero muestra como
    menú:
    a. Hacer un retiro, en este caso se introduce la cantidad a retirar
        se debe validar que el saldo de la cuenta tenga suficiente
        dinero, si no se rechaza la operación.
    b. Hacer un depósito en efectivo, esto se agrega al saldo actual.
    c. Depositar un cheque a la cuenta (es un cajero moderno, puede
        recibir cheques) en este caso también se introduce el monto del
        cheque y se incrementa el saldo.
3. El usuario puede pedir consultar el saldo en cualquier momento.
4. El usuario puede pedir ver los últimos 5 movimientos (un movimiento
    es una operación sobre la cuenta) y el promedio de estos
    movimientos.
5. El usuario puede pedir saber cuál fue el movimiento más importante
    (en monto) de sus últimos 5 moviemientos (toma en cuenta el caso
    que haya menos de 5 movimientos o ninguno).
6. Al terminar una operación, el sistema regresa al menú principal
    donde haya una opción de salir del sistema, en este caso el sistema
    se despide del cliente.
# ---------------------------------------------------------------------

Nota: Se opta por usar POO para mejorar el diseño.
"""
# pip install prototools
from prototools import Menu, float_input

from sistema.banco import Banco
from sistema.comandos import Depositar, Retirar
from sistema.controlador import BancoControlador
from sistema.cuenta import Cuenta


def cargar_cuentas(banco: Banco) -> None:
    banco.crear_cuenta("AAA", "1", "1234"),
    banco.crear_cuenta("BBB", "2", "1234"),
    banco.crear_cuenta("CCC", "3", "1234"),


def ingresar(banco: Banco) -> None:
    while True:
        numero = input("Ingrese su número de cuenta: ")
        nip = input("Ingrese su NIP: ")
        try:
            cuenta = banco.cuenta(numero)
            if cuenta.pin == nip:
                break
            else:
                print("NIP incorrecto")
        except KeyError:
            print("Número de cuenta incorrecto")
    return cuenta


class Cajero:

    def __init__(self, banco: Banco, cuenta: Cuenta) -> None:
        self.banco = banco
        self.cuenta = cuenta
        self.controlador = BancoControlador()
    
    def depositar(self) -> None:
        monto = float_input("Monto a depositar: ")
        self.controlador.registrar(Depositar(self.cuenta, monto))
        self._auto()

    def retirar(self) -> None:
        monto = float_input("Monto a retirar: ")
        try:
            self.controlador.registrar(Retirar(self.cuenta, monto))
            self._auto()
        except ValueError as e:
            print(e)
            self.controlador.deshacer()

    def movimientos(self) -> None:
        self._auto()
        self.controlador.ver_movimientos()
    
    def saldo(self) -> None:
        self._auto()
        print(f"Saldo disponible: ${self.cuenta.balance}")

    def _auto(self) -> None:
        self.banco.clear()
        self.controlador.calcular_balance()


def main():
    banco = Banco()
    cargar_cuentas(banco)
    
    cuenta = ingresar(banco)
    cajero = Cajero(banco, cuenta)
    menu = Menu("Cajero Automático")
    menu.add_options(
        ("Depositar", cajero.depositar),
        ("Retiro", cajero.retirar),
        ("Saldo", cajero.saldo),
        ("Movimientos", cajero.movimientos),
    )
    menu.run()


if __name__ == '__main__':
    main()