"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu, int_input


def _es_multiplo(a: int, b: int) -> bool:
    return a % b == 0


def _es_perfecto(n: int) -> bool:
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    return False


def main():
    menu = Menu()
    menu.add_options(
        ("Multiplo", lambda: print(_es_multiplo(int_input("n: ", min=1), 5))),
        ("Perfecto", lambda: print(_es_perfecto(int_input("n: ", min=1)))),
    )
    menu.run()


if __name__ == "__main__":
    main()
