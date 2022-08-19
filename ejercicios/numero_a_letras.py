"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un código Python necesario para que permita ingresar un número
entero (entre 0 y 100, ambos incluidos) y me muestre por pantalla el
número ingresado en letras.

Por ejemplo:
- Ingresa: 48 -> Muestra: Cuarenta y ocho
- Ingresa: 19 -> Muestra: Diecinueve
"""
from typing import Dict
# pip install prototools
from prototools import int_input

T: Dict[int, str] = {
    0: "cero", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco",
    6: "seis", 7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once",
    12: "doce", 13: "trece", 14: "catorce", 15: "quince", 16: "dieci",
    20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta",
    60: "sesenta", 70: "setenta", 80: "ochenta", 90: "noventa", 100: "cien",
}
T_: Dict[int, str] = {2: "dós", 3: "trés", 6: "séis"}


def numero_a_letras(n: int) -> str:
    """Retorna la representación en letras del número.

    :param n: Número entero entre 0 y 100.
    :type n: int
    :return: Representación en letras del número.
    :rtype: str

    >>> numero_a_letras(5)
    'cinco'
    >>> numero_a_letras(16)
    'dieciséis'
    >>> numero_a_letras(19)
    'diecinueve'
    >>> numero_a_letras(20)
    'veinte'
    >>> numero_a_letras(22)
    'veintidós'
    >>> numero_a_letras(23)
    'veintitrés'
    >>> numero_a_letras(26)
    'veintiséis'
    >>> numero_a_letras(30)
    'treinta'
    >>> numero_a_letras(42)
    'cuarenta y dos'
    >>> numero_a_letras(100)
    'cien'
    """
    u = n % 10
    if 0 <= n <= 15 or u == 0:
        return T[n]
    elif 15 < n < 20:
        return f"{T[16]}{T[u] if u != 6 else T_[6]}"
    elif n < 30:
        return f"{T[20][:-1]}i{T[u] if u not in (2, 3, 6) else T_[u]}"
    elif 30 < n < 100:
        return f"{T[n - u]} y {T[u]}"


def main():
    n = int_input("Ingrese un número entero: ", lang="es", min=0, max=100)
    print(numero_a_letras(n).capitalize())


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main() # comment this line and uncomment the previous to run tests
