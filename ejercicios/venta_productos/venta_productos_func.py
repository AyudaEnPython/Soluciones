"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple
# pip install prototools
from prototools import Menu, menu_input, float_input, tabulate, textbox

productos: Dict[str, float] = {
    "P1": {"cantidad": 0, "precio": 15.0},
    "P2": {"cantidad": 0, "precio": 17.5},
    "P3": {"cantidad": 0, "precio": 20.0},
}
ventas = {k: 0 for k in productos.keys()}
total = [0]


def _ingresar() -> Tuple[str, float]:
    producto = menu_input(tuple(productos.keys()), numbers=True)
    cantidad = float_input("Cantidad: ")
    return producto, cantidad


def _mostrar(producto: str, importe: float) -> None:
    print(tabulate(
        [
            ["Producto", producto],
            ["Cantidad", productos[producto]["cantidad"]],
            ["Precio unitario", productos[producto]["precio"]],
            ["Total a pagar", importe],
        ],
        headers=["Descripción", "Importe"],
    ))
    textbox("Gracias por su compra", width=30)


def ingresar_venta() -> None:
    producto, cantidad = _ingresar()
    productos[producto]["cantidad"] += cantidad
    importe = productos[producto]["precio"] * cantidad
    total[0] += importe
    ventas[producto] += 1
    _mostrar(producto, importe)


def ver_ventas() -> None:
    textbox("Cantidad de ventas efectuadas por producto", width=50)
    for k, v in ventas.items():
        print(f"{k}: {v}")


def ver_total() -> None:
    textbox(f"Total: {total[0]}", width=30)


def main():
    menu = Menu()
    menu.add_options(
        ("Ingresar venta", ingresar_venta),
        ("Ventas efectuadas", ver_ventas),
        ("Ver total", ver_total),
    )
    menu.run()


if __name__ == "__main__":
    main()
