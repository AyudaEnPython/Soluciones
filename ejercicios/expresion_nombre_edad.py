"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
A partir de 2 variables NOMBRE y EDAD crear una variable que se llame
EXPRESION que cumpla con todas las siguientes condiciones:
1.- Que NOMBRE sea diferente de cuatro asteriscos
2.- Que EDAD sea mayor que 10 y menor que 18
3.- Que la longuitud del NOMBRE sea mayor o igual a 3 pero también
    menor que 10
Utilizar paréntesis y que NOMBRE y EDAD sean leídos no asignados.

# ---------------------------------------------------------------------
NOTE: El enunciado original no es claro.
"""

while True:
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    if nombre != "****":
        if 10 < edad < 18:
            if 3 <= len(nombre) < 10:
                expresion = f"Su nombre es {nombre} y su edad es {edad}"
                break
            else:
                print("Su nombre debe tener entre 3 y 10 caracteres")
        else:
            print("Su edad no es válida")
    else:
        print("Su nombre debe ser diferente de cuatro asteriscos")

print(expresion)
