"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

# del ejercicio 21 y 22
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

print(sum([int(s) for s in str(n)]))