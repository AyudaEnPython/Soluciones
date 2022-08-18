"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


# Pregunta 1
def sueldo(cargo):
    if cargo == "Ejecutivo":
        return 90
    elif cargo == "Jefe":
        return 100
    elif cargo == "Externo":
        return 50


# Pregunta 2
def exponenciacion(numero):
    if numero % 2 == 0:
        return numero ** 3
    else:
        return numero ** 2


# Pregunta 3
def es_primo(numero):
    primo = True
    if numero == 2 or numero == 3:
        primo = True
    elif numero % 2 == 0 or numero < 2:
        primo = False
    else:
        for i in range(3, int(numero**0.5)+1, 2):
            if numero % i == 0:
                primo = False
    return primo
