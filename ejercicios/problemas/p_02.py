"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict


# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/contar_vocales_consonantes_digitos.py
def solver(frase: str) -> Dict[str, int]:
    frase: str = frase.lower()
    vocales: int = 0
    consonantes: int = 0
    digitos: int = 0
    for caracter in frase:
        if caracter in "aeiou":
            vocales += 1
        elif caracter in "bcdfghjklmnñpqrstvwxyz":
            consonantes += 1
        elif caracter in "0123456789":
            digitos += 1
    return {
        "vocales": vocales, "consonantes": consonantes, "digitos": digitos
    }


def main():
    frase = input("Frase: ")
    resultado = solver(frase)
    print(f"Cantidad de vocales: {resultado['vocales']}")
    print(f"Cantidad de consonantes: {resultado['consonantes']}")


if __name__ == "__main__":
    main()
