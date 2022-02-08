"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que le solicite al usuario su edad y la guarde en
una variable. Que luego solicite la cantidad de artículos que comprados
en una tienda y la guarde en otra variable.
FInalmente, mostrar en pantalla un valor de verdad (True o False) que
indique si el usuario es mayor de 18 años y además compró más de 1
artículo.
"""

edad = int(input("Edad: "))
articulos = int(input("Articulos: "))

if edad > 18 and articulos > 1:
    print("Es mayor de 18 y compró más de 1 artículo.")
else:
    print("No es mayor de 18 o no compró más de 1 artículo.")
