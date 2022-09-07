"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


# --------------------------------------------------------- Ejercicio 1
def hipotenusa(a: float, b: float) -> float:
    """
    >>> hipotenusa(3.0, 4.0)
    5.0
    >>> hipotenusa(5.0, 12.0)
    13.0
    >>> hipotenusa(8.0, 15.0)
    17.0
    """
    return (a**2 + b**2) ** 0.5


# --------------------------------------------------------- Ejercicio 2
def potencia_int(base: int, exponente: int) -> int:
    """
    >>> potencia_int(3, 4)
    81
    >>> potencia_int(2, 3)
    8
    >>> potencia_int(5, 2)
    25
    """
    result = 1
    for _ in range(exponente):
        result *= base
    return result


# --------------------------------------------------------- Ejercicio 3
def multiplo(a: int, b: int) -> bool:
    """
    >>> multiplo(4, 3)
    0
    >>> multiplo(6, 3)
    1
    >>> multiplo(9, 3)
    1
    """
    if a % b == 0:
        return 1
    return 0


# --------------------------------------------------------- Ejercicio 4
def impar(n: int) -> bool:
    """
    >>> impar(3)
    1
    >>> impar(4)
    0
    >>> impar(5)
    1
    """
    if n % 2 == 0:
        return 0
    return 1


# ----------------------------------------------------- Ejercicio 5 y 6
def cuadrado(lado: int, caracter: str, espacio: bool = True) -> None:
    """
    >>> cuadrado(3, "*")
    * * *
    * * *
    * * *
    >>> cuadrado(4, "#")
    # # # #
    # # # #
    # # # #
    # # # #
    >>> cuadrado(2, "*", False)
    **
    **
    """
    espacio = " " if espacio else ""
    for _ in range(lado):
        print((caracter + espacio)*lado)


# --------------------------------------------------------- Ejercicio 7
def tiempo(hh: int, mm: int, ss: int) -> int:
    """
    >>> tiempo(0, 0, 30)
    30
    >>> tiempo(1, 1, 1)
    3661
    """
    return (hh * 3600) + (mm * 60) + ss


# --------------------------------------------------------- Ejercicio 8
def es_perfecto(n: int) -> bool:
    """
    >>> es_perfecto(6)
    True
    """
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == n:
        return True
    return False


# --------------------------------------------------------------- Tests
if __name__ == "__main__":
    import doctest
    doctest.testmod()
