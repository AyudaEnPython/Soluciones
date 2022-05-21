"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: functional but still needs some improvements
"""
from dataclasses import dataclass, field
from typing import List
# pip install prototools
from prototools import Menu, float_input, str_input


@dataclass
class Estudiante:
    codigo: str
    nombre: str
    calificaciones: List[float] = field(default_factory=list)

    def __post_init__(self):
        self.no_evaluada = min(self.calificaciones)
        self.calificaciones.remove(self.no_evaluada)
        self.promedio = sum(self.calificaciones) / len(self.calificaciones)
        self.estado = self._estado()

    def _estado(self):
        if self.promedio >= 15:
            return "Aprobado"
        return "Desaprobado"

    def __str__(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Nombre: {self.nombre}\n"
            f"No evaluada: {self.no_evaluada:.2f}\n"
            f"Promedio: {self.promedio:.2f}\n"
            f"Estado: {self.estado}"
        )


class App(Menu):

    def __init__(self):
        super().__init__()
        self.estudiantes = []
        self.add_options(
            ("Registrar calificaciones", self.registrar),
            ("Reporte de calificaciones", self.reporte),
            ("Estadísticas de calificaciones", self.estadisticas),
        )

    def _codigo_valido(self, codigo: str) -> bool:
        for estudiante in self.estudiantes:
            if estudiante.codigo == codigo:
                return False
        return True

    def registrar(self) -> None:
        msg = "Evaluación Continua {} (EC{}): "
        codigo = str_input("Código: ")
        if not self._codigo_valido(codigo):
            print("Código inválido")
            return
        nombre = str_input("Nombre completo: ")
        calificaciones = [
            float_input(msg.format(i, i), min=0, max=20) for i in range(1, 5)
        ]
        self.estudiantes.append(Estudiante(codigo, nombre, calificaciones))

    def reporte(self) -> None:
        estudiante_id = str_input("Codigo de estudiante: ")
        for estudiante in self.estudiantes:
            if estudiante.codigo == estudiante_id:
                print(estudiante)

    def estadisticas(self) -> None:
        self.aprobados = len([
            estudiante for estudiante in self.estudiantes
            if estudiante.estado == "Aprobado"
        ])
        self.nota_maxima = max([
            estudiante.promedio for estudiante in self.estudiantes
        ])
        self.nota_minima = min([
            estudiante.promedio for estudiante in self.estudiantes
        ])
        self.promedio_general = sum([
            estudiante.promedio for estudiante in self.estudiantes
        ]) / len(self.estudiantes)
        print(
            f"Aprobados: {self.aprobados}\n"
            f"Nota máxima: {self.nota_maxima:.2f}\n"
            f"Nota mínima: {self.nota_minima:.2f}\n"
            f"Promedio general: {self.promedio_general:.2f}"
        )


if __name__ == "__main__":
    app = App()
    app.run()
