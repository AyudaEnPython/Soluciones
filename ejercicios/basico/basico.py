"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# 6. Cálculo del salario del trabajador. A un trabajador se le paga de
# acuerdo a su salario por hora hasta 40 horas. Y por cada hora extra
# trabajada, se le incrementa solo el 50% del salario por hora.
# Escriba un programa que calcule el pago a un trabajador. El programa
# le pide al usuario que ingrese el número de horas y el salario por
# hora. El programa debe mostrar el salario total.
#
# Ejemplo de entrada:
# Ingrese el número de horas trabajadas: 41
# Ingrese el salario por hora en Bs: 30
#
# Ejemplo de salida:
# El salario del trabajadro es Bs 1245.00
horas = float(input("Ingrese el número de horas trabajadas: "))
salario = float(input("Ingrese el salario por hora en Bs: "))
if horas >= 40:
    salario_total = salario * 40 + (horas - 40) * salario * 1.5
else:
    salario_total = salario * horas
print(f"El salario del trabajadro es Bs {salario_total:.2f}")


# 7. Número de pulsasiones. Calcule el número de pulsaciones que debe
# tener una persona por cada 10 segundos de ejercicio aeróbico, la fórmula
# que se aplica es la siguiente:
# Si el sexo es femenino:
# número de pulsaciones = (220 - edad) / 10
# Si el sexo es masculino:
# número de pulsaciones = (210 - edad) / 10
#
# Ejemplo de entrada:
# Ingrese el sexo (1 para femenino y 2 para masculino): 1
# Ingrese la edad: 18
#
# Ejemplo de salida:
# Usted debería tener 20.2 pulsaciones por cada 10 seg.
sexo = int(input("Ingrese el sexo (1 para femenino y 2 para masculino): "))
edad = int(input("Ingrese la edad: "))
if sexo == 1:
    pulsaciones = (220 - edad) / 10
elif sexo == 2:
    pulsaciones = (210 - edad) / 10
print(f"Usted debería tener {pulsaciones:.1f} pulsaciones por cada 10 seg.")


# 8. Descuento de ventas. Una frutería ofrece manzanas con descuento según la
# siguiente tabla:
#
#    +------------+-----------+
#    |    Kilos   | Descuento |
#    +------------+-----------+
#    | 0 - 2      |      0%   |
#    | 2.01 - 5   |     10%   |
#    | 5.01 -10   |     20%   |
#    | Mayor a 10 |     30%   |
#    +------------+-----------+
#
# Determine la cantidad a cancelar por parte de una persona que compre
# manzanas en esa frutería.
#
# Ejemplo de entrada:
# Ingrese el precio por kilo (Bs): 10
# Ingrese la cantidad de kilos: 13
#
# Ejemplo de salida:
# Precio a cancelar Bs. 91
precio = float(input("Ingrese el precio por kilo (Bs): "))
cantidad = float(input("Ingrese la cantidad de kilos: "))
if cantidad <= 2:
    descuento = 0
elif 2 < cantidad <= 5:
    descuento = 0.1
elif 5 < cantidad <= 10:
    descuento = 0.2
else:
    descuento = 0.3
precio_total = precio * cantidad * (1 - descuento)
print(f"Precio a cancelar Bs. {precio_total:.1f}")
