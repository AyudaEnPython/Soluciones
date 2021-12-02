"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que muestre todo lo que el usuario introduzca
hasta que el usuario escriba “salir” que terminará.
"""

while True:
    e = input("> ")
    if e == "salir":
        break
    print(e)
