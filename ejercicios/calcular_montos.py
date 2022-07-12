"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. En un estacionamiento cobran $15.00 por hora o fracción. Diseñe un
    programa que determine cuánto debe pagar un cliente por el
    estacionamiento de su vehículo, conociendo el tiempo de
    estacionamiento en horas y minutos.

2. Un supermercado ha puesto en oferta la venta al por mayor de cierto
    producto, ofreciendo un descuento del 15% por la compra de más de 3
    docenas y 10% en caso contrario. Además, por la compra de más de 3
    docenas se obsequia una unidad del producto por cada docena en
    exceso sobre 3. Diseñe un algoritmo que determine el monto de la
    compra, el monto del descuento, el monto a pagar y el número de
    unidades de obsequio por la compra de cierta cantidad de docenas
    del producto.

3.Que calcule el sueldo que le corresponde al trabajador de una empresa
    que cobra 40.000 euros anuales, el programa debe realizar los
    cálculos en función de los siguientes criterios:
    a. Si lleva más de 10 años en la empresa se le aplica un aumento
        del 10%.
    b. Si lleva menos de 10 años, pero más que 5 se le aplica un
        aumento del 7%.
    c. Si lleva menos de 5 años, pero más que 3 se le aplica un aumento
        del 5%.
    d. Si lleva menos de 3 años se le aplica un aumento del 3%.
"""

# Ejercicio 1 =========================================================
horas = int(input("Ingresar horas: "))
minutos = int(input("Ingresar minutos: "))
horas = horas + 1 if minutos > 0 else horas
print(f"El monto a pagar es: {horas * 15}")

# Ejercicio 2 =========================================================
docenas = int(input("Cantidad de productos en docenas: "))
precio = float(input("Precio del producto en docenas: "))
monto = docenas * precio
descuento = monto * 0.15 if docenas > 3 else monto * 0.10
obsequio = docenas - 3 if docenas > 3 else 0
total = monto - descuento
print(f"Productos comprados: {docenas*12}")
print(f"Monto de la compra: {monto}")
print(f"Descuento: {descuento}")
print(f"Total a pagar: {total}")
print(f"Cantidad de obsequios: {obsequio}")

# Ejercicio 3 =========================================================
antiguedad = int(input("Ingresar antiguedad en años: "))
sueldo = 40000
if antiguedad > 10:
    sueldo = sueldo * 1.1
elif antiguedad > 5:
    sueldo = sueldo * 1.07
elif antiguedad > 3:
    sueldo = sueldo * 1.05
else:
    sueldo = sueldo * 1.03
print(f"Sueldo: {sueldo}")
