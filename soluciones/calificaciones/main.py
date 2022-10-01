from dataclasses import dataclass
from prototools import Menu, float_input, int_input
from typing import Dict, List

Data = Dict[int, List[List[float]]]


def _crear_estudiante():
    id_ = int_input("Ingrese el ID del estudiante: ")
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    return id_, nombre, apellido


def _agregar_nota():
    id_ = int_input("Ingrese el ID del estudiante: ")
    nota = float_input("Ingresar nota: ")
    return id_, nota


def _modificar_nota():
    id_ = int_input("Ingrese el ID del estudiante: ")
    posicion = int_input("Ingrese la posicion de la nota: ")
    nota = float_input("Ingresar nueva nota: ")
    return id_, posicion, nota


def _eliminar_estudiante(data: Data):
    id_ = int_input("Ingrese el ID del estudiante: ")
    del data[id_]
    return data


def _mostrar_informacion(data: Data):
    for k, v in data.items():
        print(f"ID: {k}")
        print(f"Nombre: {v[0]} {v[1]}")
        print(f"Notas: {v[2]}")


@dataclass
class Sistema():
    data: Data

    def crear_estudiante(self):
        id_, nombre, apellido = _crear_estudiante()
        self.data[id_] = [nombre, apellido, []]

    def agregar_nota(self):
        id_, nota = _agregar_nota()
        self.data[id_][2].append(nota)

    def modificar_nota(self):
        id_, posicion, nota = _modificar_nota()
        self.data[id_][2][posicion] = nota

    def eliminar_estudiante(self):
        self.data = _eliminar_estudiante(self.data)

    def informacion(self):
        _mostrar_informacion(self.data)


def main():
    data: Data = {}
    sistema = Sistema(data)
    menu = Menu()
    menu.add_options(
        ("Crear estudiante", sistema.crear_estudiante),
        ("Agregar/Modificar calificaciones", sistema.agregar_nota),
        ("Consultar calificaciones", sistema.informacion),
        ("Eliminar estudiante", sistema.eliminar_estudiante),
    )
    menu.run()


if __name__ == "__main__":
    main()
