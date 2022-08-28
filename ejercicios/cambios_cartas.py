"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe una función de nombre gestiona Cambios que, dada una lista de
cartas ma y un número entero cambios, muestre por pantalla el proceso
del cambio y, al final, devuelva la lista resultante. Cambiar tantas
cartas de la mano como el número de cambios dado. Recuerde que no se
permite cambiar más de 4 cartas una vez. Esto, unos ejemplos de uso de
la función podrían ser:

gestionaCambios(
    [
        ["5", "corazones"],
        ["5", "trebols"],
        ["3", "picas"],
        ["K", "diamantes"],
        ["5", "picas"],
    ],
    2
)

Escribe la 1 carta a cambiar: ["10", "trabajos"]
Lo siento, no tienes esa carta.

Escribe la 1 carta a cambiar: ["3", "picas"]

Escribe la 2 carta a cambiar: ["K", "diamantes"]
[
    ["5", "corazones"],
    ["5", "trabajos"],
    ["As", "picas"],
    ["5", "diamantes"],
    ["5", "picas"],
]

NOTE: La función propuesta esta mal diseñada, tambien los ejemplos
    dados producen resultados incorrectos.
"""
from random import sample
from typing import Dict, List, Tuple

N: int = 1
Mazo = List[List[str]]
_msg: Dict[int, str] = {0: "primera", 1: "segunda", 2: "tercera"}
TIPO: Tuple[str] = ("corazones", "treboles", "picas", "diamantes")
VALID_N: List[str] = list(map(str, range(1, 11))) + list("JQKA")


def _random_card() -> List[str]:
    return list((sample(VALID_N, 1)[0], sample(TIPO, 1)[0]))


def cambiar_carta(mazo: Mazo, cambios: Mazo) -> Mazo:
    t = [carta for carta in mazo]
    for carta in cambios:
        t.remove(carta)
    i = 0
    while i < len(cambios):
        carta = _random_card()
        if carta not in t:
            t.append(carta)
        i += 1
    return t


def pedir_cartas(mazo: Mazo, _n: int) -> Mazo:
    cartas = []
    i = 0
    while _n > 0:
        carta = input(f"Escribe la {_msg[i]} carta a cambiar: ").split(",")
        if carta not in mazo:
            print(carta)
            print("Lo siento, no tienes esa carta.")
            continue
        else:
            cartas.append(carta)
            _n -= 1
            i += 1
    return cartas


def main():
    mazo = [
        ["5", "corazones"],
        ["5", "treboles"],
        ["3", "picas"],
        ["K", "diamantes"],
        ["5", "picas"],
    ]
    n = input("Escribe el número de cambios: ")
    try:
        if int(n) > 4:
            raise ValueError("No se pueden cambiar más de 4 cartas una vez")
    except ValueError as e:
        print(e)
        return
    cartas = pedir_cartas(mazo, int(n))
    mazo = cambiar_carta(mazo, cartas)
    print(mazo)


if __name__ == "__main__":
    main()
