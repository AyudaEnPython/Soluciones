"""
Escriba un programa para avisar al usuario por horas y tasa por hora
utilizando "input" para calcular el salario bruto. El pago debe ser
la tarifa normal por horas hasta 40 y 1.5 veces la tarifa por hora
para todas las horas trabajadas por encima de las 40 horas. Ponga la
lógica para hacer el cálculo de la paga en una función llamada
"computepay()" y use la función para hacer el cálculo. La función debe
devolver un valor.

Use 45 horas y una tasa de 10.50 por hora para probar el programa (la
paga debe ser 498.75).

    Salida deseada
    +------------+
    | 498.75     |
    +------------+

Debes utilizar "input" para leer una cadena y "float" para convertir la
cadena en un número. No se preocupe por la comprobación de errores en
la entrada de usuario a menos que desee: Usted puede asumir que el
usuario escribe los números correctamente. No nombre su variable "sum"
o use la función "sum()".
"""


def computepay(horas, tasa):
    if horas <= 40:
        return horas * tasa
    else:
        return 40 * tasa + ((horas - 40) * tasa * 1.5)


horas = float(input("Horas: "))
tasa = float(input("Tasa: "))

print(computepay(horas, tasa))
