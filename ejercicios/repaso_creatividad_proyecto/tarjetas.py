"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Se opta por mejorar la clase TarjetaCredito, tanto en el
    docstring como en otros aspectos (property, typing, etc.).
"""
from typing import List
from prototools.validators import validate_float


class TarjetaCredito:
    """Representación de una tarjeta de credito.

    El balance inicial por defecto es cero.

    :param cliente: Nombre del cliente.
    :cliente type: str
    :param banco: Nombre del banco.
    :banco type: str
    :param cuenta: Número de cuenta.
    :cuenta type: str
    :param limite: Limite de la tarjeta.
    :limite type: float

    >>> t = TarjetaCredito('John Wick', 'BCP', '4301 0736 9468 0135', 1000)
    """

    def __init__(
        self,
        cliente: str,
        banco: str,
        cuenta: str,
        limite: float,
        balance: float = 0,
    ) -> None:
        self._cliente = cliente
        self._banco = banco
        self._cuenta = cuenta
        self._limite = limite
        if balance is not None:
            balance = balance
        self._balance = balance

    @property
    def cliente(self) -> str:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: str) -> None:
        self._cliente = cliente

    @property
    def banco(self) -> str:
        return self._banco

    @banco.setter
    def banco(self, banco: str) -> None:
        self._banco = banco

    @property
    def cuenta(self) -> str:
        return self._cuenta

    @cuenta.setter
    def cuenta(self, cuenta: str) -> None:
        self._cuenta = cuenta

    @property
    def limite(self) -> float:
        return self._limite

    @limite.setter
    def limite(self, limite: float) -> None:
        self._limite = limite

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, balance: float) -> None:
        self._balance = balance

    def cargar(self, precio: float) -> bool:
        """Carga el precio dado a la tarjeta de credito asumiendo que
        tiene saldo.

        :param precio: Precio a cargar.
        :precio type: float
        :return: True si se pudo cargar, False en caso contrario.
        :rtype: bool
        """
        precio = validate_float(precio)
        if precio + self._balance > self._limite:
            return False
        else:
            self._balance += precio
            return True

    def pagar(self, monto: float) -> None:
        """Procesa el pago del cliente y lo descuenta del balance.

        :param monto: Monto a pagar.
        :monto type: float
        """
        monto = validate_float(
            monto, min=0, custom="El monto debe ser mayor a cero."
        )
        self._balance -= monto


if __name__ == "__main__":
    from dataclasses import dataclass, field
    from prototools.utils import boxln

    @dataclass
    class Billetera:
        tarjetas: List[TarjetaCredito] = field(default_factory=list)

    billetera = Billetera([
        TarjetaCredito("John Wick", "BCP", "4301 0751 1942 4455", 2500),
        TarjetaCredito("John Wick", "BBVA", "3901 1236 1264 0112", 3500),
        TarjetaCredito("John Wick", "BN", "4501 6426 9468 0135", 5000),
    ])

    for tarjeta in billetera.tarjetas:
        tarjeta.cargar(1000)

    for tarjeta in billetera.tarjetas:
        boxln(f"{tarjeta.cliente} | {tarjeta.banco} | {tarjeta.cuenta}")
        print(f"Limite: {tarjeta.limite} | Balance: {tarjeta.balance}")
        while tarjeta.balance > 100:
            tarjeta.pagar(100)
            print(f"Nuevo balance: {tarjeta.balance}")
        print()
