"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

def suma(a: float, b: float) -> float:
    return a + b


def resta(a: float, b: float) -> float:
    return a - b


def multiplicacion(a: float, b: float) -> float:
    return a * b


def division(a: float, b: float) -> float:
    if b <= 0:
        raise ZeroDivisionError
    return a / b