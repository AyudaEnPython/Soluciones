"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

mayor = menor = 0
for _ in range(10):
    edad = int(input("Edad: "))
    if edad >= 18:
        mayor += 1
    else:
        menor += 1

print(f"Porcentaje de mayores de edad: {mayor * 100 / 10}%")
print(f"Porcentaje de menores de edad: {menor * 100 / 10}%")
