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


if __name__ == "__main__":
    assert sueldo("Ejecutivo") == 90
    assert sueldo("Jefe") == 100
    assert sueldo("Externo") == 50
    assert exponenciacion(4) == 64
    assert exponenciacion(3) == 9
    assert es_primo(3) is True
    assert es_primo(5) is True
    assert es_primo(13) is True
    assert es_primo(1) is False
    assert es_primo(10) is False
    assert es_primo(33) is False
