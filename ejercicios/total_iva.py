"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Realizar un programa que permita el ingreso de la cantidad de 2
productos y el precio unitario de dicho producto, se desea calcular y
presentar el valor Total a pagar, se calcula el IVA 12%.

# ------------------------ Enunciado Modificado -----------------------
Realizar un programa que permita el ingresar la cantidad de un producto
y su precio unitario. Se desea calcular el total a pagar, considerando
un IVA de 12%.

# ---------------------------------------------------------------------
NOTE: El enunciado original está mal redactado.
"""

IVA = 1.12

cantidad = int(input("Ingresar cantidad: "))
precio = float(input("Ingresar precio unitario: "))
total = (cantidad * precio) * IVA

print(f"El total a pagar es: {total:.2f}")