"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime
from typing import Tuple
# pip install prototools
from prototools import menu_input, ProtoDB
from prototools.colorize import cyan
from nomina import Analista, Operativo, Supervisor

SUELDOS = {"Analista": 120_000, "Operativo": 80_000, "Supervisor": 200_000}
TIPOS = ("Analista", "Operativo", "Supervisor")
NIVEL = ("Licenciatura", "Bachillerato")


def _ingreso_base() -> Tuple[str, str, str, str]:
    tipo = menu_input(TIPOS, numbers=True, lang="es")
    nombres = input(cyan("Ingrese los nombres: "))
    apellidos = input(cyan("Ingrese los apellidos: "))
    nac = input(cyan("Ingrese la fecha de nacimiento (dd/mm/yy): "))
    ingreso = datetime.today().strftime("%d/%m/%Y")
    sueldo = SUELDOS[tipo]
    return tipo, nombres, apellidos, nac, ingreso, sueldo


def ingresar_datos() -> object:
    """Ingresa los datos de los empleados."""
    tipo, *data = _ingreso_base()
    if tipo == "Supervisor":
        lic = input(cyan("Ingresar licenciatura: "))
        area = input(cyan("Ingresar area supervisada: "))
        return Supervisor(*data,  lic, area)
    else:
        nivel = menu_input(NIVEL, numbers=True, lang="es")
        habilidades = input(cyan("Ingresar habilidades: "))
        if tipo == "Analista":
            return Analista(*data, nivel, habilidades)
        else:
            return Operativo(*data, nivel, habilidades)


def dummy_data() -> Tuple[object, object, object]:
    data = ProtoDB("database/empleados")
    empleados = data.get_data()
    supervisor, analista, operativo = empleados["empleados"]
    e1 = Supervisor(
        supervisor["nombres"],
        supervisor["apellidos"],
        supervisor["dob"],
        supervisor["ingreso"],
        supervisor["sueldo"],
        supervisor["licenciatura"],
        supervisor["area_supervisada"],
    )
    e2 = Analista(
        analista["nombres"],
        analista["apellidos"],
        analista["dob"],
        analista["ingreso"],
        analista["sueldo"],
        analista["nivel_estudios"],
        analista["habilidades"],
    )
    e3 = Operativo(
        operativo["nombres"],
        operativo["apellidos"],
        operativo["dob"],
        operativo["ingreso"],
        operativo["sueldo"],
        operativo["nivel_estudios"],
        operativo["habilidades"],
    )
    e1.id_ = supervisor["id_"]
    e2.id_ = analista["id_"]
    e3.id_ = operativo["id_"]
    e1.supervisar(e2)
    e2.supervisor = e1.fullname
    return e1, e2, e3
