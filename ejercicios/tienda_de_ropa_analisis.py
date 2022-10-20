"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El dueño de una tienda que vende ropa, a final de mes necesita realizar
un análisis de las ventas, para ello cuenta con una copia de cada una
de las facturas que representan las ventas de todo el mes.

Confeccione un algoritmo que procesa a leer el monto neto de la factura
y el número de factura y entregue como resultado los siguientes datos:
- Número de facturas procesadas.
- Valor total neto de todas las facturas.
- Venta promedio neta.
- Total, de impuesto pagado.
- A qué número de factura corresponde la mayor venta.

El fin de ingreso está dado por un valor igual a cero en el número de
la factura.

NOTE: el enunciado no indica el impuesto, se asume un 18%.
"""
# pip install prototools
from prototools import float_input

IGV = 0.18


def procesar(data):
    max_ = sum_ = impuesto = 0
    for k, v in data.items():
        sum_ += v
        impuesto += v - (v * (1 - IGV))
        if v > max_:
            max_ = v
            factura = k
    return sum_, sum_/len(data), impuesto, factura


def ingresar():
    facturas = {}
    while True:
        monto = float_input("Monto neto: ")
        if monto == 0.0:
            break
        factura = input("N° de factura: ")
        if factura not in facturas:
            facturas[factura] = monto
        else:
            print("Factura ya ingresada!")
    return facturas


def main():
    facturas = ingresar()
    sum_, mean_, igv, max_ = procesar(facturas)
    print(f"Número de facturas procesadas: {len(facturas)}")
    print(f"Valor neto de todas las facturas: {sum_}")
    print(f"Venta promedio neta: {mean_:.2f}")
    print(f"Total de impuesto pagado: {igv:.2f}")
    print(f"N° de factura de mayor venta: {max_}")


if __name__ == "__main__":
    main()
