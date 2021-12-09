"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Union
# pip install prototools
from prototools import menu_input, float_input, int_input, textbox
from prototools.colorize import cyan, red
from nomina import Supervisor, Analista, Operativo
from utils import ingresar_datos, TIPOS, dummy_data


class Empresa:
    id_: int = 1
    empleados: List[Union[Supervisor, Analista, Operativo]] = []

    def __init__(self, dummy: bool = False):
        self.dummy = dummy
        if self.dummy:
            self._load_employees()

    def _load_employees(self):
        for empleado in dummy_data():
            __class__.empleados.append(empleado)
        __class__.id_ = 4

    def agregar_empleado(self) -> None:
        obj_ = ingresar_datos()
        obj_.id_ = self.id_
        __class__.id_ += 1
        __class__.empleados.append(obj_)

    def aumentar_sueldo(self) -> None:
        id_ = int_input(cyan("Ingresar id del empleado: "))
        empleado = self._buscar(id_)
        aumento = float_input(cyan("Ingresar aumento: "))
        if empleado is not None:
            empleado.aumentar_sueldo(aumento)

    def mostrar_empleados(self) -> None:
        for empleado in self.empleados:
            empleado.datos()

    def _buscar(self, id_) -> object:
        for empleado in self.empleados:
            if empleado.id_ == id_:
                return empleado

    def buscar_empleado(self) -> object:
        id_ = int_input(cyan("Ingresar id: "))
        empleado = self._buscar(id_)
        if empleado is None:
            textbox(red("No se encontro el empleado"), bcolor="red")
        else:
            empleado.datos()

    def mostrar_por_tipo(self) -> None:
        tipo = menu_input(TIPOS, numbers=True, lang="es")
        for empleado in self.empleados:
            if empleado.__class__.__name__ == tipo:
                empleado.datos()

    def asignar_supervisor(self) -> None: # TODO: split it in more methods
        id_ = int_input(cyan("Ingresar id del empleado: "))
        empleado = self._buscar(id_)
        if empleado is None:
            textbox(red("No se encontro el empleado"), bcolor="red")
            return
        if isinstance(empleado, Supervisor):
            textbox(red(
                "El empleado debe ser Analista u Operativo"), bcolor="red"
            )
            return
        print(empleado.fullname)
        id_ = int_input(cyan("Ingresar id del supervisor: "))
        supervisor = self._buscar(id_)
        if not isinstance(supervisor, Supervisor):
            textbox(red("El supervisor debe ser Supervisor"), bcolor="red")
            return
        elif supervisor is None:
            textbox(red("No se encontro el supervisor"), bcolor="red")
            return
        empleado.supervisor = supervisor.fullname
        if empleado not in supervisor.supervisados:
            supervisor.supervisar(empleado)
        else:
            textbox(red("El empleado ya es supervisado"), bcolor="red")