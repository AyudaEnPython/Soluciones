"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint

while True:
    print(randint(1, 100)*5)
    opcion = input(
        "Ingrese 's' para salir, para continuar presione cualquier tecla: "
    )
    if opcion == 's':
        break
