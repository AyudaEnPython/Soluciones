"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass


@dataclass
class Cuenta:
    titular: str = ""
    numero: str = ""
    pin: str = ""
    _balance: float = 0.0

    @property
    def balance(self) -> float:
        return self._balance

    def depositar(self, cantidad: float) -> None:
        self._balance += cantidad

    def retirar(self, cantidad: float) -> None:
        if cantidad > self._balance:
            raise ValueError("No hay suficiente saldo")
        self._balance -= cantidad

    def clear(self) -> None:
        self._balance = 0.0
