"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from string import ascii_uppercase
from typing import Dict, List, Tuple
# pip install prototools
from prototools import int_input, textbox

MIN, MAX, GRUPOS = 10, 35, 3
Data = Dict[str, int]


def inscribir() -> Data:
    grupos: Data = {k:0 for k in ascii_uppercase[:GRUPOS]}
    for grupo in grupos:
        grupos[grupo] += int_input(f"[{grupo}] Cantidad de alumnos: ", min=0)
    return grupos


def _disponibilidad(grupos: Data, valor: int) -> List[Tuple[str, int]]:
    return [
        (grupo, grupos[grupo]) for grupo in grupos
        if grupos[grupo] <= valor
    ]


def _sobrecupo(grupos: Data) -> List[Tuple[str, int]]:
    return [
        (grupo, grupos[grupo] - MAX) for grupo in grupos
        if grupos[grupo] > MAX
    ]


def informe(grupos: Data) -> None:
    textbox("Informe")
    print("Grupos disponibles:")
    for grupo, cantidad in _disponibilidad(grupos, MAX):
        if cantidad > MIN:
            print(f"Grupo {grupo} | Disponibles: {MAX - cantidad} cupos")
    print("\nGrupos no disponibles:")
    for grupo, cantidad in _disponibilidad(grupos, MIN):
        print(f"Grupo {grupo} | inscritos al momento: {cantidad}")
    print("\nGrupos sobrecupados:")
    for grupo, cantidad in _sobrecupo(grupos):
        print(f"Grupo {grupo} | sobre cupo: {cantidad} estudiantes")


def main():
    data: Data = inscribir()
    informe(data)


if __name__ == "__main__":
    main()
