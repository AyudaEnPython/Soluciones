"""
Escriba un programa para pedirle al usuario las horas y la tarifa por
hora usando la entrada para calcular el salario bruto. Paga la tarifa
por hora por las horas hasta 40 y 1.5 veces la tarifa por hora para
todas las horas que se trabajaron por encima de las 40 horas.

Use 45 horas y una tasa de 10.50 por hora para probar el programa (la
paga debe ser 498.75).

    +--------+
    | 498.75 |
    +--------+

Debes utilizar "input" para leer una cadena y "float" para convertir la
cadena en un número.
No se preocupe por la comprobación de errores en la entrada del
usuario: suponga que el usuario escribe los números correctamente.
"""

horas = float(input("Horas: "))
tasa = float(input("Tasa: "))

if horas <= 40:
    total = horas * tasa
else:
    total = 40 * tasa + ((horas - 40) * tasa * 1.5)
print(total)