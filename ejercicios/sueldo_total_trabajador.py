"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El programa deberá calcular el total a pagar al trabajador de acuerdo a
las siguientes reglas:

a) Si el número de horas trabajadas es menor o igual a 40 el monto a
    pagar es el número de horas multiplicado por su tarifa de pago por
    hora.
b) Si el número de horas trabajadas es mayor a 40 pero menor o igual a
    50, el monto a pagar es el mismo que en el inciso a) más la
    diferencia en horas por arriba de 40 a una tasa por hora 10% más
    alta de la tarifa básica.
c) Si el número de horas trabajadas es mayor a 50, el monto a pagar es
    el mismo que en el inciso b) más la diferencia en horas por arriba
    de 50 a una tasa por hora 20% más alta de la tarifa básica.
d) En caso de que alguno de los valores capturados inicialmente (número
    de horas trabajadas por semana o tarifa de pago por hora) sea
    errónea (ya sea debido a la captura de valores negativos o de texto),
    deberá imprimirse un mensaje que diga "Parámetros incorrectos".

Ejemplo:

    Número de horas trabajadas: 55
    Tarifa por hora: 5

        Monto a pagar: 40(5) + 10(5)(1.1) + 5(5)(1.2) = 258
"""

HORA_BASE = 40
TASAS = {"a": 1.0, "b": 1.1, "c": 1.2}
SUPERIOR, INFERIOR = 50, 40


def validar(n: str) -> float:
    if not n.isdigit():
        raise ValueError("Parámetros incorrectos")
    if int(n) < 0:
        raise ValueError("Parámetros incorrectos")
    return float(n)


def pago(horas: int, tarifa: float) -> float:
    ex_1 = ex_2 = 0
    pago_base = HORA_BASE * tarifa
    if horas > SUPERIOR:
        ex_1 = (horas - SUPERIOR) * tarifa * TASAS["c"]
        ex_2 = (50 - HORA_BASE) * tarifa * TASAS["b"]
    elif INFERIOR < horas <= SUPERIOR:
        ex_1 = (horas - INFERIOR) * tarifa * TASAS["b"]
    return pago_base + ex_1 + ex_2


def main():
    try:
        horas = validar(input("Número de horas trabajadas: "))
        tarifa = validar(input("Tarifa por hora: "))
    except ValueError as e:
        print(e)
    else:
        print(f"Monto a pagar: {pago(horas, tarifa):.2f}")


if __name__ ==  "__main__":
    main()
