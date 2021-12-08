"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Empresa:
    emplados: List[object] = field(default_factory=list)

    def agregar_empleado(self) -> None:
        ...

    def buscar_empleado(self, id_=None, nombre=None) -> object:
        if id_ is not None:
            for empleado in self.emplados:
                if empleado.id == id_:
                    return empleado
        elif nombre is not None:
            for empleado in self.emplados:
                if empleado.nombre == nombre:
                    return empleado
        return None
    
    def mostrar_empleados(self) -> None:
        for empleado in self.emplados:
            empleado.datos()
        
    def mostrar_por_tipo(self, tipo) -> None:
        for empleado in self.emplados:
            if empleado.__class__.__name__ == tipo:
                empleado.datos()

    def aumentar_sueldo(
        self, aumento: float,
        nombre: str = None,
        id_: str = None,
    ) -> None:
        empleado = self.buscar_empleado(id_, nombre)
        if empleado is not None:
            empleado.aumentar_sueldo(aumento)
        else:
            print("No se encontro el empleado")