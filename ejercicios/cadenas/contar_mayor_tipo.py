"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que permita una frase y muestre si tiene más
vocales o más consonantes.

Ejemplo
-------
De la frase: "mi perro se encuentra contemplando el cielo" el
resultado mostrado sería:
la frase cuenta con más consonantes que vocales.
"""

ss = input("Ingresar frase: ").lower()
v = sum(1 for s in ss if s in "aeiouáéíóú")
c = sum(1 for s in ss if s.isalpha() and s not in "aeiouáéíóú")
print("No ingresaste una frase" if not ss else
    "La frase cuenta con {}".format(
    "la misma cantidad de vocales y consonantes" if v == c else
    "más vocales que consonantes" if v > c else 
    "más consonantes que vocales" 
))
