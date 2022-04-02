"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
# pip install prototools
from prototools import ProtoSqlite

db = ProtoSqlite("data.db", lang="es")


@dataclass
class Empleado:
    cedula: str
    nombres: str
    apellidos: str

    def to_db(self) -> None:
        db.add("empleados", self.__dict__)


@dataclass
class ReporteAsistencia:
    cedula: str
    fecha: str
    entrada: str
    salida: str

    def to_db(self) -> None:
        db.add("asistencia", self.__dict__)

    def update(self, value: object) -> None:
        db.update(
            "asistencia", f"salida = {value}", f"cedula='{self.cedula}'",
        )
