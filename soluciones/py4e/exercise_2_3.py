"""
Escriba un programa para solicitar al usuario las horas y la tarifa por
hora utilizando la entrada para calcular el salario bruto. Utilice 35
horas y una tarifa de 2,75 por hora para probar el programa (el pago
debe ser 96,25). Debe usar input para leer una cadena y float () para
convertir la cadena en un número. No se preocupe por la verificación de
errores o datos de usuario incorrectos.
"""

horas = float(input("Ingresar horas: "))
tarifa = float(input("Ingresar tarifa: "))
print("Pago: ", horas * tarifa)