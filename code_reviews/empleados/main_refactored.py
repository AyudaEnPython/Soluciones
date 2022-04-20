"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: take a second look if there's a bug in the code.
"""
from typing import Tuple
from prototools import Menu, float_input, date_input, tabulate

HEADERS = (
    "Nombre", "Fecha de nacimiento", "Cargo", "Sueldo", "Descuento", "Neto"
)


def _guardar(data: Tuple[str, str, str, float]) -> None:
    with open("data.txt", "a") as f:
        f.write(f"{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]}\n")


def agregar() -> None:
    nombre = input("Nombre: ")
    fecha = date_input("Fecha de nacimiento: ")
    cargo = input("Cargo: ")
    sueldo = float_input("Sueldo: ", min=0)
    descuento = sueldo*0.1 if sueldo > 1800 else 0
    neto = sueldo - descuento
    _guardar((nombre, fecha, cargo, sueldo, descuento, neto))


def buscar() -> None:
    nombre = input("Nombre: ")
    with open("data.txt", "r") as f:
        for line in f.read().splitlines():
            if nombre in line:
                data = line
    data = [[d for d in data.split(",")]]
    print(tabulate(data, headers=HEADERS))


def mostrar() -> None:
    with open("data.txt", "r") as f:
        data = f.read().splitlines()
    data = [d.split(",") for d in data]
    print(tabulate(data, headers=HEADERS))


def main():
    menu = Menu()
    menu.add_options(
        ("Añadir empleados", agregar),
        ("Buscar empleados", buscar),
        ("Ver empleados", mostrar)
    )
    menu.run()


if __name__ == "__main__":
    main()
