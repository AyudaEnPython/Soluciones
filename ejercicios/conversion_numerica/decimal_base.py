"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Conversión Numérica
-------------------

Diseñar un programa que realice conversiones entre los diferentes
sistemas numéricos y para la verificación de su funcionamiento
realizar las conversiones numéricas dadas en el punto 1 del Taller
1 Unidad.

(28496)_10 a base 2, base 8 y base 16
(234,56)_10 a base 2, base 8 y base 16
(34526)_8 a base 2, base 10 y base 16
(F4A56)_16 a base 2, base 8 y base 10
(1100101011)_2 a base 8, base 10 y base 16
(11001100,11011)_2 a base 8, base 10 y base 16
"""


def ascii_value(c):
    if (c >= '0' and c <= '9'):
        return ord(c) - 48
    else:
        return ord(c) - 65  + 10


def to_decimal(sn, b):
    p = 1
    n = 0
    for i in range(len(sn) - 1, -1, -1):
        if ascii_value(sn[i]) >= b:
            return -1
        n += ascii_value(sn[i]) * p
        p *= b
    return n


def chr_value(n):
    if (n >= 0 and n <= 9):
        return chr(n + 48)
    else:
        return chr(n - 10 + 65)


def from_decimal(b, n):
    r = ""
    while n > 0:
        r += chr_value(n % b)
        n //= b
    r = r[::-1]
    return r


def convert(sn, a, b):
    return from_decimal(b, to_decimal(sn, a))


def main():
    numero = input("Número: ")
    base = int(input("Base: "))
    a_base = int(input("A base: "))
    print(convert(numero, base, a_base))


if __name__ == "__main__":
    main()
