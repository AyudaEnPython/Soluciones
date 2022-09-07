"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingrese por teclado un número. Si éste número es 50 entonces ingresará
otro número, luego mostrará la suma de dichos números, sólo si la
condición se cumple.

Ejemplo:

    Ingrese un número: 50
    Ingrese otro número: 30
    Suma = 80
"""

x = int(input("Ingrese un número: "))
if x == 50:
    y = int(input("Ingrese otro número: "))
    print(f"Suma = {x + y}")
