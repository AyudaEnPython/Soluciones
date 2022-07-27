"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import List, Tuple
# pip install prototools
from prototools import Menu, str_input, date_input_dmy


@dataclass
class Persona:
    cedula: str
    apellidos: str
    nombres: str
    fecha_nacimiento: str

    def __str__(self) -> str:
        return (
            f"Cédula: {self.cedula}\n"
            f"Apellidos y Nombres: {self.apellidos}, {self.nombres}\n"
            f"Fecha de Nacimiento: {self.fecha_nacimiento}"
        )


def _buscar_cedula(data: List[Persona], cedula: str) -> Tuple[bool, Persona]:
    for persona in data:
        if persona.cedula == cedula:
            return True, persona
    return False, None


def _cedula_no_repetida(data: List[Persona]) -> str:
    while True:
        cedula = str_input("Cédula: ")
        encontrado, _ = _buscar_cedula(data, cedula)
        if not encontrado:
            return cedula
        print("Ya existe la cédula, ingrese otra")


def datos_personales(data: List[Persona]) -> None:
    cedula = _cedula_no_repetida(data)
    apellidos = str_input("Apellidos: ")
    nombres = str_input("Nombres: ")
    fecha_nacimiento = date_input_dmy("Fecha de nacimiento (mm/dd/aa): ")
    persona = Persona(cedula, apellidos, nombres, fecha_nacimiento)
    data.append(persona)


def buscar(data: List[Persona]) -> None:
    cedula = str_input("Cédula: ")
    encontrado, persona = _buscar_cedula(data, cedula)
    if encontrado:
        print(persona)
    else:
        print("No se encontró la cédula")


def mostrar(data: List[Persona]) -> None:
    for persona in data:
        print(persona)


def main():
    data: List[Persona] = []
    menu = Menu("Ingreso de Información")
    menu.add_options(
        ("Datos Personales", lambda: datos_personales(data)),
        ("Consultar por cédula", lambda: buscar(data)),
        ("Consultar todos", lambda: mostrar(data)),
    )
    menu.run()


if __name__ == "__main__":
    main()
