"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que solicite al usuario ingresar un número de
decimales y almacénelo en una variable. A continuación, el programa
debe solicitar al usuario que ingrese un número entero y guardarlo en
otra variable. En una tercera variable se deberá guardar el resultado
de la suma de los dos números ingresados por el usuario. Por último, se
debe mostrar en pantalla el texto "El resultado de la suma es [suma]",
donde "[suma]" se reemplazará por el resultado de la operación.
"""

a = float(input("Ingrese un número de decimales: "))
b = int(input("Ingrese un número entero: "))
c = a + b
print(f"El resultado de la suma es {c}")