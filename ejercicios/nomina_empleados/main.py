"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List
# pip install prototools
from prototools import int_input

PAGO = 10_000
Nomina = Dict[str, List[int]]


def _ingresar_nombre(nomina: Nomina) -> str:
    while True:
        nombre = input("Nombre: ")
        if nombre not in nomina:
            return nombre
        print("Nombre ya existe")


def obtener_nomina(n: int, m: int) -> Nomina:
    nomina = {}
    for i in range(n):
        print(f"Datos del empleado N°{i+1}")
        nombre = _ingresar_nombre(nomina)
        nomina[nombre] = [int_input(
            f"Ingresar horas trabajadas semana N°{j+1}: ",
            min=0, lang="es",
        ) for j in range(m)]
    return nomina


def _pago(horas: int, pago: int = PAGO) -> int:
    return horas * pago


def _gasto_semanal(i: int, nomina: Nomina) -> int:
    return sum(_pago(horas[i]) for horas in nomina.values())


def mostrar_salarios(nomina: Nomina) -> None:
    for nombre, horas in nomina.items():
        print(f"Empleado: {nombre} | Sueldo: $ {_pago(sum(horas))}")


def mostrar_semanal(m: int, nomina: Nomina) -> None:
    for i in range(m):
        print(f"Gastos (semana N°{i+1}): $ {_gasto_semanal(i, nomina)}")


def main():
    n = int_input("Ingresar cantidad de empleados: ", min=1, lang="es")
    m = int_input("Ingresar cantidad de semanas: ", min=1, lang="es")
    nomina = obtener_nomina(n, m)
    print("\nResultados:\n")
    mostrar_salarios(nomina)
    mostrar_semanal(m, nomina)


if __name__ == "__main__":
    main()
