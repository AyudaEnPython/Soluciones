"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Crea un programa en python para resolver el siguiente problema. Luis
fue a una tienda de ropa a comprar unos zapatos, un pantalón y una
camisa. El necesita saber cuánto es el total que debe pagar por la
comprar de los 30 numero de artículos. La tienda tiene una promoción
por venta de liquidación de verano del 30% de descuento en compras
mayores a $2,000.00. Desarrolla el programa en Python de tal forma que
le ayudes a Luis a saber si a su compra de le aplicara el descuento
correspondiente o realizara un pago sin descuento.

# ------------------------ Enunciado Modificado -----------------------
Luis fue a una tienda de ropa a comprar unos zapatos, un pantalón y una
camisa. El necesita saber cuánto es el total que debe pagar por la
comprar de los artículos.
La tienda tiene una promoción por venta de liquidación de verano del
30% de descuento en compras mayores a $2,000.00.

Desarrolla el programa en Python de tal forma que le ayudes a Luis a
saber si a su compra se le aplicará el descuento correspondiente o
realizará un pago sin descuento.

NOTE: El enunciado original tiene errores ortográficos y no es claro.
"""
# pip install prototools
from prototools import menu_input, int_input, textbox

LIMITE = 2000
STOCK = {"Zapatos": 150, "Pantalón": 200, "Camisa": 100}


def compra():
    monto = 0
    while True:
        articulo = menu_input(tuple(STOCK.keys()), numbers=True, lang="es")
        cantidad = int_input("Cantidad: ", min=1, lang="es")
        monto += STOCK[articulo] * cantidad
        if input("¿Desea continuar? (s/n): ").lower() == "n":
            return monto


def main():
    descuento = 0
    monto = compra()
    if monto > LIMITE:
        descuento = monto * 0.3
    textbox("Informe de Compra", 52)
    print(f"Descuento: ${descuento:>8}")
    print(f"Monto a pagar: ${monto - descuento:>8}")


if __name__ == "__main__":
    main()
