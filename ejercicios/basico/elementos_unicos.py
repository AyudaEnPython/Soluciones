"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba una función de Python que tome un número como parámetro y
verifique que el número sea primo o no.

NOTE: Ambas funciones retornan una lista con elementos unicos.
"""


def elementos_unicos_a(iterable):
    return list(set(iterable))


def elementos_unicos_b(iterable):
    secuencia = []
    for elemento in iterable:
        if elemento not in secuencia:
            secuencia.append(elemento)
    return secuencia
