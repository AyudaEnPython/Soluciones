"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que permita ingresar un texto y que calcule las
siguientes operaciones:
- Cantidad de espacios en blanco.
- Cantidad de vocales.
- Convierta el texto en mayúsculas.
"""
# pip install prototools
from prototools import str_input


def to_upper(text: str) -> str:
    return text.upper()


def contar_espacios(text: str) -> int:
    return text.count(" ")


def contar_vocales(text: str) -> int:
    return sum(1 for c in text if c in "aeiouáéíóúAEIOUÁÉÍÓÚ")


def main():
    text = str_input("> ")
    print(f"Espacios: {contar_espacios(text)}")
    print(f"Vocales: {contar_vocales(text)}")
    print(f"Mayúsculas: {to_upper(text)}")


if __name__ == "__main__":
    main()
