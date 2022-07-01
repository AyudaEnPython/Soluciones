"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que permita cargar una indeterminada cantidad de
registros en una matriz con la siguiente estructura de datos:

N° DE CUENTA (código de 5 dígitos alfanuméricos)
DNI
NOMBRE Y APELLIDO
SALDO (valor númerico real)

Se debe validar que el dato ingresado como N° DE CUENTA, tenga
exactamente 5 dígitos, y el dato ingresado como DNI tenga exactamente
8 dígitos. Se sugiere hacer estas validaciones con funciones (
preferentemente una única función).

Al terminar la carga los datos deben quedar guardados en un archivo
binario. Y debe consultarse al usuario si se quiere generar un archivo
de texto. Si se responde que sí, generarlo con el nombre "cuentas.txt".
"""
import struct
from typing import Any, List, Tuple


def validar(dato: str, n: int) -> str:
    if not dato.isdigit():
        raise ValueError("Debe ingresar unicamente números")
    if len(dato) != n:
        raise ValueError(f"Debe tener {n} dígitos")
    return dato


def get_registro() -> Tuple[str, ...]:
    cuenta = validar(input("Ingrese el número de cuenta: "), 5)
    dni = validar(input("Ingrese el DNI: "), 8)
    nombre = input("Ingrese el nombre: ")
    saldo = float(input("Ingrese el saldo: "))
    return [cuenta, dni, nombre, saldo]


def get_data() -> List[List[Any]]:
    data = []
    while True:
        opcion = input("¿Desea cargar un registro? (s/n): ").lower()
        if opcion.startswith("s"):
            try:
                data.append(get_registro())
            except ValueError as e:
                print(e)
        else:
            break
    return data


def save_bin(filename: str, data: List[List[Any]]) -> None:
    data = [[
        s.encode() if isinstance(s, str) else struct.pack("f", s)
        for s in reg
    ] for reg in data]
    data = b"".join(b"".join(reg) for reg in data)
    with open(f"{filename}.bin", "wb") as f:
        f.write(data)


def save_txt(filename: str, data: List[List[Any]]) -> None:
    with open(f"{filename}.txt", "w") as f:
        for row in data:
            f.write(", ".join(str(s) for s in row) + "\n")


def main():
    data = get_data()
    save_bin("cuentas", data)
    mode = input("¿Desea generar un archibo de texto? (s/n): ").lower()
    if mode.startswith("s"):
        save_txt("cuentas", data)


if __name__ == "__main__":
    main()
