"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple
# pip install prototools
from prototools import menu_input, int_input, tabulate
from prototools.utils import text_align, main_loop, ask_to_finish

TIPO = {"lucuma": 2.5, "fresa": 1.3, "mango": 2.0, "leche": 1.7}


def ingresar_pedido() -> Dict[str, int]:
    """Pide al usuario los datos para calcular el precio de la compra.

    :return: Cantidad de cada helado
    :rtype: Dict[str, int]
    """
    data = {"lucuma": 0, "fresa": 0, "mango": 0, "leche": 0}
    while True:
        tipo = menu_input(tuple(TIPO.keys()), numbers=True, lang="es")
        cantidad = int_input("Cantidad: ", min=1)
        data[tipo] += cantidad
        if not ask_to_finish(lang="es"):
            return data


def _descuento(cantidad: int, total: float) -> float:
    """Calcula el descuento a aplicar. Si la cantidad de helados es
    mayor a 7, el descuento es del 10% de lo que se compro; de lo
    contrario no se aplica descuento.

    :param cantidad: Cantidad de helados
    :type cantidad: int
    :param total: Total de la compra
    :type total: float
    :return: Descuento a aplicar
    :rtype: float
    """
    if cantidad >= 7:
        return total * 0.1
    return 0


def calcular(data: Dict[str, int]) -> Tuple[float, int, float]:
    """Calcula el total, cantidad y descuento a aplicar.

    :param data: Cantidad de cada helado
    :type data: Dict[str, int]
    :return: Total, cantidad y descuento
    :rtype: Tuple[float, int, float]
    """
    total = 0
    cantidad = sum(data.values())
    for helado, n in data.items():
        total += TIPO[helado] * n
    descuento = _descuento(cantidad, total)
    return total, cantidad, descuento


def main_():
    data = ingresar_pedido()
    total, cantidad, descuento = calcular(data)
    text_align("Boleta", align="center", width=38)
    print(tabulate(
        [
            ["Cantidad", cantidad],
            ["Importe", f"$ {total:.2f}"],
            ["Descuento", f"{descuento:.2f}"],
            ["Total a pagar", f"$ {total - descuento:.2f}"],
        ],
        headers=["Descripción", "Detalle"], align="right",
    ))
    text_align("Gracias por su compra", width=38)


if __name__ == "__main__":
    main_loop(main_)
