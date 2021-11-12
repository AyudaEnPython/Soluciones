"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ REDACCION ORIGINAL ------------------------
1. Crear un programa que pida un número entero e imprimirlo, si no se
ingresa deberá preguntar otra vez por el número entero hasta que
ingrese un número positivo.

2. Crear una lista que almacene edades.

3. Con la lista anterior, contar cuantos son mayores de edad.

# --------------------------------------------------------------------
NOTA: Los ejercicios estan mal redactados, el instructor deberia tener
    mas claridad e integrar lo enseñado con ejercicios bien diseñados.
"""

def ingresar_numero():
    while True:
        n = input("Ingrese un número entero: ")
        try:
            n = int(n)
            if n >= 0:
                return n
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("No es un número entero.")

print(ingresar_numero()) # 1 

edades = [18, 13, 11, 19, 17, 15, 16, 14, 12, 10, 20] # 2

print(f"Mayores de edad: {len([e for e in edades if e >= 18])} personas") # 3