"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/calculadora/operadores.py


def suma(a: float, b: float) -> float:
    """Suma dos números.

    :param a: Primer número.
    :a type: float
    :param b: Segundo número.
    :b type: float
    :return: La suma de los dos números.
    :rtype: float
    """
    return a + b


def resta(a: float, b: float) -> float:
    """Resta dos números.

    :param a: Primer número.
    :a type: float
    :param b: Segundo número.
    :b type: float
    :return: La resta de los dos números.
    :rtype: float
    """
    return a - b


def multiplicacion(a: float, b: float) -> float:
    """Multiplica dos números.

    :param a: Primer número.
    :a type: float
    :param b: Segundo número.
    :b type: float
    :return: La multiplicación de los dos números.
    :rtype: float
    """
    return a * b


def division(a: float, b: float) -> float:
    """Divide dos números.

    :param a: Primer número.
    :a type: float
    :param b: Segundo número.
    :b type: float
    :raises ZeroDivisionError: Si el segundo número es cero.
    :return: La división de los dos números.
    :rtype: float
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "No se puede dividir entre cero"
