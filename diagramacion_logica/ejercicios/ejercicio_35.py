"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

suma = 0
# si son 100 personas, se cambia 10 por 100 (dentro de range)
for _ in range(10):
    peso = float(input("Ingresar peso: "))
    suma += peso

print(f"Peso acumulado {suma}")
