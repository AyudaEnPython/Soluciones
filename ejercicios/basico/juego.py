"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Enunciado Original:
Programar un juego en PYTHON en el que jueguen dos jugadores intentado adivinar
un número (el programa debe tener un número secreto constante). Se pueden hacer
tantos intentos como se quiera. Al finalizar los intentos ganará el jugador que
más puntos haya logrado. En cada ronda del juego adivinará cada jugador y se
llevará el punto el que más cerca del número secreto haya estado. Si alguno de
los jugadores acierta el número gana y se da por finalizado el juego. Si ambos
jugadores aciertan en la misma ronda empatan. Si al finalizar las rondas ambos
jugadores consiguieron la misma cantidad de puntos es un empate. Es importante
que el juego vaya interactuando con los resultados parciales y finales para que
los jugadores se guíen.

Ejs:
Adivinan (S/N): S
Jugador 1: 333
Jugador 2: 514
Más cerca el jugador 1
Adivinan (S/N): S
Jugador 1: 350
Jugador 2: 400
Más cerca el jugador 1
Adivinan (S/N): S
Jugador 1: 350
Jugador 2: 299
Más cerca el jugador 2
Adivinan (S/N): S
Jugador 1: 200
Jugador 2: 280
Más cerca el jugador 2
Adivinan (S/N): S
Jugador 1: 250
Jugador 2: 260
Más cerca el jugador 2
Adivinan (S/N): S
Jugador 1: 256
Jugador 2: 259
Más cerca el jugador 2
Adivinan (S/N): S
Jugador 1: 258
Jugador 2: 258
Empate!!
>>>

NOTA: "... se llevará el punto el que más cerca del número secreto haya estado."
No se ve reflejado en el ejemplo.
"""
from random import randint

NUMERO = randint(10, 1000)
puntos_1 = 0
puntos_2 = 0

while True:
    continuar = input("Adivinan (S/N): ").lower()
    if continuar in "no":
        break
    jugador_1 = int(input("Jugador 1: "))
    jugador_2 = int(input("Jugador 2: "))
    jugador_1 = abs(NUMERO - jugador_1)
    jugador_2 = abs(NUMERO - jugador_2)
    min_ = min(jugador_1, jugador_2)
    if jugador_1 == 0 or jugador_2 == 0:
        if jugador_1 == 0 and jugador_2 == 0:
            print("Empate!")
        elif jugador_1 == 0: 
            print("Gana el jugador 1!")
        else: 
            print("Gana el jugador 2!")
        break
    if min_ == jugador_1:
        jugador = "Jugador 1"
        puntos_1 += 1
    else:
        jugador = "Jugador 2"
        puntos_2 += 1
    print(f"Más cerca el jugador {jugador}")
print(f"Puntos del jugador 1: {puntos_1}")
print(f"Puntos del jugador 2: {puntos_2}")
