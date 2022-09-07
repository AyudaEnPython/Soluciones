"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un código que solicite:
    - El nombre completo de una persona.
    - Un número entero.

Con dicha información, el programa debe imprimir el primer nombre del
usuario, repetido la cantidad de veces correspondiente al número entero

TODO: add tests
"""


def solucion_a():  # solucion propuesta autocompletada por github copilot
    nombre = input("Ingrese su nombre completo: ")
    numero = int(input("Ingrese un número entero: "))
    print(nombre[0:nombre.find(" ")] * numero)


def solucion_b():
    nombre_completo = input("Ingrese su nombre completo: ")
    repeticiones = int(input("Ingrese un número entero: "))
    primer_nombre, _ = nombre_completo.split(" ")
    for _ in range(repeticiones):
        print(primer_nombre)


def solucion_c():
    nombre_completo = input("Ingrese su nombre completo: ")
    repeticiones = int(input("Ingrese un número entero: "))
    primer_nombre, _ = nombre_completo.split(" ")
    print((primer_nombre + "\n") * repeticiones)


def solucion_d():
    nombre_completo = input("Ingrese su nombre completo: ")
    repeticiones = int(input("Ingrese un número entero: "))
    primer_nombre = nombre_completo.split(" ")[0]
    for _ in range(repeticiones):
        print(primer_nombre)


if __name__ == "__main__":
    solucion_a()
