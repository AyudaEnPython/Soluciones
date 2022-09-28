"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import Any, List

from utils import (
    _tem,
    _cuota_mensual,
    diferencia_dias,
    convertir_fecha,
    sumar_mes,
)
# pip install prototools
from prototools import RangeDict

DATA = RangeDict(
    {
        (5_000, 10_000): (12, 0.26),
        (10_001, 15_000): (18, 0.24),
        (15_001, 20_000): (24, 0.22),
        (20_001, 25_000): (30, 0.20),
        (25_001, 30_000): (36, 0.18),
    }
)


@dataclass
class Cliente:
    apellidos: str
    nombres: str
    dni: str


@dataclass
class Cuota:
    monto_prestamo: float
    dias_pago: int
    fecha: str


@dataclass
class Cronograma:
    cliente: Cliente
    cuota: Cuota
    interes: float = field(init=False)
    meses: int = field(init=False)
    tem: float = field(init=False)
    cuota_mensual: float = field(init=False)
    data: List[Any] = field(default_factory=list)

    def __post_init__(self):
        self.meses, self.interes = DATA[self.cuota.monto_prestamo]
        self.tem = round(_tem(self.interes), 2)
        self.cuota_mensual = round(
            _cuota_mensual(
                self.cuota.monto_prestamo,
                self.tem,
                self.meses
            ), 2
        )
        self.data.append({
            "periodo": "00",
            "fecha_pago": self.cuota.fecha,
            "fecha_vencimiento": convertir_fecha(
                self.cuota.fecha, self.cuota.dias_pago
            ),
            "dias": "",
            "capital": self.cuota.monto_prestamo,
            "amortizacion": round(
                self.cuota_mensual - self.cuota_mensual*self.tem, 2
            ),
            "interes": self.cuota.monto_prestamo*self.tem,
            "cuota": self.cuota_mensual,
        })
        self._generar_cronograma()

    def _generar_cronograma(self):
        capital = self.cuota.monto_prestamo
        interes = self.interes
        for i in range(1, self.meses + 1):
            interes = round(self.data[i-1]["capital"] * self.tem, 2)
            amortizacion = round(self.cuota_mensual - interes, 2)
            capital = round(self.data[i-1]["capital"] - amortizacion, 2)
            fecha = sumar_mes(self.data[i-1]["fecha_vencimiento"])
            dias = diferencia_dias(self.data[i-1]["fecha_vencimiento"], fecha)
            self.data.append({
                "periodo": f"{i:02d}",
                "fecha_pago": self.cuota.fecha,
                "fecha_vencimiento": fecha,
                "dias": dias,
                "capital": capital if capital > 0.5 else 0.0,
                "amortizacion":
                    amortizacion if capital > 0.5 else
                    self.data[i-1]["capital"],
                "interes": interes,
                "cuota": self.cuota_mensual,
            })
        self.data.pop(0)
