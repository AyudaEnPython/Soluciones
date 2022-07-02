"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import uuid
from random import randint
from typing import Dict, Tuple

GENERO: Dict[str, str] = {"m": "Masculino", "f": "Femenino"}
DIAS: Tuple[int, int] = (1, 30)
MESES: Tuple[int, int] = (1, 12)


def _generate_rut() -> str:
    return str(uuid.uuid4().int)[:8]


class Rut:

    def __init__(self, rut: str, dv: str) -> None:
        self.rut = rut
        self.dv = dv

    def mostrar_rut(self) -> str:
        return f"{self.rut}-{self.dv}"


class Fecha:

    def __init__(self, dd: int, mm: int, aa: int) -> None:
        self.dd = dd
        self.mm = mm
        self.aa = aa
    
    def mostrar_fecha(self) -> str:
        return f"{self.dd}/{self.mm}/{self.aa}"


class Persona:

    def __init__(self, apellidos: str, nombres: str, genero: str) -> None:
        self.apellidos = apellidos
        self.nombres = nombres
        self.genero = genero

    def __str__(self) -> str:
        return (
            f"Apellidos: {self.apellidos}\nNombres: {self.nombres}\n"
            f"Genero: {GENERO[self.genero]}"
        )


class Sueldo:

    def __init__(self, monto: float) -> None:
        self.monto = monto

    def mostrar_sueldo(self) -> str:
        return f"Sueldo: {self.monto}"


class Empleado(Persona):

    def __init__(
        self,
        id_: int,
        rut: Rut,
        apellidos: str,
        nombres: str,
        genero: str,
        fecha: Fecha,
        sueldo: Sueldo,
    ) -> None:
        super().__init__(
            apellidos=apellidos,
            nombres=nombres,
            genero=genero
        )
        self.id_ = id_
        self.rut = rut
        self.fecha = fecha
        self.sueldo = sueldo

    def mostrar_informacion(self) -> str:
        return (
            f"ID: {self.id_}\n"
            f"Rut: {self.rut.mostrar_rut()}\n"
            f"{super().__str__()}\n"
            f"Fecha de ingreso: {self.fecha.mostrar_fecha()}\n"
            f"Sueldo: {self.sueldo.mostrar_sueldo()}\n"
        )


def main():
    names: Tuple[str, ...] = (
        ("Becker", "Jason", "m"),
        ("Malmsteen", "Yngwie", "m"),
        ("Mithcell", "Joni", "f"),
        ("Panagaris", "Orianthi", "f"),
        ("Satriani", "Joe", "m"),
    )
    for empleado in [
        Empleado(
            id_,
            Rut(_generate_rut(), str(randint(0, 9))),
            last_name,
            name,
            gender,
            Fecha(randint(*DIAS), randint(*MESES), 2022),
            Sueldo(randint(5, 34)*1000),
        ) for id_, (last_name, name, gender) in enumerate(names, 1)
    ]:
        print(empleado.mostrar_informacion())


if __name__ == "__main__":
    main()
