"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import Dict

from .cuenta import Cuenta


@dataclass
class Banco:
    cuentas: Dict[str, Cuenta] = field(default_factory=dict)

    def cuenta(self, numero: str) -> Cuenta:
        return self.cuentas[numero]

    def crear_cuenta(self, titular: str, numero: str, clave: str) -> Cuenta:
        cuenta = Cuenta(titular, numero, clave)
        self.cuentas[numero] = cuenta
        return cuenta

    def clear(self) -> None:
        for cuenta in self.cuentas.values():
            cuenta.clear()
