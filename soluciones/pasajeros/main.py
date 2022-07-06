"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import namedtuple
from typing import List
# pip install prototools
from prototools import Menu

Pasajero = namedtuple("Pasajero", "nombre cedula destino")
Destino = namedtuple("Destino", "ciudad pais")


def ingresar_datos(pasajeros: List[Pasajero]) -> None:
    nombre = input("Nombre: ")
    cedula = input("Cedula: ")
    ciudad = input("Ciudad: ")
    pais = input("Pais: ")
    destino = Destino(ciudad, pais)
    pasajero = Pasajero(nombre, cedula, destino)
    pasajeros.append(pasajero)


def mostrar_destino(pasajeros: List[Pasajero],cedula: str) -> None:
    for pasajero in pasajeros:
        if pasajero.cedula == cedula:
            print(f"Nombre: {pasajero.nombre}")
            print(f"Cedula: {pasajero.cedula}")
            print(f"Destino: {pasajero.destino.ciudad}")
            print(f"Pais: {pasajero.destino.pais}")
            break
    else:
        print(f"No se encontro pasajero con cedula {cedula}")


def cantidad_pasajeros(pasajeros: List[Pasajero], ciudad: str) -> None:
    cantidad = len([
        pasajero for pasajero in pasajeros
        if pasajero.destino.ciudad == ciudad
    ])
    print(f"Cantidad de pasajeros a {ciudad}: {cantidad}")


def main():
    pasajeros: List[Pasajero] = []
    menu = Menu("Ayuda en Python")
    menu.add_options(
        ("Ingresar datos", lambda: ingresar_datos(pasajeros)),
        ("Mostrar destino",
            lambda: mostrar_destino(
                pasajeros, 
                input("Ingresar cedula: "))),
        ("Mostrar cantidad de pasajeros a un destino",
            lambda: cantidad_pasajeros(
                pasajeros, 
                input("Ingresar ciudad: "))),
    )
    menu.run()


if __name__ == "__main__":
    main()
