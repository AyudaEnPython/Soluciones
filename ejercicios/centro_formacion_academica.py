"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

#------------------------- ENUNCIADO ORIGINAL -------------------------
Crear una aplicación para el siguiente proceso.

Un Centro de Formación Académica, desea una aplicación que permita el
control de sus estudiantes en el Taller de Informática, para lo cual se
debe tener en cuenta los siguientes datos: nombre del estudiante, edad
(18 - 25 años), sexo (M o F), sus 5 calificaciones (0 - 20), luego de
ello mostrar su promedio. Existen 4 aulas denominadas: "ALFA", "BETA",
"DELTA", "GAMA" y por cada aula se deben ingresar los datos de un 
estudiante, si el usuario desea, ingresará un siguiente estudiante a la
misma aula y continuará hasta que decida ya no ingresar uno más. Este
proceso se repetirá para las 4 aulas creadas.

Al terminar el proceso de registro de información, se debe presentar un
listado de resultados que se desean mostrar, de la siguiente manera:

    +-----------------------------------------------------------------+
    | Menú de Opciones                                                |
    | ================                                                |
    | 1. Mostrar los promedios generales de cada aula.                |
    | 2. El nombre y promedio del alumno con mayor promedio, así como |
    |    el aula a la que pertenece.                                  |
    | 3. Porcentaje de varones y mujeres por cada aula.               |
    | 4. Estudiante que tiene la mayor y menor edad de todos.         |
    | 5. Listado: Aula, cantidad de estudiantes, promedio de aula.    |
    | 6. Salir.                                                       |
    +-----------------------------------------------------------------+

Este menú debe repetirse hasta que el usuario seleccione la opción 6
(salir).

Nota: No utilizar ningun tio de listas, ni funciones, ni métodos.
#------------------------- FIN DEL ENUNCIADO --------------------------

    +-------------------------------------------------+
    | Nota: Se opta por un cambio de diseño dadas las |
    |   restricciones del enunciado.                  |
    +-------------------------------------------------+

NOTE: add testcases
"""
from dataclasses import dataclass, field
from typing import List
# pip install prototools
from prototools import Menu, int_input, choice_input, ask_to_finish


NUMERO_CALIFICACIONES = 5
AULAS = ("alfa", "beta", "delta", "gamma")
SEXOS = ("M", "F")


@dataclass
class Estudiante:
    nombre: str
    edad: int
    sexo: str
    calificaciones: List[int] = field(default_factory=list)

    def promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


@dataclass
class Aula:
    nombre: str
    estudiantes: List[Estudiante] = field(default_factory=list)

    def promedio(self):
        if len(self.estudiantes) == 0:
            return 0
        return sum(e.promedio() for e in self.estudiantes) / len(self.estudiantes)
    
    def cantidad_estudiantes(self):
        return len(self.estudiantes)

    def porcentaje(self, sexo):
        return (
            len([e for e in self.estudiantes if e.sexo == sexo]) / len(self.estudiantes)
        )
    
    def mayor_edad(self):
        return max(e.edad for e in self.estudiantes)

    def menor_edad(self):
        return min(e.edad for e in self.estudiantes)

    def mejor_alumno(self):
        return max(self.estudiantes, key=lambda e: e.promedio())


@dataclass
class Taller:
    aulas: List[Aula] = field(
        default_factory=lambda: [Aula(nombre=aula) for aula in AULAS]
        )


def registrar_estudiante(aula: Aula):
    """Registra un estudiante en una aula."""
    estudiante = Estudiante(
        nombre=input("Nombre del estudiante: "),
        edad=int_input("Edad del estudiante: ", min=18, max=25),
        sexo=choice_input(SEXOS),
        calificaciones=[
            int_input(f"Calificación {i+1}: ", min=0, max=20)
            for i in range(NUMERO_CALIFICACIONES)
            ]
        )
    aula.estudiantes.append(estudiante)


def registrar():
    """Registra estudiantes en las aulas del taller."""
    taller = Taller()
    for aula in taller.aulas:
        print(f"Aula: {aula.nombre}")
        while True:
            registrar_estudiante(aula)
            if not ask_to_finish():
                break
    return taller


taller = registrar()


def mostrar_promedio_generales():
    """
    Muestra los promedios generales de cada aula.
    """
    for aula in taller.aulas:
        print(f"Aula: {aula.nombre}")
        print(f"Promedio general: {aula.promedio():.2f}")


def mostrar_mejor_alumno():
    """
    Muestra el nombre y promedio del alumno con mayor promedio, así como
    el aula a la que pertenece.
    """
    for aula in taller.aulas:
        print(f"Aula: {aula.nombre}")
        print(f"Mejor alumno: {aula.mejor_alumno().nombre}")
        print(f"Promedio: {aula.mejor_alumno().promedio():.2f}")


def mostrar_porcentaje_sexo():
    """
    Muestra el porcentaje de varones y mujeres por cada aula.
    """
    for aula in taller.aulas:
        print(f"Aula: {aula.nombre}")
        print(f"Porcentaje de varones: {aula.porcentaje('M'):.2%}")
        print(f"Porcentaje de mujeres: {aula.porcentaje('F'):.2%}")


def mostrar_estudiantes_por_edad():
    """
    Muestra el estudiante que tiene la mayor y menor edad de todos.
    """
    for aula in taller.aulas:
        print(f"Aula: {aula.nombre}")
        print(f"Mayor edad: {aula.mayor_edad()}")
        print(f"Menor edad: {aula.menor_edad()}")


def mostrar_informacion_por_aula():
    """
    Muestra la cantidad de estudiantes, el promedio de la aula y el nombre
    del aula.
    """
    for aula in taller.aulas:
        print(f"Aula: {aula.nombre}")
        print(f"Cantidad de estudiantes: {aula.cantidad_estudiantes()}")
        print(f"Promedio: {aula.promedio():.2f}")


if __name__ == "__main__":
    menu = Menu()
    menu.add_options(
        ("Promedios generales por cada aula",
            mostrar_promedio_generales),
        ("Información del mejor alumno",
            mostrar_mejor_alumno),
        ("Porcentaje de varones y mujeres por aula",
            mostrar_porcentaje_sexo),
        ("Estudiantes que tienen la mayor y menor edad de todos",
            mostrar_estudiantes_por_edad),
        ("Información por aula",
            mostrar_informacion_por_aula),
    )
    menu.run()