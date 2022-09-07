"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa donde se registre la venta de uno o varios
artículos partiendo que el usuario debe registrar: cantidad de
artículos y el precio unitario de estos. Se desea conocer el monto a
abonar teniendo en cuenta que si la compra es superior a $1500 se
realiza un descuento del 7%.

Nota: Se aclara que el programa debe poder procesar más de un artículo
en la venta.
"""


def registro():
    cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))
    precio_unitario = float(input("Ingrese el precio unitario: "))

    monto_total = cantidad_articulos * precio_unitario
    if monto_total > 1500:
        monto_final = monto_total - monto_total * 0.07
    else:
        monto_final = monto_total

    print("El monto total a abonar es: $%.2f" % monto_final)


def main():
    while True:
        registro()
        continuar = input("¿Desea continuar? (S/N): ")
        if continuar.upper() == "N":
            break


if __name__ == "__main__":
    main()
