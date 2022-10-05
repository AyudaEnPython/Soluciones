"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple
# pip install prototools
from prototools import float_input, tabulate, menu_input, int_input
from prototools.utils import text_align, ask_to_finish

ARTICULOS: Dict[str, int] = {
    "Tomate": 750,
    "Yuca": 900,
    "Papa": 550,
    "Sandia": 1_200,
}
LIMITE = 10_000
DESCUENTO = 0.05


def _descuento(monto: int) -> float:
    if monto > LIMITE:
        return monto * DESCUENTO
    return 0


def ingresar_pedido() -> Dict[str, int]:
    data = {k: 0 for k in ARTICULOS.keys()}
    while True:
        tipo = menu_input(tuple(ARTICULOS.keys()), numbers=True, lang="es")
        cantidad = int_input("Cantidad: ", min=1, lang="es")
        data[tipo] += cantidad
        if not ask_to_finish(lang="es"):
            return data


def ingresar_pago(monto: float) -> float:
    print(f"Monto a pagar: $ {monto:.2f}")
    pago = float_input("Ingresar pago: ", min=monto, lang="es")
    return pago, pago - monto


def calcular(data: Dict[str, int]) -> Tuple[float, float]:
    subtotal = 0
    cantidad = sum(data.values())
    for articulo, n in data.items():
        subtotal += ARTICULOS[articulo] * n
    descuento = _descuento(subtotal)
    return subtotal, cantidad, descuento


def main():
    data = ingresar_pedido()
    subtotal, cantidad, descuento = calcular(data)
    total = subtotal - descuento
    text_align("Boleta", align="center", width=46)
    print(tabulate(
        [
            ["Articulo", "Cantidad", "Precio", "Subtotal"],
            *[
                (k, str(v), str(ARTICULOS[k]), str(ARTICULOS[k]*v))
                for k, v in data.items()
            ],
            ["" for _ in range(4)],
            ["", "", "Subtotal", f"$ {subtotal:.2f}"],
            ["", "", "Descuento", f"$ {descuento:.2f}"],
            ["", "", "Total", f"$ {total:.2f}"],
        ],
        inner=False, border_type="borderless",
    ))
    pago, vuelto = ingresar_pago(total)
    print(
        f"\nPor la compra de los {cantidad} productos, "
        f"el total a pagar es de $ {total:.2f}.\n"
        f"El pago fue de $ {pago:.2f} y el vuelto de $ {vuelto:.2f}\n"
    )
    text_align("Gracias por su compra", width=46)


if __name__ == "__main__":
    main()
