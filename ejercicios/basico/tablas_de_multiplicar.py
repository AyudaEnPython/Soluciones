"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingrese por teclado el número de la tabla a multiplicar, mostrar dicha
tabla de 1 al 15 en el siguiente formato:

Ejemplo:
    INGRESE TABLA = 10
    
    10 * 1 = 10
    10 * 2 = 20
    10 * 3 = 30
        .
        .
        .
    10 * 15 = 150
"""

tabla = int(input("Ingresar la tabla: "))
for n in range(1, 16):
    print(f"{tabla} * {n} = {tabla * n}")
