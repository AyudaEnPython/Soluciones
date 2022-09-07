"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

mayor = menor = 0

n = int(input("Ingrese cantidad de personas: "))

for _ in range(n):
    edad = int(input("Ingrese edad: "))
    if edad >= 18:
        mayor += 1
    else:
        menor += 1

print(f"Mayores de edad: {mayor}")
print(f"Menores de edad: {menor}")
