"""
Escriba un programa para solicitar al usuario Horas y tarifa por hora
utilizando la función de entrada para calcular el salario bruto.

Use 35 horas y una tasa de 2,75 por hora para probar el programa (la
paga debe ser 96.25).

    +-------------+
    | Paga: 96.25 |
    +-------------+

Debes utilizar input () para leer una cadena y float () para convertir
la cadena en un número.
No se preocupe por la comprobación de errores o los datos de usuario
incorrectos.
"""

horas = float(input("Ingresar horas: "))
tarifa = float(input("Ingresar tarifa: "))
print("Paga:", horas * tarifa)