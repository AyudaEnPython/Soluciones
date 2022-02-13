"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Any, Dict, Tuple, Union
from prototools import Menu, int_input  # type: ignore

N = Union[int, float]
TARIFAS: Dict[str, Dict[str, Any]] = {
    "residencial": {
        "fijo": 299.37, "precio_kw": 3.37, "impuesto": 1.21,
        "lim": 250, "desc": 150, "iva": "21%",
    },
    "comercial": {
        "fijo": 315.25, "precio_kw": 4.55, "impuesto": 1.26,
        "lim": 150, "desc": 20, "iva": "26%",
    },
}


def ingresar(tipo: str) -> Tuple[int, int, str]:
    anterior = int_input("Ingrese lectura anterior: ", min=0, lang="es")
    actual = int_input("Ingrese lectura actual: ", min=anterior, lang="es")
    return anterior, actual, tipo


def calcular(anterior: int, actual: int, tipo: str) -> Tuple[str, N, N, N, N]:
    consumo = actual - anterior
    subtotal = TARIFAS[tipo]["precio_kw"] * consumo + TARIFAS[tipo]["fijo"]
    total = subtotal * TARIFAS[tipo]["impuesto"]
    descuento = TARIFAS[tipo]["desc"] if consumo < TARIFAS[tipo]["lim"] else 0
    return tipo, consumo, total, subtotal, descuento


def factura(tipo: str, consumo: N, total: N, subtotal: N, desc: N) -> None:
    print(f"\nSubtotal: {subtotal}\nImpuesto: {TARIFAS[tipo]['iva']}\n")
    if desc > 0:
        print(
            f"Su consumo es de {consumo}kw, su monto es de ${total}."
            f"\nRecibe bonificacion de ${desc} y debe abonar "
            f"${total - desc:.2f}."
        )
    else:
        print(
            f"Su consumo es de {consumo}kw, esta excedido y "
            f"debera abonar ${total:.2f}."
        )


def main():
    menu = Menu("Facturacion de servicio de electricidad")
    menu.add_options(
        ("Tarifa residencial", lambda:
            factura(*calcular(*ingresar("residencial")))),
        ("Tarifa comercial", lambda:
            factura(*calcular(*ingresar("comercial")))),
    )
    menu.run()


if __name__ == "__main__":
    main()
