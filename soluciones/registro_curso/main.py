"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar una aplicación en Python que permita almacenar en un Curso
del cual se registran en forma privada, el código de la clase, el 
nombre de la clase y el semestre al que pertenece. Para cada curso se
debe registrar estudiantes y sus atributos privados serían: rut,
nombre, dirección y teléfono. Considerar que cada estudiante, tiene
cierta cantidad de notas (4).

Para la gestión y administración de los procesos, se requiere del
diseño de un Menú que permita administrar todos los ingresos, las
modificaciones y las consultas necesarias para el buen desarrollo y
registro de los datos. Considerar que los registros deben contemplar
listas para guardar la información.

Considerar que se pueden consultar las notas y el resultado de cada
estudiante en forma privada, implemente todos los métodos o
comportamientos necesarios para que se permita el buen trabajao de este
mini-sistema.

TODO: still needs some work, if there's a bug, report it asap.
"""
from dataclasses import dataclass, field
from typing import List
# pip install prototools
from prototools import Menu


@dataclass
class Estudiante:
    _dni: str
    _nombre: str
    _direccion: str
    _telefono: str
    _notas: List[float] = field(default_factory=list)

    @property
    def dni(self) -> str:
        return self._dni
    
    @dni.setter
    def dni(self, dni: str) -> None:
        self._dni = dni

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def direccion(self) -> str:
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion: str) -> None:
        self._direccion = direccion

    @property
    def telefono(self) -> str:
        return self._telefono

    @telefono.setter
    def telefono(self, telefono: str) -> None:
        self._telefono = telefono

    def mostrar_notas(self) -> None:
        print(f"Notas del estudiante {self.nombre}:")
        for nota in self._notas:
            print(f"{nota:.2f}")


@dataclass
class Curso:
    _codigo: str
    _nombre: str
    _semestre: str
    _estudiantes: List[Estudiante] = field(default_factory=list)

    @property
    def codigo(self) -> str:
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo: str) -> None:
        self._codigo = codigo

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def semestre(self) -> str:
        return self._semestre
    
    @semestre.setter
    def semestre(self, semestre: str) -> None:
        self._semestre = semestre

    def mostrar_notas(self) -> None:
        print(f"Notas del curso {self.nombre}:")
        for estudiante in self._estudiantes:
            estudiante.mostrar_notas()


@dataclass
class Sistema:
    cursos: List[Curso] = field(default_factory=list)

    def buscar_curso(self, codigo: str) -> Curso:
        for curso in self.cursos:
            if curso.codigo == codigo:
                return curso
        return None

    def agregar_curso(self, curso: Curso) -> None:
        self.cursos.append(curso)

    def eliminar_curso(self, codigo: str) -> None:
        curso = self.buscar_curso(codigo)
        if curso:
            self.cursos.remove(curso)

    def agregar_estudiante(self, codigo: str, estudiante: Estudiante) -> None:
        curso = self.buscar_curso(codigo)
        if curso:
            curso._estudiantes.append(estudiante)


if __name__ == "__main__":
    sistema = Sistema()
    menu = Menu()
    menu.add_options(
        ("Crear curso",
        lambda: sistema.agregar_curso(
            Curso(input("Código: "), input("Nombre: "), input("Semestre: ")))),
        ("Buscar curso",
        lambda: print(sistema.buscar_curso(input("Código: ")))),
        ("Eliminar curso",
        lambda: sistema.eliminar_curso(input("Código: "))),
        ("Agregar estudiante",
        lambda: sistema.agregar_estudiante(
            input("Código: "),
            Estudiante(input("DNI: "),
            input("Nombre: "),
            input("Dirección: "),
            input("Teléfono: ")))),
        ("Información de estudiante", 
        lambda: print(
            sistema.buscar_curso(
                input("Código: ")).buscar_estudiante(input("DNI: ")))),
    )
    menu.run()