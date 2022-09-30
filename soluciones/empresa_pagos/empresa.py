"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import Dict, List, Tuple
from planilla import planilla
# pip install prototools
from prototools import int_input, float_input, menu_input
from prototools import tabulate, textbox
from prototools.colorize import red, green, cyan, magenta


IMPUESTOS: Dict[str, float] = {
    "obrero": 0.1,
    "empleado": 0.12,
}


def ingresar_datos() -> Tuple[str, str, int, float, str]:
    nombre = input(cyan("Nombre: "))
    apellido = input(cyan("Apellido: "))
    horas = int_input(cyan("Horas: "), min=0)
    sueldo = float_input(cyan("Sueldo: "), min=0)
    tipo = menu_input(tuple(IMPUESTOS.keys()), numbers=True, lang="es")
    return nombre, apellido, horas, sueldo, tipo


@dataclass
class Empleado:
    nombres: str
    apellidos: str
    horas: int
    sueldo: int
    tipo: str

    def __post_init__(self) -> None:
        self.pago = self.calcular_pago()

    def calcular_pago(self) -> float:
        pago = self.horas * self.sueldo
        impuesto = IMPUESTOS[self.tipo]
        pago_neto = pago - pago * impuesto
        return pago if pago < 1000 else pago_neto


@dataclass
class Empresa:
    empleados: List[Empleado] = field(default_factory=list)

    def __post_init__(self) -> None:
        self._load()

    def _load(self) -> None:
        for data in planilla:
            self.empleados.append(Empleado(**data))

    def agregar(self) -> None:
        empleado = Empleado(*ingresar_datos())
        self.empleados.append(empleado)

    def reporte(self) -> None:
        obreros, empleados = self._tipo_empleado()
        print(tabulate(
            [
                [e.nombres, e.apellidos, e.horas, e.sueldo, e.tipo, e.pago]
                for e in self.empleados
            ],
            headers=[
                cyan("Nombre"),
                cyan("Apellido"),
                cyan("Horas"),
                cyan("Sueldo"),
                cyan("Tipo"),
                cyan("Pago"),
            ],
            color=magenta,
        ))
        print(tabulate(
            [
                [cyan("Total a pagar"), f"${self._total_pago():.2f}"],
                [cyan("Tipo Obrero"), f"{obreros}"],
                [cyan("Tipo Empleados"), f"{empleados}"],
            ],
            headless=True,
            color=magenta,
        ))

    def eliminar(self) -> None:
        nombre = input(cyan("Nombre: "))
        empleado = self._buscar(nombre)
        if empleado:
            self.empleados.remove(empleado)
            textbox(green("Empleado eliminado!"))
        else:
            textbox(red("No existe empleado!"))

    def _buscar(self, nombre) -> Empleado:
        for empleado in self.empleados:
            if empleado.nombres == nombre:
                return empleado

    def _total_pago(self) -> float:
        return sum([e.pago for e in self.empleados])

    def _tipo_empleado(self) -> Tuple[int, int]:
        obreros = len([e for e in self.empleados if e.tipo == "obrero"])
        empleados = len([e for e in self.empleados if e.tipo == "empleado"])
        return obreros, empleados
