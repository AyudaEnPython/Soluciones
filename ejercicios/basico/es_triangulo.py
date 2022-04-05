"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar las medidas de los lados de un triángulo y luego mostrar si
las medidas corresponden a un triángulo. Las medidas corresponden a un
triángulo si la suma de dos de sus lados es mayor al tercer lado para
todos sus lados.

Ejemplo:
- Si se ingresa 5.0, 4.0, 3.0; mostrará, "Las medidas corresponden a un
    triángulo".
- Si se ingresa 10.0, 20.0 y 10.0; mostrará, "Las medidas NO
    corresponden a un triángulo".
"""

a = float(input("Ingrese la medida del primer lado: "))
b = float(input("Ingrese la medida del segundo lado: "))
c = float(input("Ingrese la medida del tercer lado: "))

if a + b > c and a + c > b and b + c > a:
    print("Las medidas corresponden a un triángulo")
else:
    print("Las medidas NO corresponden a un triángulo")
