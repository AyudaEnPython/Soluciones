"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que pida un número y que saque en secuencia la
palabra EMPRENDER tantas veces como sea el número ingresado.

Ejemplo:
Digite un numero: 4

Salida:
EMPRENDER
EMPRENDER
EMPRENDER
EMPRENDER
"""
# pip install prototools
from prototools import int_input


def repetir(n: int, frase: str = "EMPRENDER") -> None:
    for _ in range(n):
        print(frase)


def main():
    n = int_input("Digite un numero: ", min=1)
    repetir(n)


if __name__ == "__main__":
    main()
