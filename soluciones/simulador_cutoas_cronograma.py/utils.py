from datetime import datetime
from dateutil.relativedelta import relativedelta


def diferencia_dias(a: str, b: str) -> int:
    """
    Calcula la diferencia de días entre dos fechas sin importar el
    orden

    :param a: Fecha inicial
    :param b: Fecha final
    :return: Diferencia de días
    """
    return abs(
        datetime.strptime(b, "%Y-%m-%d") - datetime.strptime(a, "%Y-%m-%d")
    ).days


def sumar_mes(a: str) -> str:
    """
    Suma un mes a una fecha

    :param a: Fecha
    :return: Fecha sumada
    """
    date = datetime.strptime(a, "%Y-%m-%d") + relativedelta(months=1)
    return str(date.date())


def convertir_fecha(
    fecha: str, dia: int = None, mes: int = None, caracter: str = "-"
) -> str:
    dd, mm, aaaa = fecha.split(caracter)
    if len(dd) > 2:
        dd, aaaa = aaaa, dd
    dia = dia if dia is not None else dd
    mes = mes if mes is not None else mm
    return f"{aaaa}-{mes}-{dia}"


def _tem(I: float) -> float:
    """
    Retorna el valor de la tasa efectiva mensual

    :param I: Tasa efectiva anual
    :return: Tasa efectiva mensual
    """
    return ((1+I)**(30/360))-1


def _cuota_mensual(L: float, I: float, n: float) -> float:
    """
    Calcula los pagos mensuales de un cronograma

    :param L: Monto del préstamo
    :param I: Tasa de interes
    :param n: Número de cuotas
    :return: Monto de la cuota
    """
    return L * (I * ((1+I) ** n) / ((1+I) ** n - 1))


def show(data):
    ss = (8, 12, 18, 5, 10, 16, 10, 10)
    print("+"+"-"*(112)+"+")
    print("|", end=" ")
    for k, s in zip(data[0], ss):
        print(f"{k:>{s}}", end=" | ")
    print()
    print("+"+"-"*(112)+"+")
    for d in data:
        print("|", end=" ")
        for v, s in zip(d.values(), ss):
            print(f"{v:>{s}}", end=' | ')
        print()
    print("+"+"-"*(112)+"+")