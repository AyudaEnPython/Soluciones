"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una función que reciba un número entero y retorne la suma de
sus cifras. Ejemplo:

    +---------+--------+
    | Entrada | Salida |
    +---------+--------+
    |  123456 | 21     |
    | -123    | 6      |
    |  987123 | 30     |
    | -4      | 4      |
    +---------+--------+

"""


def f(n):
    return sum(int(x) for x in str(abs(n)))


if __name__ == "__main__":
    for n in (123456, -123, 987123, -4):
        print(f(n))
