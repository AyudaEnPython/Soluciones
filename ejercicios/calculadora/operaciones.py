"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b <= 0:
        raise ZeroDivisionError
    return a / b
