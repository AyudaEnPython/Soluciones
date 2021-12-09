"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import List
# pip install prototools
from prototools import tabulate, textbox
from prototools.colorize import cyan, green, magenta, red


@dataclass
class Empleado:
    nombres: str
    apellidos: str
    dob: str
    ingreso: str
    sueldo: float
    id_: int = field(init=False)

    def __post_init__(self) -> None:
        self.fullname = f"{self.apellidos}, {self.nombres}"
        self.edad = self._calcular_edad()
        self.antiguedad = self._calcular_antiguedad()

    def aumentar_sueldo(self, aumento: float) -> None:
        if self.sueldo > aumento:
            textbox(red("No se puede aumentar el sueldo"), bcolor="red")
            return
        self.sueldo = aumento
        textbox(green(f"Sueldo aumentado a {self.sueldo}"), bcolor="green")

    def datos(self) -> None:
        data = [
            [cyan("Tipo"), self.__class__.__name__,
                cyan("ID"), self.id_, cyan("Sueldo"), self.sueldo],
            [cyan("Nombres"), self.nombres, cyan("Nacimiento"),
                self.dob, cyan("Edad"), self.edad],
            [cyan("Apellidos"), self.apellidos, cyan("Ingreso"), self.ingreso,
                cyan("Antiguedad"), self.antiguedad],
        ]
        print(tabulate(data, headless=True, color=magenta, inner=True))

    def _calcular_edad(self) -> int:
        return int(datetime.today().strftime("%Y")) - int(self.dob[-4:])

    def _calcular_antiguedad(self) -> int:
        return int(datetime.today().strftime("%Y")) - int(self.ingreso[-4:])


@dataclass
class Supervisor(Empleado):
    licenciatura: str
    area_supervisada: str
    supervisados: List[object] = field(init=False, default_factory=list)

    def supervisar(self, personal: object) -> None:
        self.supervisados.append(personal)

    def datos(self) -> None:
        super().datos()
        data = [
            [cyan("Licenciatura"), self.licenciatura],
            [cyan("Personal supervisado"), 
                "- ".join(s.fullname for s in self.supervisados)],
        ]
        print(tabulate(
            data, headless=True, color=magenta, inner=True, style=(8, 1, 1, 1)
        ))


@dataclass
class Administrativo(Empleado):
    nivel_estudios: str
    habilidades: str
    supervisor: str = field(init=False, default="No asignado")

    def datos(self) -> None:
        super().datos()
        data = [
            [cyan("Nivel de estudios"), self.nivel_estudios],
            [cyan("Habilidades"), self.habilidades],
            [cyan("Supervisor"), self.supervisor],
        ]
        print(tabulate(
            data, headless=True, color=magenta, inner=True, style=(8, 1, 1, 1)
        ))


@dataclass
class Analista(Administrativo):

    def analizar(self) -> None:
        ...

    def optimizar(self) -> None:
        ...


@dataclass
class Operativo(Administrativo):

    def tecnicas(self) -> None:
        ...
    
    def ejecutar(self) -> None:
        ...