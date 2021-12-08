"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Empresa:
    emplados: List[object] = field(default_factory=list)

    def buscar_empleado(self, id_=None, nombre=None):
        if id_ is not None:
            for empleado in self.emplados:
                if empleado.id == id_:
                    return empleado
        elif nombre is not None:
            for empleado in self.emplados:
                if empleado.nombre == nombre:
                    return empleado
        return None
    
    def mostrar_empleados(self):
        for empleado in self.emplados:
            empleado.datos()
        
    def mostrar_por_tipo(self, tipo):
        for empleado in self.emplados:
            if empleado.__class__.__name__ == tipo:
                empleado.datos()