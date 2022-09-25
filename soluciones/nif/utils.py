"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from datetime import date, datetime, timedelta
from typing import Any, Dict, List
# pip install prototools
from prototools import str_input, menu_input, date_input, yes_no_input

MIN, MAX = 10, 100
ESTADO = ("soltero(a)", "casado(a)", "viudo(a)")
Data = Dict[str, List[Any]]


def obtener_precio() -> int:
    return randint(MIN, MAX)


def _validar_nif(nif: str) -> str:
    if len(nif) != 8:
        raise ValueError("El nif debe tener 8 caracteres")
    return nif


def _validar_edad(fecha: datetime) -> int:
    today = date.today()
    edad = (today - fecha) // timedelta(days=365.2425)
    if edad < 15:
        raise ValueError("La edad debe ser mayor a 15")
    return edad


def _print(nombre, fecha, estado, pertenece):
    print(f"Nombre: {nombre}")
    print(f"Fecha de nacimiento: {fecha}")
    print(f"Estado civil: {estado}")
    print(f"Pertenece a la UE: {pertenece}")


def grabar(data: Data):
    try:
        nif = str_input("NIF: ", function=_validar_nif)
    except ValueError as e:
        print(e)
        return None
    nombre = str_input("Nombre: ")
    fecha = date_input("Fecha de nacimiento: ")
    try:
        fecha = _validar_edad(fecha)
    except ValueError as e:
        print(e)
        return None
    estado = menu_input(ESTADO, numbers=True, lang="es")
    pertenece = yes_no_input("¿Pertenece a la Unión Europea?", lang="es")
    data[nif] = [nombre, fecha, estado, pertenece]
    return data


def buscar(data: Data) -> None:
    try:
        nif = str_input("NIF: ", function=_validar_nif)
    except ValueError as e:
        print(e)
        return None
    if nif in data:
        print(f"NIF: {nif}")
        _print(*data[nif])
    return None


def imprimir(data: Data) -> None:
    if data is None:
        print("No hay datos")
        return None
    print(f"Costo: {obtener_precio()}")
    for nif, (nombre, fecha, estado, pertenece) in data.items():
        print(f"NIF: {nif}")
        _print(nombre, fecha, estado, pertenece)
        print("-" * 20)
