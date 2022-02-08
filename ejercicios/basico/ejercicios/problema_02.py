"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que solicite al usuario que ingrese cúantos shows
musicales ha visto en el último año y almacene ese número en una
variable. A continuación, mostrar en pantalla un valor de verdad (True
o False) que indique si el usuario ha visto más de 3 shows.
"""

n = int(input("Shows musicales vistos en el último año: "))
if n > 3:
    print("Ha visto más de 3 shows musicales el último año")
else:
    print("No ha visto más de 3 shows musicales el último año")