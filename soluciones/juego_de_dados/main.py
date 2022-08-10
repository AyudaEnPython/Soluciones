"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint, shuffle
from typing import Dict, Tuple
# pip install prototools
from prototools import menu_input, text_align, textbox, str_input, compose

Jugadores = Dict[str, Dict[str, int]]


def _son_pares(a: int, b: int) -> bool:
    return a % 2 == 0 and b % 2 == 0


def _son_impares(a: int, b: int) -> bool:
    return a % 2 != 0 and b % 2 != 0


def lanzar() -> Tuple[int, int]:
    return randint(1, 6), randint(1, 6)


def _preguntar(nombre: str) -> int:
    return int(menu_input(
        ("5", "10"),
        prompt=f"¿{nombre}, Cuantos puntos deseas sumar?\n",
        numbers=True,
        lang="es",
    ))


def _azar(jugadores: Jugadores) -> str:
    nombres = list(jugadores.keys())
    shuffle(nombres)
    return nombres


def _negar(jugadores: Jugadores, nombre: str) -> None:
    jugadores_ = list(jugadores.keys())
    jugadores_.remove(nombre)
    while True:
        print("Escojer a quien negarle una de sus rondas opcionales")
        jugador = menu_input(jugadores_, numbers=True, lang="es")
        if jugadores[jugador]["opcionales"] > 0:
            jugadores[jugador]["opcionales"] -= 1
            break
        elif all(jugadores[k]["opcionales"] == 0 for k in jugadores_):
            print("Ningun jugador tiene jugadas opcionales")
            break
        else:
            print("Seleccionar otro jugador")


def _verificar(puntos: int) -> bool:
    return False if puntos >= 50 else True


def ingreasar_jugadores() -> Jugadores:
    jugadores: Jugadores = {}
    while True:
        nombre = str_input("Ingrese un nombre: ")
        if nombre not in jugadores:
            jugadores[nombre] = {"puntos": 0, "opcionales": 3}
            if len(jugadores) == 4:
                break
        else:
            print("Nombre ya existe, elegir otro")
    return jugadores


def ganador(jugadores: Jugadores) -> str:
    _jugadores = [
        jugador for jugador in jugadores
        if _verificar(jugadores[jugador]["puntos"])
    ]
    ganador = max(
        _jugadores,
        key=lambda jugador: jugadores[jugador]["puntos"]
    )
    return ganador


def obligatorio(jugadores: Jugadores) -> Jugadores:
    for n in range(1, 4):
        textbox(f"Ronda N°{n}")
        for nombre in jugadores:
            jugada(jugadores, nombre)
    return jugadores


def jugada(jugadores: Jugadores, nombre: str) -> None:
    text_align(f"Turno de {nombre}")
    x, y = lanzar()
    jugadores[nombre]["puntos"] += x + y
    print(f"Primer dado: {x} | Segundo dado: {y}")
    if _son_pares(x, y):
        jugadores[nombre]["puntos"] += _preguntar(nombre)
    elif _son_impares(x, y):
        _negar(jugadores, nombre)
    mostrar(jugadores)


def opcional(jugadores: Jugadores) -> Jugadores:
    for i, nombre in enumerate(_azar(jugadores)):
        textbox(f"Ronda N°{i + 1}")
        opcionales = jugadores[nombre]["opcionales"]
        if opcionales > 0:
            textbox(f"{nombre} tiene {opcionales} opcionales")
            while opcionales > 0:
                jugada(jugadores, nombre)
                opcionales -= 1
            jugadores[nombre]["opcionales"] = opcionales
    return jugadores


def mostrar(jugadores: Jugadores) -> None:
    for k, v in jugadores.items():
        print(
            f"Jugador {k} -> "
            f"Puntos: {v['puntos']} | Opcionales: {v['opcionales']}"
        )


def main():
    game = compose(
        obligatorio,
        opcional,
    )
    jugadores = game(ingreasar_jugadores())
    text_align("Resultados")
    print(f"Ganador: {ganador(jugadores)}")


if __name__ == "__main__":
    main()
