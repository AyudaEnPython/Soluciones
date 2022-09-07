"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En una estación de servicio se conoce la cantidad de nafta común y
super vendida en el corriente mes. El usuario deberá ingresar las
ventas totales de cada tipo de nafta por cada día del mes. Al finalizar
debe informar la venta total del mes y el porcentaje vendido de cada
tipo de nafta (en el mes actual).

Nota: Se puede optar por dos alternativas, pedir la cantidad de días
que tiene el mes o solicitar al usuario que indique en cada carga si es
el último día.
"""

comun = 0
super_ = 0

dias = int(input("Ingrese la cantidad de días del mes: "))
for i in range(dias):
    print(f"Día {i+1}")
    comun += int(input("Venta total de nafta comun: "))
    super_ += int(input("Venta total de nafta super: "))

total = comun + super_
porcentaje_comun = round(comun / total * 100, 2)
porcentaje_super = round(super_ / total * 100, 2)

print(f"La venta total del mes es de: {total}")
print(f"El porcentaje de nafta común vendida es de: {porcentaje_comun}")
print(f"El porcentaje de nafta super vendida es de: {porcentaje_super}")
