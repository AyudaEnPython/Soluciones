"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint

MIN, MAX, intentos = 1, 100, 0
NUMERO_ALEATORIO = randint(MIN, MAX)
FLECHA = u"\u25ba\u25ba" + " "
mensaje = "Sorry {}, ese no es pero estas a una distancia {}"

print("Hola! ¿Cuál es tu nombre? ")
jugador = input(FLECHA)
print(f"Bien, estoy pensando en un número entre el {MIN} y el {MAX}")

while True:
    print(f"¡Adivina! {intentos + 1}° intento")
    numero_ingresado = int(input(FLECHA))
    intentos += 1
    if numero_ingresado == 0:
        print(
            f"No lo lograste a pesar de tratar {intentos} veces. "
            "Mas suerte para otra vez"
        )
        break
    if numero_ingresado == NUMERO_ALEATORIO:
        print(f"Felicitaciones {jugador}, lo lograste en {intentos} intentos")
        break
    elif NUMERO_ALEATORIO - 5 < numero_ingresado < NUMERO_ALEATORIO + 5:
        print(mensaje.format(jugador, "menor a 5"))
    elif NUMERO_ALEATORIO - 10 < numero_ingresado < NUMERO_ALEATORIO + 10:
        print(mensaje.format(jugador, "mayor que 5 y menor que 10"))
    elif NUMERO_ALEATORIO - 20 < numero_ingresado < NUMERO_ALEATORIO + 20:
        print(mensaje.format(jugador, "mayor que 10 y menor que 20"))
    else:
        print(mensaje.format(jugador, "mayor que 20"))
