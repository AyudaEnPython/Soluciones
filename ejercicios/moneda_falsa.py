"""
Desarrollar un programa que contenga las siguientes funciones:

Crear una variable de tipo lista que contenga los pesos de cada una
de las 8 monedas.

cargar_monedas() -> Esta función permitirá al usuario cargar el peso
(float) de cada una de las 8 monedas, controlando que solo sea 1
moneda la que el usuario introduzca con un peso menor. Esta función
agregará los pesos de cada una de las monedas a la variable tipo lista
y los acomodará de manera aleatorio.

imprimir_monedas() -> Esta función imprimirá en pantalla el peso de
cada una de las monedas.

encontrar_moneda_falsa() -> Esta función retornará la posición en la
lista donde se encuentra la moneda falsa. Se deberá simular que la
balanza citada en el ejercicio hecho en clase existe, y que solo se
puede pesar 2 veces sobre esa balanza. La moneda falsa deberá ser
encontrada a través de simular estas mediciones, utilizando solo
sentencias if y elif como herramienta.

El programa deberá de llamar cada una de estas funciones en el flujo
correcto o a través de la implementación de un menú.
"""
from random import uniform, shuffle
# pip install prototools
from prototools import Menu, float_input, textbox

TAMAÑO, PESO, MARGEN = 8, 8.1, 0.8
monedas = []


def _balanza(moneda):
    if PESO - MARGEN <= moneda <= PESO + MARGEN:
        return True
    return False


def cargar_monedas():
    monedas.clear()
    falsa = float_input("Peso: ", min=PESO-MARGEN)
    monedas.append(falsa)
    for _ in range(TAMAÑO - 1):
        monedas.append(round(uniform(PESO-MARGEN, PESO+MARGEN), 1))
    shuffle(monedas)
    textbox("Monedas cargadas")


def imprimir_monedas():
    for n, moneda in enumerate(monedas):
        print(f"Posicion {n}: {moneda} gr.")


def encontrar_moneda_falsa():
    for n, moneda in enumerate(monedas):
        if _balanza(moneda):
            continue
        else:
            textbox(f"Posicion {n}")


if __name__ == "__main__":
    menu = Menu()
    menu.add_options(
        ("Cargar monedas", cargar_monedas),
        ("Ver monedas", imprimir_monedas),
        ("Encontrar moneda falsa", encontrar_moneda_falsa)
    )
    menu.run()
