"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa que efectúe la liquidación de sueldos basado en
los siguientes datos: nombre del empleado, cantidad de días trabajados
(cada día trabajando contempla 8 horas diarias), cantidad de horas
extras (tienen un valor del 50% más con respecto a la hora normal), y
el valor de la hora normal. Imprimir: el nombre del empleado y el neto
a cobrar, considerando que el descuento a realizarse sobre el sueldo
bruto es de 17%.
"""

HORAS = 8

empleado = input("Ingrese el nombre del empleado: ")
dias = int(input("Ingrese la cantidad de días trabajados: "))
extras = int(input("Ingrese la cantidad de horas extras: "))
valor = int(input("Ingrese el valor de la hora normal: "))

neto = (dias * HORAS * valor) + (extras * valor * 1.5)
descuento = neto * 0.17
total = neto - descuento

print("Sueldo neto a cobrar: ", total)