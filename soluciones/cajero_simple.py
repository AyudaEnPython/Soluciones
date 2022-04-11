"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import Menu, float_input


class Cajero(Menu):

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.add_options(
            ("Depositar", self.depositar),
            ("Retirar", self.retirar),
            ("Saldo", self.saldo),
        )

    def depositar(self):
        n = float_input("Monto a depositar: ", min=0)
        self.balance += n

    def retirar(self):
        n = float_input("Monto a retirar: ", min=0, max=self.balance)
        self.balance -= n

    def saldo(self):
        print(f"Saldo restante: {self.balance:.2f}")


if __name__ == "__main__":
    cajero = Cajero()
    cajero.run()
