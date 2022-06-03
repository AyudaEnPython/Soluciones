"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from utils import contar_espacios, contar_vocales, to_upper


def main():
    text = input("> ")
    print(f"Espacios: {contar_espacios(text)}")
    print(f"Vocales: {contar_vocales(text)}")
    print(f"Mayúsculas: {to_upper(text)}")


if __name__ == "__main__":
    main()
