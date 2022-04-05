"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Mostrar en pantalla una pirámide de tamaño T, usando como relleno las
letras del alfabeto.

Ejemplo:
Si t = 7, entonces:
#       A
#      ABC
#     ABCDE
#    ABCDEFG
"""
from string import ascii_uppercase


def piramide(t: int = 7) -> None:
    t = t + 1 if t % 2 == 0 else t
    s = ascii_uppercase[:t]
    for i in range(0, t+1, 2):
        print(" "*(t - i//2) + s[:i+1])


def main():
    t = int(input("Tamaño: "))
    print()
    piramide(t)


if __name__ == "__main__":
    main()
