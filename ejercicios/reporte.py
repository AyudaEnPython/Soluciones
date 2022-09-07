"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un reporte llamado "Reporte de Ingresos", el cual deberá contener
los costos que se han cobrado por los Servicios que se han realizado.
Donde deberás tener en cuenta que el Ingreso Neto es igual al
Costo - Porcentaje de Descuento. Este reporte deberá mostrarse así:

+----------------------------------------------------------------------+
|                          Titulo del Reporte                          |
+----+---------+----------+--------+--------------------+--------------+
| NP | Nombre  |          | Costo  |   Descuento Neto   | Ingreso Neto |
|    |   del   | Servicio |  (en   | Aplicado (Cantidad | (Cantidad en |
|    | Cliente |          | pesos) | en Pesos)          |  Pesos)      |
+----+---------+----------+--------+--------------------+--------------+
"""
reporte = []

n = int(input("Ingrese la cantidad de clientes: "))

for i in range(n):
    proveedor = input("Ingrese el nombre del proveedor: ")
    cliente = input("Ingrese el nombre del cliente: ")
    servicio = input("Ingrese el nombre del servicio: ")
    costo = float(input("Ingrese el costo del servicio: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    ingreso = round(costo - (costo * descuento / 100), 2)
    reporte.append(
        [proveedor, cliente, servicio, costo, descuento, ingreso]
    )

print("=" * 72)
print(" Reporte de Ingresos ".center(72, " "))
print("=" * 72)
print(
    "{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
        "Proveedor", "Cliente", "Servicio", "Costo", "Descuento", "Ingreso"
    )
)
for i in range(n):
    print("-" * 72)
    print(
        "{:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
            reporte[i][0],
            reporte[i][1],
            reporte[i][2],
            reporte[i][3],
            reporte[i][4],
            reporte[i][5]
        )
    )
print("-" * 72)
