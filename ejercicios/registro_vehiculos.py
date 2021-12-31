"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un programa que permita llevar el registro de los vehículos del
estacionamiento del IESTP-JULIACA utilizando como estructura de
almacenamiento listas. Los datos solicitados por cada vehículo son:
placa, marca, modelo, año y precio. El programa debe permitir realizar
agregar un vehiculo por teclado.
"""
from typing import List, Tuple


def registrar() -> Tuple(str, str, str, str, str):
    placa = input("Ingrese la placa del vehiculo: ")
    marca = input("Ingrese la marca del vehiculo: ")
    modelo = input("Ingrese el modelo del vehiculo: ")
    year = input("Ingrese el año del vehiculo: ")
    precio = input("Ingrese el precio del vehiculo: ")
    return placa, marca, modelo, year, precio


def main_():
    vehiculos: List = []
    while True:
        placa, marca, modelo, year, precio = registrar()
        vehiculos.append([placa, marca, modelo, year, precio])
        opcion = input("Desea agregar otro vehiculo? (s/n) ")
        if opcion == "n":
            break
    print("Vehiculos registrados: ")
    for vehiculo in vehiculos:
        print(vehiculo)


if __name__ == "__main__":
    main_()