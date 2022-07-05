"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un banco realiza el pago de intereses a sus clientes por un deposito a
plazo fijo de acuerdo a la siguiente información: tipo de moneda,
tiempo de deposito y monto depositado. Los intereses serán según el
siguiente cuadro:

    +----------+---------+-----------+
    | Meses    | Soles % | Dolares % |
    +----------+---------+-----------+
    |  0 - 5   |    0    |     0     |
    |  6 - 12  |    6    |     4     |
    | 13 - mas |    9    |     7     |
    +----------+---------+-----------+

Mostrar el interes y el monto total a recibir.

* prueba de escritorio
d = 8500
mes = 12
mon = 2 (dolares)
inte = 340
total = 8840

NOTE: el enunciado original contenía varios errores ortográficos.
    La "prueba de escritorio" sugiere identificadores mal nombrados.
"""

deposito = float(input("Monto a depositar: "))
meses = int(input("Cantidad de meses: "))
moneda = int(input("Tipo de moneda (1 = soles, 2 = dolares): "))

if 0 <= meses <= 5:
    interes = 0 if moneda == 1 else 6
elif 6 <= meses <= 12:
    interes = 6 if moneda == 1 else 4
elif 13 <= meses:
    interes = 9 if moneda == 1 else 7

interes_ganado = deposito * (interes / 100)

print(f"Interes: {interes_ganado}")
print(f"Total: {deposito + interes_ganado}")
