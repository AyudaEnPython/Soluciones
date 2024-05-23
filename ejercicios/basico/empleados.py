"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
En una empresa trabajan n empleados cuyos sueldos oscilan entre 500 y 1500.
Realizar un programa que informe de cuántos empleados cobran menos de 1000 y
cuántos más o igual de 1000 informar también del total que gasta la empresa
en pagar a sus empleados suman el valor de 15% del IVA.

NOTE: el enunciado contiene errores ortográficos y debería ser más específico.
"""

IVA = 1.15

total = 0
mas_o_igual_a_1000 = 0
menos_de_1000 = 0

n = int(input("Ingresar número de empleados: "))

for i in range(n):
    sueldo = int(input(f"Empleado N°{i+1} Ingresar sueldo: "))
    if sueldo >= 1000:
        mas_o_igual_a_1000 += 1
    else:
        menos_de_1000 += 1
    total += sueldo

total_con_iva = total * IVA

print(f"N° de empleados que cobran menos de 1000: {menos_de_1000}")
print(f"N° de empleados que cobran más o igual a 1000: {mas_o_igual_a_1000}")
print(f"Total que gasta la empresa: {total}")
print(f"Total que gasta la empresa (IVA incluido): {total_con_iva:.2f}")
