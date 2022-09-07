"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

n = int(input("Cantidad de personas: "))

h = m = 0
for _ in range(n):
    sexo = input("Ingrese su sexo (H/M): ").lower()
    edad = input("Ingrese su edad: ")
    if sexo == "m" and int(edad) >= 18:
        m += 1
    elif sexo == "h" and int(edad) < 18:
        h += 1

print(f"Mujeres mayores de edad: {m}")
print(f"Hombres menores de edad: {h}")
