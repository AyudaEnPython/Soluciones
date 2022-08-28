"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que simule un juego de bingo para dos jugadores y
muestre al ganador. Deberá ingresar como entrada los cartones de cada
jugador y luego los números que vayan saliendo en la tómbola.

El ganador será aquel jugador que logre marcar todos los números de su
cartón. Si ocurre un empate deberá indicar que ambos jugadores ganaron.

Observaciones: Los datos de la tómbola que se van ingresando serán
    siempre correctos y no se debe considerar mal uso del programa,
    como por ejemplo ingresar números repetidos de la tómbola. Puede
    usar números aleatorios entre 0 y 99 para generar los intentos de
    la tómbola.

+--------------------------------+   +--------------------------------+
|Carton del jugador 1: 1-12-54-5 |   |Carton del jugador 1: 1-12-54-5 |
|Carton del jugador 2: 3-6-12-2  |   |Carton del jugador 2: 3-6-12-2  |
|Ingrese numero de la tombola: 1 |   |Ingrese numero de la tombola: 1 |
|Ingrese numero de la tombola: 6 |   |Ingrese numero de la tombola: 6 |
|Ingrese numero de la tombola: 4 |   |Ingrese numero de la tombola: 4 |
|Ingrese numero de la tombola: 3 |   |Ingrese numero de la tombola: 3 |
|Ingrese numero de la tombola: 54|   |Ingrese numero de la tombola: 54|
|Ingrese numero de la tombola: 8 |   |Ingrese numero de la tombola: 2 |
|Ingrese numero de la tombola: 5 |   |Ingrese numero de la tombola: 5 |
|Ingrese numero de la tombola: 12|   |Ingrese numero de la tombola: 12|
|El ganador es el jugador 1      |   |Ambos jugadores ganan           |
+--------------------------------+   +--------------------------------+
"""
from random import shuffle, sample
from typing import List, Optional, Tuple

N = 99
BOLILLERO = list(range(1, N+1))
DISPLAY = [0] * 5
MENSAJES = {
    0: "Ambos jugadores ganan",
    1: "El ganador es el jugador 1",
    2: "El ganador es el jugador 2",
}


def obtener_carton(carton: str) -> List[int]:
    return list(map(int, carton.split("-")))


def carton_random(n: int) -> List[int]:
    return sample(list(range(1, N+1)), n)


def tombola(show: Optional[bool] = True) -> int:
    shuffle(BOLILLERO)
    n = BOLILLERO.pop(0)
    DISPLAY.append(n)
    if show:
        print(" - ".join(map("{:02}".format, DISPLAY[-6:])))
    return n


def check(x: int, xs: List[int]) -> None:
    if x in xs:
        xs.remove(x)


def result(a: List[int], b: List[int]) -> Tuple[bool, int]:
    if not a and not b:
        return True, 0
    elif not a:
        return True, 1
    elif not b:
        return True, 2
    return False, -1


def run(a: List[int], b: List[int]) -> None:
    while True:
        n = tombola()
        check(n, a)
        check(n, b)
        end_game, msg = result(a, b)
        if end_game:
            print(MENSAJES[msg])
            break


def main():
    a = obtener_carton(input("Carton del jugador 1: "))  # carton_random(4)
    b = obtener_carton(input("Carton del jugador 2: "))  # carton_random(4)
    run(a, b)


if __name__ == "__main__":
    main()
