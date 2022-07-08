"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Tuple
# pip install prototools
from prototools import Menu, menu_input, int_input, textbox

PRECIOS = {
    "Termometro": 2999,
    "Mascarillas": 2190,
    "Vendas": 500,
    "Aposito": 370,
}
IDX = {k:i for i, k in enumerate(PRECIOS.keys())}


def _search(data: List[int], value: int) -> str:
    return list(IDX.keys())[data.index(value)]


def _promedio(data: List[int]) -> float:
    return sum(data) / len(data)


def superior_inferior(data: List[int]) -> Tuple[List[str], List[str]]:
    superior = list(set(
        [_search(data, x) for x in data if x >= _promedio(data)]
    ))
    inferior = list(set(
        [_search(data, x) for x in data if x <= _promedio(data)]
    ))
    return superior, inferior


def informe(data: List[int]) -> None:
    textbox("Informe de Insumos", 52)
    for insumo, cantidad in zip(IDX.keys(), data):
        print(
            f"Insumo:{insumo:>12} | Cantidad:{cantidad:>4} | "
            f"Total:{cantidad * PRECIOS[insumo]:>8}"
        )
    if not all(cantidad == 0 for cantidad in data):
        print(f"\nMenos comprado: {_search(data, min(data))}")
        print(f"Mas comprado: {_search(data, max(data))}")
        superior, inferior = superior_inferior(data)
        print(f"\nSuperiores al promedio: {', '.join(superior)}")
        print(f"Inferiores al promedio: {', '.join(inferior)}")


def ingresar_compra(insumos: List[int]) -> None:
    insumo = menu_input(tuple(PRECIOS.keys()), numbers=True, lang="es")
    cantidad = int_input("Cantidad: ", lang="es")
    insumos[IDX[insumo]] += cantidad


def main():
    insumos = [0] * len(PRECIOS)
    menu = Menu()
    menu.add_options(
        ("Ingresar compra", lambda: ingresar_compra(insumos)),
        ("Mostrar informe", lambda: informe(insumos)),
    )
    menu.run()


if __name__ == "__main__":
    main()
