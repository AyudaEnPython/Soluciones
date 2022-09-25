"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
# pip install prototools
from prototools import int_input, text_align, textbox
from prototools.colorize import cyan, yellow, magenta, red

LIMITE, MIN, MAX, intentos = 5, 1, 10, 0
NUMERO_ALEATORIO = randint(MIN, MAX)

textbox(
    cyan("ADIVINA EL NUMERO"),
    align="center", light=False, bcolor="magenta", style="double"
)
print(cyan("Hola! Cuál es tu nombre?"))
usuario = input(yellow(u"\u25ba\u25ba" + " "))
print(cyan(f"Bien, estoy pensando en un número entre el {MIN} y el {MAX}"))
print(cyan(f"Tienes {LIMITE} intentos!"))

while intentos < LIMITE:
    text_align(magenta(f"¡Adivina! {intentos + 1}° intento"))
    numero_ingresado = int_input(
        yellow(u"\u25ba\u25ba" + " "), min=MIN, max=MAX, lang="es",
    )
    intentos += 1
    if numero_ingresado == NUMERO_ALEATORIO:
        print(magenta(f"¡Felicidades {usuario}! ¡Has ganado!"))
        print(magenta(f"¡Adivinaste el número en {intentos} intentos!"))
        break
    elif numero_ingresado > NUMERO_ALEATORIO:
        text_align(yellow("El número es mayor al que estoy pensando"))
    else:
        text_align(yellow("El número es menor al que estoy pensando"))
else:
    print(red(f"¡Lo siento, {usuario}! ¡Has perdido!"))
    print(red(f"El número que pensé era {NUMERO_ALEATORIO}"))
