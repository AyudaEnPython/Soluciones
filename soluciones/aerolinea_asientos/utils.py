"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import int_input, str_input
from typing import Dict, List

ASIENTOS = 42
POR_FILA = 6
CLASE: Dict[str, int] = {"normal": 75_000, "vip": 250_000}


def _validation(s: str) -> str:
    if not s.isdigit():
        raise ValueError("Debe ingresar solo números")
    if len(s) != 8:
        raise ValueError("Debe ingresar un RUT válido")
    return s


def _disponible(asientos: List[bool], asiento: int) -> bool:
    return asientos[asiento - 1]


def asientos_disponibles(asientos: List[bool], n: int = 3, m: int = 7) -> str:
    out = ""
    for i in range(0, ASIENTOS, POR_FILA):
        out += f"{'|':<3}"
        for j in range(i, i + POR_FILA):
            if j % n == 0 and j != i:
                out += " " * m
            if asientos[j]:
                out += f"{j+1:>4}"
            else:
                out += f"{'X':>4}"
        out += f"{'|':>5}\n"
        if i == POR_FILA*4:
            out += f"|{'_'*(2*m+1)}{' '*m}{'_'*(2*m+1)}|\n"*2
        if i != POR_FILA*6 and i != POR_FILA*4 or i == POR_FILA*5:
            out += f"|{' '*(12*n+1)}|\n"
        if i == POR_FILA*5:
            out += f"|{' '*(12*n+1)}|\n"
    return out


def comprar_pasaje(asientos: List[bool], pasajeros: Dict[int, str]) -> None:
    try:
        rut = str_input("RUT: ", function=_validation)
    except ValueError as e:
        print(e)
        return None
    asiento = int_input("Asiento: ", min=1, max=ASIENTOS)
    if not _disponible(asientos, asiento):
        print("Asiento no disponible")
        return None
    asientos[asiento - 1] = False
    pasajeros[asiento] = rut


def estadisticas(asientos: List[bool]) -> str:
    normales = sum(1 for asiento in asientos[:30] if not asiento)
    vip = sum(1 for asiento in asientos[30:] if not asiento)
    recaudado = normales * CLASE["normal"] + vip * CLASE["vip"]
    return (
        f"{'Asientos Vip vendidos:':>28} {vip}\n"
        f"{'Asientos Normales vendidos:':>28} {normales}\n"
        f"{'Total recaudado:':>28} ${recaudado}"
    )


def anular_venta(asientos: List[bool], pasajeros: Dict[int, str]) -> None:
    asiento = int_input("Asiento: ", min=1, max=ASIENTOS)
    if _disponible(asientos, asiento):
        print("Asiento no vendido")
        return None
    asientos[asiento - 1] = True
    del pasajeros[asiento]


def listar_pasajeros(pasajeros: Dict[int, str]) -> None:
    if not pasajeros:
        print("No hay pasajeros")
        return None
    pasajeros = dict(sorted(pasajeros.items(), key=lambda x: x[0]))
    for asiento, rut in pasajeros.items():
        print(f"Asiento {asiento}: {rut}")
