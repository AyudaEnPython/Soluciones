"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

n = int(input("Ingrese un número entero: "))

if n < 0:
    print(f"{n} es negativo")
elif n == 0:
    print(f"{n} es nulo")
else:
    print(f"{n} es positivo")