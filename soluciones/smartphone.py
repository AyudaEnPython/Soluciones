"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: La persona que pidio ayuda no dió mas detalles.
TODO: add docstring and tests later...
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from random import choices
from string import digits
from typing import Callable, Dict


def generar_imei() -> str:
    tac = "".join(choices(digits, k=6))
    fac = "".join(choices(digits, k=2))
    serial = "".join(choices(digits, k=6))
    spare = "".join(choices(digits, k=1))
    return f"{tac}{fac}{serial}{spare}"


@dataclass
class Procesador:
    soc: str
    cores: int
    frecuencia: float

    def overclock(self) -> None:
        self.frecuencia *= 2


@dataclass
class Camara:
    megapixeles: int

    def capturar_imagen(self) -> None:
        print("Imagen capturada")

    def capturar_video(self) -> None:
        print("Video capturado")


@dataclass
class Smartphone(ABC):
    almacenamiento: str
    memoria: str
    procesador: Procesador
    camara: Camara
    sistema: str = field(init=False)
    imei: str = field(default_factory=generar_imei)

    @abstractmethod
    def telefono(self):
        return NotImplementedError()


class AndroidPhone(Smartphone):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.sistema = "Android"

    def telefono(self, accion) -> Callable:
        acciones: Dict[str, Callable] = {
            "colgar": self.colgar,
            "marcar": self.marcar,
            "contestar": self.contestar,
        }
        return acciones[accion]()

    def contestar(self) -> None:
        print("Atendiento llamada entrante...")

    def colgar(self) -> None:
        print("Llamada entrante colgada!")

    def marcar(self) -> None:
        print("Marcando numero...")

    def tomar_foto(self) -> None:
        self.camara.capturar_imagen()

    def grabar_video(self) -> None:
        self.camara.capturar_video()


if __name__ == "__main__":
    movil = AndroidPhone(
        "128GB",
        "8GB",
        Procesador("Snapdragon 888", 8, 2.84),
        Camara(16),
    )
    print(movil)
    print(movil.almacenamiento)
    movil.telefono("marcar")
    movil.tomar_foto()
