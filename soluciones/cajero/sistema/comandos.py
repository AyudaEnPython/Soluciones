"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field

from .cuenta import Cuenta
from .transaccion import Transaccion


@dataclass
class Depositar(Transaccion):
    cuenta: Cuenta
    monto: float

    @property
    def detalles(self) -> str:
        return f"${self.monto:.2f} en cuenta {self.cuenta.numero}"

    def ejecutar(self) -> None:
        self.cuenta.depositar(self.monto)
        # print(f"Depositado {self.detalles}")

    def __repr__(self) -> str:
        return f"Depositado {self.detalles}"


@dataclass
class Retirar(Transaccion):
    cuenta: Cuenta
    monto: float

    @property
    def detalles(self) -> str:
        return f"${self.monto:.2f} de cuenta {self.cuenta.numero}"

    def ejecutar(self) -> None:
        self.cuenta.retirar(self.monto)
        # print(f"Retirado {self.detalles}")

    def __repr__(self) -> str:
        return f"Retirado {self.detalles}"


@dataclass
class Transferir(Transaccion):
    de_cuenta: Cuenta
    a_cuenta: Cuenta
    monto: float

    @property
    def detalles(self) -> str:
        return (
            f"${self.monto:.2f} de cuenta {self.de_cuenta.numero}"
            f" a cuenta #{self.a_cuenta.numero}"
        )

    def ejecutar(self) -> None:
        self.de_cuenta.retirar(self.monto)
        self.a_cuenta.depositar(self.monto)
        # print(f"Transferido {self.detalles}")
    
    def __repr__(self) -> str:
        return f"Transferido {self.detalles}"