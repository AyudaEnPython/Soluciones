"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

class Fecha:

    def __init__(self, dia, mes, año) -> None:
        self._dia = dia
        self._mes = mes
        self._año = año

    @property
    def dia(self) -> int:
        return self._dia

    @property
    def mes(self) -> int:
        return self._mes

    @property
    def año(self) -> int:
        return self._año

    @dia.setter
    def dia(self, dia) -> None:
        self._dia = dia

    @mes.setter
    def mes(self, mes) -> None:
        if self._mes + mes > 12:
            self._año += 1
            self._mes = mes - (12 - self._mes)
        self._mes += mes

    @año.setter
    def año(self, año) -> None:
        self._año = año

    def __str__(self) -> str:
        return f"{self.dia}/{self.mes}/{self.año}"
