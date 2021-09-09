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
from prototools.entradas import entrada_float
from prototools.menu import EzMenu
from prototools.utils import caja

PESO, MARGEN = 8.1, 0.8
monedas = []

def _balanza(moneda):
    if PESO-MARGEN <= moneda <= PESO+MARGEN:
        return True
    return False

def cargar_monedas():
    monedas.clear()
    falsa = entrada_float("Peso: ", menor=7.3)
    monedas.append(falsa)
    for _ in range(7):
        monedas.append(round(uniform(PESO-MARGEN, PESO+MARGEN), 1))
    shuffle(monedas)
    print("Monedas cargadas")

def imprimir_monedas():
    for n, moneda in enumerate(monedas):
        print(f"Posicion {n}: {moneda} gr.")

@caja
def encontrar_moneda_falsa():
    for n, moneda in enumerate(monedas):
        if _balanza(moneda):
            continue
        else:
            return f"Posicion {n}"


if __name__ == "__main__":
    menu = EzMenu()
    menu.titulo("Monedas")
    menu.agregar_opciones(
        "cargar monedas",
        "ver monedas",
        "encontrar moneda falsa",
        "salir"
    )
    menu.agregar_funciones(
        cargar_monedas,
        imprimir_monedas,
        encontrar_moneda_falsa,
    )
    menu.run()