"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

n = int(input("Ingrese un número: "))

k = n 
x = 0
while k != 0:
    x = 10*x + k%10
    k //= 10

if x == n:
    print("El número es capicua")
else:
    print("El número no es capicua")