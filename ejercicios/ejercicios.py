"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Escribe un programa que solicité al usuario ingresar cuatro números
para luego mostrar el promedio de los tres.

2. Tres personas deciden invertir su dinero para fundar una empresa.
    Cada una de ellas invierte una cantidad distinta. Obtener el
    porcentaje que cada uno invierte con respecto a la cantidad total
    invertida.

3. Calcular el sueldo de un empleado, ingrese los siguientes datos:
    nombre, horas de trabajo y el salario por hora. Luego incrementar
    el sueldo en 15%.

4. Ingresar 2 números y luego escoger la operación que se quiere hacer
    con ellos (suma, resta, multiplicación, división) y reportar el
    resultado.

5. Diseñe un algoritmo que lea tres números y determine el número mayor.

6. Diseñe un algoritmo que determine si un número es par o impar.

7. Elabore un algoritmo que permita calcular el área de un triángulo.
    area = (base * altura) / 2

8. Diseñe un algoritmo que verifique si la cantidad de digitos
    ingresados de un DNI es correcta o no (el DNI tiene 8 dígitos).

9. Una tienda de música ha puesto a la venta DVD de diversos géneros
    con los precios que se describe en la siguiente tabla:

    +------------+-----------------+
    | Marca      | Precio Unitario |
    +------------+-----------------+
    | 1 Salsa    |      S/.  56.00 |
    | 2 Rock     |      S/.  63.00 |
    | 3 Pop      |      S/.  87.00 |
    | 4 Folclore |      S/. 120.50 |
    +------------+-----------------+

    Como oferta la tienda ofrece un porcentaje de descuento sobre al
    importe de la compra en base a la cantidad de discos adquiridos de
    acuerdo con la siguiente tabla:

NOTE: Ejercicio 9 esta incompleto, falta la tabla de descuentos.
"""

# ---------------------------------------------------------------- Ejercicio 1
x = int(input("Ingrese un número: "))
y = int(input("Ingrese un número: "))
z = int(input("Ingrese un número: "))
print(f"El promedio de los tres números es: {(x + y + z) / 3}")

# ---------------------------------------------------------------- Ejercicio 2
x = int(input("Ingresar inversión: "))
y = int(input("Ingresar inversión: "))
z = int(input("Ingresar inversión: "))
print(f"Porcentaje invertido del primero: {x / (x + y + z) * 100}")
print(f"Porcentaje invertido del segundo: {y / (x + y + z) * 100}")
print(f"Porcentaje invertido del tercero: {z / (x + y + z) * 100}")

# ---------------------------------------------------------------- Ejercicio 3
nombre = input("Ingrese su nombre: ")
horas = int(input("Ingrese las horas trabajadas: "))
salario = int(input("Ingrese el salario por hora: "))
print(f"{nombre} gana {(salario * horas)}")
print(f"Sueldo incrementado: {salario * horas * 1.15}")

# ---------------------------------------------------------------- Ejercicio 4
x = int(input("Ingrese un número: "))
y = int(input("Ingrese un número: "))
operacion = input("Ingrese la operación que desea realizar: ")
if operacion == "+":
    print(f"{x} + {y} = {x + y}")
elif operacion == "-":
    print(f"{x} - {y} = {x - y}")
elif operacion == "*":
    print(f"{x} * {y} = {x * y}")
elif operacion == "/":
    if y == 0:
        print("No se puede dividir por 0")
    else:
        print(f"{x} / {y} = {x / y}")
else:
    print("Operación inválida")

# ---------------------------------------------------------------- Ejercicio 5
mayor = 0
x = int(input("Ingrese un número: "))
y = int(input("Ingrese un número: "))
z = int(input("Ingrese un número: "))
if x > mayor:
    mayor = x
if y > mayor:
    mayor = y
if z > mayor:
    mayor = z
print(f"El número mayor es: {mayor}")

# ---------------------------------------------------------------- Ejercicio 6
numero = int(input("Ingrese un número: "))
print("El número es par" if numero % 2 == 0 else "El número es impar")

# ---------------------------------------------------------------- Ejercicio 7
base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))
print(f"El área del triángulo es: {(base * altura) / 2}")

# ---------------------------------------------------------------- Ejercicio 8
dni = input("Ingrese su DNI: ")
print("DNI correcto" if len(dni) == 8 else "DNI incorrecto")
