"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Haciendo uso de estructuras "while" o "for", escribir un programa en
lenguaje Python que muestre los múltiplos de 5. Los números inicial y
final de la serie de números son introducidos por el usuario.
"""

inicio = int(input("Inicio: "))
final = int(input("Final: "))

while inicio <= final:
    if inicio % 5 == 0:
        print(inicio)
    inicio += 1
