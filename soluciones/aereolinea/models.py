from abc import ABC
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Persona(ABC):
    dni: str
    nombre: str
    apellido: str
    edad: int


@dataclass
class Pasajero(Persona):
    destino: str
    categoria: str


@dataclass
class Tripulante(Persona):
    cargo: str

    def generar_email(self, aerolinea: str) -> str:
        return f"{self.nombre[0]}.{self.apellido}@{aerolinea}.com".lower()


@dataclass
class Avion:
    modelo: str
    fabricante: str
    tripulantes: List[Tripulante] = field(default_factory=list)
    pasajeros: List[Pasajero] = field(default_factory=list)

    def registrar_pasajero(self, pasajero: Pasajero) -> bool:
        for pasajero_existente in self.pasajeros:
            if pasajero_existente.dni == pasajero.dni:
                return False
        return True
    
    def buscar_pasajero(self, dni: str) -> Optional[Pasajero]:
        for pasajero_existente in self.pasajeros + self.tripulantes:
            if pasajero_existente.dni == dni:
                return pasajero_existente
        return None

    def bajar_pasajero(self, dni: str) -> bool:
        for pasajero_existente in self.pasajeros:
            if pasajero_existente.dni == dni:
                self.pasajeros.remove(pasajero_existente)
                return True
        return False

    def mostrar_tripulantes(self):
        for tripulante in self.tripulantes:
            print(tripulante)

    def mostrar_pasajeros(self):
        for pasajero in self.pasajeros:
            print(pasajero)


@dataclass
class Vuelo:
    avion: Avion
    aerolinea: str

    def mostrar_informacion(self):
        print(f"Aerolinea: {self.aerolinea}")
        print(f"Modelo: {self.avion.modelo}")
        print(f"Fabricante: {self.avion.fabricante}")
        print(f"Tripulantes: {self.avion.tripulantes}")
        print(f"Lista de asajeros: ")
        self.avion.mostrar_pasajeros()