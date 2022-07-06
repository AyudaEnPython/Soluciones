"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from funciones import mcd, factores, es_abundante
# pip install prototools
from prototools import Menu, int_input, textbox


def main():
    menu = Menu("Ayuda en Python")
    menu.add_options(
        ("Calcular mcd",
            lambda: print(mcd(int_input("a: "), int_input("b: ")))),
        ("Calcular factores",
            lambda: print(factores(int_input("n: ")))),
        ("Es abundante",
            lambda: print(es_abundante(int_input("n: ")))),
    )
    menu.run()


if __name__ == "__main__":
    main()
