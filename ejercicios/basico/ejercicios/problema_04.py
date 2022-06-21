"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una juguetería tiene mucho éxito en dos de sus productos: payasos y
muñecas.

Suele hace venta por correo y la empresa de logística les cobra por
peso de cada paquete así que deben calcular el peso de los payasos y
muñecas que saldrán en cada paquete a demanda.

Cada payaso pesa 112 g y cada muñeca pesa 75 g.

Escribir un programa que lea el número de payasos y muñecas vendidos en
el último pedido y calcule el peso total del paquete que será enviado.
"""

PAYASO_PESO = 112
MUÑECA_PESO = 75

payasos = int(input("Payasos vendidos: "))
muñecas = int(input("Muñecas vendidas: "))

peso = (payasos * PAYASO_PESO) + (muñecas * MUÑECA_PESO)

print(f"El peso total del paquete es {peso} g.")
