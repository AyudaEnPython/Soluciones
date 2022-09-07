"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

n = int(input("Cantidad de personas: "))

h = m = 0
for _ in range(n):
    sexo = input("Ingrese su sexo (H/M): ").lower()
    if sexo == "h":
        h += 1
    else:
        m += 1

print(f"Hombres: {h}")
print(f"Mujeres: {m}")
print(f"Porcentaje de hombres: {h/n*100:.2f}%")
print(f"Porcentaje de mujeres: {m/n*100:.2f}%")
