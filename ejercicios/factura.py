"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcular el total de una factura, la cual contiene 6 ítems, el sistema
debe solicitar los 6 productos, luego el costo unitario de cada uno y
luego la cantidad de productos a llevar.

El sistema debe calcular el total de la factura e indicar cuanto es el
IVA (19%) de esta compra, si el total de la factura es de menos de
$100000, mostrar no se le aplicara descuento al cliente, si el total de
la factura esta entre $100000 y 200000 se le aplicara descuento del 5%
a los productos que tenga un costo unitario superior a 20000, si el
total de la factura es superior a $200000, debe generar un 10% al total
de la factura antes de IVA.

Al mostrar el resultado de la factura debe preguntar al usuario si
desea continuar facturando o no, si el usuario decide no seguir
facturando el sistema debe mostrar el total facturado, el total de los
descuentos y el total IVA facturado.

TODO: add tests later.
"""
from typing import Dict, Union

ITEMS, IVA, Data = 6, 0.19, Dict[str, Dict[str, Union[float, int]]]


def ingresar_datos() -> Data:
    """Función que solicita los datos del producto.

    :return: Diccionario con los datos de los productos.
    :rtype: Dict[str, Dict[str, Union[float, int]]]
    """
    print("Ingreso de datos "+"-"*16+"\n")
    productos = [
        input(f"Nombre del producto [{i+1}]: ") for i in range(ITEMS)
    ]
    costos = [
        float(input(f"Costo unitario [{i}][{producto}]: "))
        for i, producto in enumerate(productos, 1)
    ]
    cantidades = [
        int(input(f"Cantidad [{i}][{producto}]: "))
        for i, producto in enumerate(productos, 1)
    ]
    return {
        producto: {
            "costo": costo, "cantidad": cantidad, "precio": costo * cantidad
        }
        for producto, (costo, cantidad)
        in zip(productos, zip(costos, cantidades))
    }


def total_factura(productos: Data) -> float:
    """Función que calcula el total de la factura.

    :param productos: Diccionario con los datos de los productos.
    :type productos: Dict[str, Dict[str, Union[float, int]]]
    :return: Total de la factura.
    :rtype: float
    """
    return float(sum(v["precio"] for _, v in productos.items()))


def obtener_descuento(total: float, productos: Data) -> float:
    """Función que obtiene el descuento del total de la factura.

    :param total: Total de la factura.
    :type total: float
    :param productos: Diccionario con los datos de los productos.
    :type productos: Dict[str, Dict[str, Union[float, int]]]
    :return: Descuento.
    :rtype: float
    """
    return {
        total < 100000: 0,
        100000 <= total < 200000: sum(
                v["precio"]*0.05 for _, v in productos.items()
                if v["costo"] > 20_000
            ),
        total >= 200000: total * 0.1,
    }[True]


def mostrar(
    total: float,
    descuento: float,
    total_iva: float,
    total_con_descuento: float,
) -> None:
    print("\nFactura "+"-"*25)
    print(f"{'Total:':>20} {total:>12.2f}")
    print(f"{'Descuento:':>20} {descuento:>12.2f}")
    print(f"{'IVA:':>20} {total_iva:>12.2f}")
    print(f"{'Total con descuento:':>20} {total_con_descuento:>12.2f}")
    print(f"{'Total con IVA:':>20} {total_con_descuento + total_iva:>12.2f}")
    print("-"*33)


def procesar():
    data = ingresar_datos()
    total = total_factura(data)
    descuento = obtener_descuento(total, data)
    total_con_descuento = total - descuento
    total_iva = total * IVA
    mostrar(total, descuento, total_iva, total_con_descuento)


def main():
    while True:
        procesar()
        if input("¿Desea continuar? (s/n): ").lower() == "n":
            break


if __name__ == "__main__":
    procesar()
