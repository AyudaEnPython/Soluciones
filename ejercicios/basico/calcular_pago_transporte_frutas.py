"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una empresa de carga realiza el transporte de frutas, el precio por la
carga está en función al tipo de fruta a transportar y la distancia en
kilómetros que debe recorrer, los precios que se muestran en la tabla
es por cada caja de fruta:


    +---------+------------------------------+
    |         |       Distancia en km        |
    |  Fruta  +----------------+-------------+
    |         | menos de 30 km | 30 o más km |
    +---------+----------------+-------------+
    | Naranja |      S/.2.00   |   S/.4.00   |
    |  Fresa  |      S/.6.00   |   S/.9.00   |
    |  Mango  |      S/.3.00   |   S/.5.00   |
    +---------+----------------+-------------+

Sólo se realiza la carga de un solo tipo de fruta. Calcular el pago que
debe realizarse por esa carga.
"""

fruta = input("Fruta a transportar: ").lower()
cajas = int(input("Cantidad de cajas: "))
distancia = float(input("Distancia en km: "))

if distancia <= 30:
    if fruta == "naranja":
        precio = 2.00
    elif fruta == "fresa":
        precio = 6.00
    else:
        precio = 3.00
else:
    if fruta == "naranja":
        precio = 4.00
    elif fruta == "fresa":
        precio = 9.00
    else:
        precio = 5.00

print(f"Pago: S/.{cajas * precio}")
