"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import float_input, menu_input, yes_no_input, main_loop

from vehiculos import Auto, Moto

TIPO = ("auto", "moto")


def ingresar_datos(tipo):
    marca = input("Ingrese la marca del vehiculo: ")
    modelo = input("Ingrese el modelo del vehiculo: ")
    km = float_input("Ingrese los km recorridos: ", min=0)
    precio = float_input("Ingrese el precio del vehiculo: ", min=0)
    if tipo == "auto":
        airbag = yes_no_input("¿Tiene airbag? (s/n): ")
        return marca, modelo, km, precio, airbag
    else:
        casco = yes_no_input("¿Tiene casco? (s/n): ", yes_value="s", no_value="n")
        return marca, modelo, km, precio, casco


def main():
    tipo = menu_input(TIPO, numbers=True)
    data = ingresar_datos(tipo)
    if tipo == "auto":
        vehiculo = Auto(*data)
    else:
        vehiculo = Moto(*data)
    print(f"\nEl precio del vehiculo es: ${vehiculo.obtener_precio()}")


if __name__ == "__main__":
    main_loop(main)