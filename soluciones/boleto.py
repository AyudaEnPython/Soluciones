"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------ 
Una empresa de conciertos desea desarrollar un simulador para calcular
el precio por la venta de boletos para un evento. La empresa ofrece dos
tipos de boletos: gradas y general. Desarrolla un programa en Python
que pida al usuario el tipo y número de boletos, y realice lo
siguiente:

a. Que calcule e imprima el precio de la venta de boletos, considerando
    que las gradas cuestan 925 pesos y la entrada general 810 pesos. La
    empresa establece un máximo de 12 boletos por transacción, para 
    evitar revendedores, por lo que el programa debe validar este dato
    y mostrar un mensaje al usuario.
b. Los precios no incluyen IVA, del 16%. El programa debe calcular este
    cargo adicional implementando una función.
c. El programa debe permitir que el usuario repita el cálculo del
    importe a pagar por la compra de boletos tantas veces como quiera,
    hasta que indique que desea terminar.

Ejemplo:

- Tipo boleto: general
- Número de boletos: 3
- Precio de la compra: 3 x 810 = 2430
- IVA: 388
- Total a pagar: 2818.8 pesos
# ---------------------------------------------------------------------
"""
from typing import Dict
# pip install prototools
from prototools import choice_input, int_input, main_loop, tabulate, text_align

IVA: float = 0.16
TIPO: Dict[str, int] = {"grada": 925, "general": 810}


def ingresar_datos():
    """Pide al usuario los datos para calcular el precio de la compra
    de boletos.

    :return: tipo, cantidad
    :rtype: tuple
    """
    text_align("Datos de la compra", width=35)
    tipo: str = choice_input(tuple(TIPO.keys()))
    cantidad: int = int_input("Ingrese el número de boletos: ", min=1, max=12)
    return tipo, cantidad


def calcular_precio(tipo: str, cantidad: int):
    """Calcula el precio de la compra de boletos.
    
    :param tipo: tipo de boleto
    :tipo type: str
    :param cantidad: número de boletos
    :tipo type: int
    :return: precio, iva, total
    :rtype: tuple
    """
    precio = cantidad * TIPO[tipo]
    iva = precio * IVA
    return precio, iva, precio + iva


def main():
    tipo, cantidad = ingresar_datos()
    precio, iva, total = calcular_precio(tipo, cantidad)
    text_align("Boleta", align="center", width=38)
    print(tabulate(
        [
            ["Tipo boleto", tipo],
            ["Número de boletos", cantidad],
            ["Precio de la compra", f"$ {precio:.2f}"],
            ["IVA", f"$ {iva:.2f}"],
            ["Total a pagar", f"$ {total:.2f}"],
        ],
        headers=["Descripción", "Importe"], align="right",
    ))
    text_align("Gracias por su compra", width=38)


if __name__ == "__main__":
    main_loop(main)
