"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: there's still more room for improvement in this code.
"""
from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum, auto
from textwrap import indent
from typing import Dict

PRECIOS: Dict[str, int] = {"ECONOMICO": 300, "PREMIUM": 500}


class Estado(Enum):
    REPARACION = auto()
    LIBRE = auto()
    OCUPADO = auto()


class Tipo(Enum):
    ECONOMICO = auto()
    PREMIUM = auto()


@dataclass
class Vehiculo:
    placa: str
    marca: str
    year: str
    estado: Estado = field(init=False, default=Estado.LIBRE)

    def __str__(sefl) -> str:
        return f"Placa: {sefl.placa}\nMarca: {sefl.marca}\nAño: {sefl.year}"


@dataclass
class Calificacion:
    _puntaje: int = field(init=False, repr=False, default=5)
    _caracter: str = field(init=False, repr=False, default=u"\u2605")

    @property
    def caracter(self) -> str:
        return self._caracter

    @caracter.setter
    def caracter(self, value: str) -> None:
        self._caracter = value

    @property
    def puntaje(self) -> int:
        return self._puntaje

    @puntaje.setter
    def puntaje(self, value: int) -> None:
        value = value if value <= 5 else 5
        self._puntaje = int(
            Decimal((self.puntaje + value) / 2).quantize(0, ROUND_HALF_UP)
        )

    def __str__(self) -> str:
        return f"{self.caracter} " * self.puntaje


@dataclass
class Uber:
    vehiculo: Vehiculo
    tipo: Tipo
    viajes: int = field(default=0)
    monto: float = field(default=0)
    acumulado: float = field(default=0)
    _precios: Enum = field(init=False)

    def __post_init__(self) -> None:
        self._calificacion = Calificacion()
        self._precios = PRECIOS

    def set_calificacion(self, calificacion: int) -> None:
        self._calificacion.puntaje = calificacion

    def viaje(self, kilometros: float) -> None:
        if self.vehiculo.estado.name == "LIBRE":
            self.viajes += 1
            self._calcular_monto(kilometros)

    def enviar_reparacion(self) -> None:
        self.vehiculo.estado = Estado.REPARACION

    def recibir_reparacion(self) -> None:
        self.vehiculo.estado = Estado.LIBRE

    def get_tipo(self) -> Tipo:
        return self.tipo.name

    def get_estado(self) -> Estado:
        return self.vehiculo.estado.name

    def get_viajes(self) -> int:
        return self.viajes

    def reset(self) -> None:
        self.viajes = 0

    def mostrar(self) -> None:
        titulo = "Información detallada"
        print(titulo)
        print("-"*len(titulo))
        print(indent(str(self), " " * 4))
        print()

    def _calcular_monto(self, kilometros: float) -> None:
        self.monto = self._precios[self.tipo.name] * kilometros
        self.acumulado += self.monto

    def __str__(self) -> str:
        return (
            f"{self.vehiculo}\n"
            f"Estado: {self.get_estado()}\n"
            f"Tipo: {self.get_tipo()}\n"
            f"Calificación: {self._calificacion}\n"
            f"Cantidad de viajes: {self.get_viajes()}\n"
            f"Monto actual: $ {self.monto:,}\n"
            f"Monto acumulado: $ {self.acumulado:,}"
        )


def registrar_vehiculo(placa: str, marca: str, año: str) -> Vehiculo:
    return Vehiculo(placa, marca, año)


def uber_object(vehiculo: Vehiculo, tipo: Tipo) -> Uber:
    return Uber(vehiculo, Tipo[tipo.upper()])
