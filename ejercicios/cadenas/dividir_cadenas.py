"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Divida una cadena de caracteres en bloques de tamaño 4, por ejemplo la cadena:
'intente analizar mas profundamente los mensajes recibidos'

Resultaría en:
inte
nte
anal
izar
mas
pro
fund
amen
te l
os m
ensa
jes
reci
bido
ssss

Nota: Si el bloque final está incompleto, complételo repitiendo el último caracter

Luego vuevla a imprimir pero esta vez separados por un *:
Inte*nte *anal*izar*mas*pro*fund*amen*te l*os m*ensa*jes *reci*bido*ssss
"""
from typing import List


def dividir(cadena: str, size: int) -> List[str]:
    """Divide una cadena de caracteres en bloques de tamaño size.

    :param cadena: cadena de caracteres
    :cadena type: str
    :param size: tamaño de bloque
    :size type: int
    :return: lista de cadenas de texto
    :rtype: List[str]
    """ 
    r = [cadena[i:i + size] for i in range(0, len(cadena), size)]
    if len(r[-1]) < size:
        r[-1] += cadena[-1] * (size - len(r[-1]))
    return r


def main():
    s = "intente analizar mas profundamente los mensajes recibidos"
    r = dividir(s, 4)
    print("\n".join(r))
    print("*".join(r))


if __name__ == '__main__':
    main()
