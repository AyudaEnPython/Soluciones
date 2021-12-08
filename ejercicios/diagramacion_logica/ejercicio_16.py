"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

hombres = int(input("Cantidad de hombres: "))
mujeres = int(input("Cantidad de mujeres: "))

total = hombres + mujeres
porcentaje_hombres = (hombres * 100) / total
porcentaje_mujeres = (mujeres * 100) / total

print(f"El porcentaje de hombres es {porcentaje_hombres}%")
print(f"El porcentaje de mujeres es {porcentaje_mujeres}%")

