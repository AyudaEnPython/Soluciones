"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def ingresar_numero(indicacion: str):
    """Pide un número al usuario y lo devuelve.

    :param indicacion: Indicación a mostrar al usuario.
    :indicacion: str
    :return: número ingresado por el usuario.
    """
    while True:
        try:
            numero = input(indicacion)
            return float(numero)
        except ValueError:
            print(f"{numero} es un tipo de dato no válido.")
