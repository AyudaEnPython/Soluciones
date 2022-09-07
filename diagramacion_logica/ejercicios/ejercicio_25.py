"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# del ejercicio 21
while True:
    try:
        n = input("Ingrese un número: ")
        if len(n) != 5:
            print("El número debe tener 5 dígitos")
            continue
        else:
            n = int(n)
            break
    except ValueError:
        print("Error: debe ingresar un número entero")
        continue

k = n 
x = 0
while k != 0:
    x = 10*x + k%10
    k //= 10

if x == n:
    print("El número es capicua")
else:
    print("El número no es capicua")
