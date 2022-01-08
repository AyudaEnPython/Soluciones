"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Persona:
    nombre: str
    apellido: str
    dni: str

    def full_name(self):
        return f"{self.apellido}, {self.nombre}"


@dataclass
class Pasajero(Persona):
    pasaporte: str


@dataclass
class Pasaje:
    origen: str
    destino: str
    cantidad: int
    precio: float


@dataclass
class Venta:
    id_venta: int
    pasajero: Pasajero
    pasaje: Pasaje


@dataclass
class DAO(ABC):

    @abstractmethod
    def insertar(self, obj):
        ...

    @abstractmethod
    def actualizar(self, obj):
        ...

    @abstractmethod
    def eliminar(self, obj):
        ...

    @abstractmethod
    def seleccionar(self, obj):
        ...