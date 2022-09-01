"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dar cambio. Escriba un programa CajaRegistradora. La caja registradora
le ayuda a un cajero a devolver el cambio en bolivianos al cliente.
Para ello lea dos números: total de la venta y pago que realiza el
cliente, seguidamente imprima la devolución del cambio en monedas al
cliente, fraccionados de la siguiente manera:

5 bolivianos
2 bolivianos
1 boliviano
50 centavos
20 centavos
10 centavos

Aqui está un ejemplo de código:

total = float(input("Total Venta: "))
pago = float(input("Pago: "))
cambio = total - pago
...
print("CAMBIO: ", cambio)
print("5 bolivianos: ", cinco)
print("2 bolivianos: ", dos)
print("1 boliviano: ", uno)
print("50 centavos: ", cincuenta)
print("20 centavos: ", veinte)
print("10 centavos: ", diez)

Ejemplo de entrada
Total Venta: 81.20
Pago: 100

Ejemplo de salida
CAMBIO: 18.80
5 bolivianos: 3
2 bolivianos: 1
1 bolivianos: 1
50 centavos: 1
20 centavos: 1
10 centavos: 1
"""
from typing import Dict, Union
# pip install prototools
from prototools import float_input


def dar_cambio(x: int) -> Dict[Union[int, float], int]:
    t = {5: 0, 2: 0, 1: 0, .5: 0, .2: 0, .1: 0}
    for y in t:
        if x >= y:
            t[y] = x // y
            x %= y
        x = round(x, 2)
    return t


def mostrar(r: Dict[Union[int, float], int]) -> None:
    for k in r:
        print(f"{k if k % 1 == 0 else int(k*100)} bolivianos: {int(r[k])}")


def main():
    total = float_input("Total de la venta: ", min=0)
    pago = float_input("Pago: ", min=total)
    cambio = round(pago - total, 2)
    resultado = dar_cambio(cambio)
    print(f"CAMBIO: {cambio:.2f}")
    mostrar(resultado)


if __name__ == "__main__":
    main()
