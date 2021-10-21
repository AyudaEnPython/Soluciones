"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solución completa en:
https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/palabras_largas.py
"""
from prototools.entradas import entrada_int


def solver(s: str, n: int) -> bool:
    return any(len(e) >= n for e in s.split())


def main():
    s = input("Ingresar cadena: ")
    n = entrada_int("k: ", min=1) # pip install prototools
    print("Hay palabras largas" if solver(s, n) else "No hay palabras largas")


if __name__ == "__main__":
    main()