"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

suma = 0

for _ in range(5):
    peso = float(input("Ingresar peso: "))
    suma += peso

print(f"El peso promedio es: {suma / 5}")