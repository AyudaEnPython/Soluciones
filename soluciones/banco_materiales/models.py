"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import List


@dataclass
class Estudiante:
    codigo: str
    nombre: str
    apellido: str
    ingreso: str
    recibido: bool

    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"


@dataclass
class Carrera:
    codigo: str
    nombre: str
    facultad: str

    def __str__(self) -> str:
        return f"{self.nombre}"


@dataclass
class Materia:
    codigo: str
    nombre: str
    semestre: str
    carrera: Carrera

    def __str__(self) -> str:
        return f"{self.nombre}"


@dataclass
class Material:
    codigo: str
    titulo: str
    contenido: str
    materia: Materia
    gestor: Estudiante
    calificacion: int

    @property
    def nombre(self) -> str:
        return self.materia.nombre

    @property
    def carrera(self) -> str:
        return self.materia.carrera

    def ver_documento(self) -> str:
        return (
            f"Carrera: {self.carrera}\n"
            f"Materia: {self.materia}\n"
            f"Calificación: {self.calificacion}\n"
            f"Titulo: {self.titulo}\n"
            f"Contenido: {self.contenido}\n"
        )

    def ver_por_calificacion(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Titulo: {self.titulo}\n"
            f"Materia: {self.materia}\n"
            f"Carrera: {self.carrera}\n"
        )

    def ver_por_materia(self) -> str:
        return (
            f"Código: {self.codigo}\n"
            f"Título: {self.titulo}\n"
        )


@dataclass
class BancoMateriales:
    materiales: List[Material] = field(default_factory=list)

    def add_material(self, material: str) -> None:
        self.materiales.append(material)

    def ver_por_materia(self, materia: str) -> None:
        for material in self.materiales:
            if material.materia.nombre == materia:
                print(material.ver_por_materia())

    def ver_documento(self, codigo: str) -> None:
        for material in self.materiales:
            if material.codigo == codigo:
                print(material.ver_documento())

    def cantidad_materiales_por_carrera(self, carrera: str) -> None:
        print(len([
                material for material in self.materiales
                if material.carrera.nombre == carrera
            ]))

    def ver_por_calificacion(self, calificacion: int) -> None:
        for material in self.materiales:
            if material.calificacion >= calificacion:
                print(material.ver_por_calificacion())

    def ver_gestores(self) -> None:
        gestores = set([str(material.gestor) for material in self.materiales])
        for gestor in gestores:
            print(gestor)
