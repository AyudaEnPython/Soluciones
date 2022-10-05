"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List

from .transaccion import Transaccion


@dataclass
class BancoControlador:
    libro: List[Transaccion] = field(default_factory=list)
    actual: int = 0

    def registrar(self, transaccion: Transaccion) -> None:
        del self.libro[self.actual:]
        self.libro.append(transaccion)
        self.actual += 1

    def deshacer(self) -> None:
        if self.actual > 0:
            self.actual -= 1

    def rehacer(self) -> None:
        if self.actual < len(self.libro):
            self.actual += 1

    def calcular_balance(self) -> None:
        for transaccion in self.libro[:self.actual]:
            transaccion.ejecutar()

    def ver_movimientos(self) -> None:
        for i, transaccion in enumerate(self.libro[-5:], 1):
            print(f"{i}. {transaccion}")
