"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# del ejercicio 21
while True:
    try:
        n = input("Ingrese un número: ")
        if len(n) > 4:
            print("El máximo permitidio es un número de 4 dígitos")
            continue
        else:
            n = int(n)
            break
    except ValueError:
        print("Error: debe ingresar un número entero")
        continue

m = n // 1000
d = n % 1000 // 100
c = n % 100 // 10
u = n % 10
print(f"d1 = {m}, d2 = {d}, d3 = {c}, d4 = {u}")