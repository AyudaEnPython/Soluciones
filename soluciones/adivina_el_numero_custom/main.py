"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import Dict
# pip install prototools
from prototools import int_input

MIN, MAX = 0, 20
MENSAJES : Dict[str, str] = {
    "end": "¡LO LOGRASTE! Usaste {} intentos",
    "low": "¡Ups! Estás por debajo",
    "high": "¡Ups! Te pasaste",
    "out": "¡Te saliste del intervalo!",
}


def main():
    n = int_input("Número de participantes: ")
    participantes = [0] * n
    for i in range(n):
        NUMERO_ALEATORIO = randint(MIN, MAX)
        intentos = 1
        while True:
            numero_ingresado = int_input("Ingresa un número: ")
            if numero_ingresado == NUMERO_ALEATORIO:
                print(MENSAJES["end"].format(intentos))
                participantes[i] = intentos
                break
            elif numero_ingresado < MIN or numero_ingresado > MAX:
                print(MENSAJES["out"])
            elif numero_ingresado < NUMERO_ALEATORIO:
                print(MENSAJES["low"])
            else:
                print(MENSAJES["high"])
            intentos += 1
    print("\n\n")
    ganador = participantes.index(min(participantes)) + 1
    print(f"El ganador es el participante {ganador}")


if __name__ == "__main__":
    main()
