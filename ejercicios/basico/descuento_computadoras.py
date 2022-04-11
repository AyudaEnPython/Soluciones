"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoras que compre. Si el
número de computadoras es menor a 5 tendrá un descuento de un 7% del
total de la compora; si el número es mayor o igual a 5 pero menor a
10 se le otorga 25% de descuento total de la compra; y si son 10 o
más se les da un 45% de descuento total de la compra.
Además, si el cliente paga con tarjeta se le aplicará un recargo de un
10% al total de la compra, si paga en efectivo se le aplicará un
descuento de un 15% del total de la compra. El programa debe mostrar el
total a pagar por el cliente.
"""

cantidad = int(input("Ingrese la cantidad de computadoras: "))
precio = float(input("Ingrese el precio de la computadora: "))
print("Ingrese el medio de pago: (T)arjeta o (E)fectivo?")
medio = input("> ")

total = cantidad * precio
descuento = 0

if cantidad < 5:
    descuento *= 0.07
elif 5 <= cantidad < 10:
    descuento *= 0.25
elif cantidad >= 10:
    descuento *= 0.45

total -= descuento

if medio == "T":
    total *= 1.1
elif medio == "E":
    total *= 0.85

print(f"El total a pagar es: {total}")
