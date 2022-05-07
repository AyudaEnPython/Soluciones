"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, List


T: Dict[str, Dict[str, float]] = {
    "PG": {"n1": .15, "n2": .15, "n3": .4, "n4": .3},
    "EPE": {"n1": .2, "n2": .2, "n3": .3, "n4": .3},
}


@dataclass
class Estudiante:
    codigo: str
    nombre_completo: str
    modalidad: str


@dataclass
class Calificacion:
    m: str
    n1: float
    n2: float
    n3: float
    n4: float

    def __post_init__(self) -> float:
        self.nf = self.n1*T[self.m]["n1"] + \
                self.n2*T[self.m]["n2"] + \
                self.n3*T[self.m]["n3"] + \
                self.n4*T[self.m]["n4"]

    def final(self):
        return self.nf


@dataclass
class Registrar:
    estudiantes: List[Estudiante] = field(default_factory=list)
    calificacion: List[Calificacion] = field(default_factory=list)

    def guardar_calificacion(self):
        df = pd.DataFrame(
            columns=[
                "Código",
                "Nombre Completo",
                "Modalidad",
                "Nota Final",
            ]
        )
        for estudiante, calificacion in zip(self.estudiantes, self.calificacion):
            df = df.append(
                {
                    "Código": estudiante.codigo,
                    "Nombre Completo": estudiante.nombre_completo,
                    "Modalidad": estudiante.modalidad,
                    "Nota Final": calificacion.final(),
                },
                ignore_index=True
            )
        df.to_excel("calificaciones.xlsx", index=False)
