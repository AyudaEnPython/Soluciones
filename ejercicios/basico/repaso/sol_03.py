"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def main():
    mensaje = "Pago con "
    gasto = float(input("Ingresar gasto: "))
    if gasto <= 1000:
        mensaje += "dinero en efectivo"
    elif 1000 < gasto < 3000:
        mensaje += "tarjeta de débito"
    else:
        mensaje += "tarjeta de crédito"
    print(mensaje)


if __name__ == "__main__":
    main()
