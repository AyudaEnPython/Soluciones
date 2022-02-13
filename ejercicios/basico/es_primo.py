"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una función de Python que tome un número como parámetro y
verifique que el número sea primo o no.

NOTE: Mas implementaciones en:
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
"""


def es_primo(numero):
    if numero == 2 or numero == 3:
        return True
    elif numero % 2 == 0 or numero < 2:
        return False
    else:
        for i in range(3, int(numero**0.5)+1, 2):
            if numero % i == 0:
                return False
    return True
