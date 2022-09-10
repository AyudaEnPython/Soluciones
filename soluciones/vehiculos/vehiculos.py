"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass


@dataclass
class Vehiculo:
    marca: str
    modelo: str
    km: float
    precio: float

    def obtener_precio(self):
        return self.precio


@dataclass
class Auto(Vehiculo):
    airbag: bool

    def obtener_precio(self):
        precio = super().obtener_precio()
        return precio + 300 if self.airbag else precio


@dataclass
class Moto(Vehiculo):
    casco: bool

    def obtener_precio(self):
        precio = super().obtener_precio()
        return precio + 80 if self.casco else precio
