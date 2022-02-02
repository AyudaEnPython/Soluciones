"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar un programa en python que tenga una  función la cual debe
recibir los siguientes parámetros:
start: fecha de inicio
end:  fecha de final
delta: intervalo (el intevarlo debe ser cada una hora)

La función debe realizar los siguientes:
1- Generar a partir de la fecha de inicio  todas las fechas con un
intervalo de cada  hora hasta la fecha final.
Ejemplo:
start: 2009 05 01
end:  2009 05 02

5/1/2009 0:00
5/1/2009 1:00
5/1/2009 2:00
...
5/1/2009 22:00
5/1/2009 23:00
5/2/2009 0:00
5/2/2009 1:00
5/2/2009 2:00
...
5/2/2009 22:00
5/2/2009 23:00

Como pueden ver la la fecha inicial, inicia  a la 0:00  hora y la fecha
final termina a la 23:00 hora y el incremento es de una hora.

TODO: add tests later.
"""
import time


def generar_fechas(start: str, end: str, delta: int = 1):
    """Genera una lista con todas las fechas entre start y end con un
    intervalo de delta horas.

    :param start: fecha de inicio
    :start type: str
    :param end: fecha de final
    :end type: str
    :param delta: intervalo, por defecto 1 (hora)
    :delta type: int
    :return: lista con todas las fechas
    :rtype: list
    """
    fechas = []
    fecha_inicio = time.strptime(start, "%Y %m %d")
    fecha_final = time.strptime(end, "%Y %m %d")
    while fecha_inicio <= fecha_final:
        fechas.append(time.strftime("%m/%d/%Y %H:%M", fecha_inicio))
        fecha_inicio = time.localtime(
            time.mktime(fecha_inicio) + delta * 3600
        )
    return fechas


def generar_fechas_alt(start: str, end: str, delta: int = 1):
    """Genera una lista con todas las fechas entre start y end con un
    intervalo de delta horas.

    :param start: fecha de inicio
    :start type: str
    :param end: fecha de final
    :end type: str
    :param delta: intervalo, por defecto 1 (hora)
    :delta type: int
    :return: lista con todas las fechas
    :rtype: list
    """
    fechas = []
    if "/" in start and "/" in end:
        start = time.strptime(start, "%Y/%m/%d")
        end = time.strptime(end, "%Y/%m/%d")
    else:
        start = time.strptime(start, "%Y %m %d")
        end = time.strptime(end, "%Y %m %d")
    start, end = time.mktime(start), time.mktime(end)
    while start < end:
        fechas.append(time.strftime("%m/%d/%Y %H:%M", time.localtime(start)))
        start += delta * 3600
    return fechas


def main():
    print(generar_fechas_alt("2009 05 01", "2009 05 02", 1))
    print(generar_fechas("2009/05/01", "2009/05/02", 1))


if __name__ == "__main__":
    main()
