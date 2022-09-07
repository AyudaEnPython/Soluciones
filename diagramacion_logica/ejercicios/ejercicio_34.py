"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

mayor = 0
suma = 0
for _ in range(10):
    edad = int(input("Ingresar edad: "))
    if edad >= 18:
        mayor += 1
    suma += edad

print(f"Promedio: {suma / 10}")
print(f"Mayores de edad: {mayor}")
