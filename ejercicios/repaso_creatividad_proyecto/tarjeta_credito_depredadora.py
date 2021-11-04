"""Al igual que TarjetaCredito, se opta por mejorar la clase.
"""
from tarjetas import TarjetaCredito


class TarjetaCreditoDepredadora(TarjetaCredito):
    """Tarjeta de credito que cobra intereses e impouestos."""

    __IMPUESTO = 5

    def __init__(
        self,
        cliente: str,
        banco: str,
        cuenta: str,
        limite: float,
        interes: float,
        balance: float = 0,
    ) -> None:
        super().__init__(cliente, banco, cuenta, limite, balance)
        self._interes = interes
        self.__i = 0
        self.__adicional = 0
        self.__pago_minimo = 0

    @property
    def pago_minimo(self) -> float:
        return self.__pago_minimo

    def cargar(self, precio: float) -> bool:
        """Carga el precio dado en la tarjeta, asumiendo que hay
        credito.

        :param precio: precio a cargar
        :return: True si se pudo cargar, False de lo contrario y cobra
            $5 de impuesto si el cargo es denegado.
        """
        self.__i += 1
        if self.__i >= 10:
            self.__adicional = 1
        exito = super().cargar(precio)
        if not exito:
            self._balance += self.__class__.__IMPUESTO + self.__adicional
        return exito

    def proceso_mensual(self) -> None:
        """Asigna un interes mensual sobre el balance."""
        if self._balance > 0:
            self._balance *= (1 + self._interes)**(1/12)
            self.__pago_minimo = self._balance * 0.1