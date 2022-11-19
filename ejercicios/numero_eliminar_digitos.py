"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una función que reciba como parámetro un número entero positivo
de seis cifras y retorne un nuevo número sin la tercera y cuarta
cifras. Si el número recibido no es un número entero positivo de 6
cifras, la función debe retornar un mensaje indicando el error.

Ejemplo:

    +---------+------------------+
    | Entrada |      Salida      |
    +---------+------------------+
    |  123456 | 1246             |
    |  987654 | 9854             |
    |  123    | Número no válido |
    | -234561 | Número no válido |
    +---------+------------------+

"""


def f(n):
    return (n // 10000) * 100 + n % 100


def validar(n):
    if len(str(n)) != 6 or n < 0:
        raise ValueError("Número no válido")
    return n


def modificar(n):
    try:
        return f(validar(n))
    except ValueError as e:
        return e


if __name__ == "__main__":
    for n in (123456, 987654, 123, -234561):
        print(modificar(n))
