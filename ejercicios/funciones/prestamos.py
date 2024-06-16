
"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Una empresa de préstamos tiene el siguiente esquema de cobros:

    +-------------------------+------------------+
    | Monto del préstamo S/.  | Número de cuotas |
    +-------------------------+------------------+
    |       Hasta 5000        |        2         |
    +-------------------------+------------------+
    | Desde 5000 hasta 10000  |        4         |
    +-------------------------+------------------+
    | Desde 10000 hasta 15000 |        6         |
    +-------------------------+------------------+
    |       Más de 15000      |       10         |
    +-------------------------+------------------+

Si el monto del préstamo es mayor de S/. 10000, la empresa cobra 3% de
interés mensual; en caso contrario, cobra 5% de interés mensual.

Dado el monto del préstamo de un cliente, diseñe un programa que
determine el número de cuotas, el monto de la cuota mensual y el monto
del interés total entre todas las cuotas.

Declare todas las variables como globales y use métodos sin retorno.
# ---------------------------------------------------------------------
NOTE: El uso de variables globales no es recomendable
"""
# flake8: noqa
UNIDAD = "S/."


def obtener_tasa_de_interes(p):
    return .03 if p > 10_000 else .05


def obtener_periodo_de_tiempo(p):
    if p <= 5_000:
        t = 2
    elif p <= 10_000:
        t = 4
    elif p <= 15_000:
        t = 6
    else:
        t = 10
    return t


def calcular_interes(p, r, t):
    """
    Retorna el interés total

    :param p: Monto del préstamo
    :param r: Tasa de interés
    :param t: periodo de tiempo
    """
    return p * r * t


def calcular_cuota_mensual(p, r, t):
    return (p * (1 + r*t))/t


def mostrar(t, cuota, interes):
    print(f"Número de cuotas: {t}")
    print(f"Monto de la cuota mensual: {UNIDAD} {cuota:.2f}")
    print(f"Monto del interés total: {UNIDAD} {interes:.2f}")


def main():
    p = float(input("Ingresar monto del préstamo: "))
    r = obtener_tasa_de_interes(p)
    t = obtener_periodo_de_tiempo(p)
    interes = calcular_interes(p, r, t)
    cuota = calcular_cuota_mensual(p, r, t)
    mostrar(t, cuota, interes)


if __name__ == "__main__":
    main()
