"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que determine qué número de participante fue el
ganador de la competencia.

NOTE: el enunciad no es claro y no brinda mas detalles.
"""
from typing import List, Tuple
# pip install prototools
from prototools import int_input

PARTICIPANTES = 3
tiempos = []


def entrada() -> Tuple[int, int, int]:
    """Entrada de datos

    :return: horas, minutos y segundos
    :rtype: Tupla[int]
    """
    horas = int_input("Hora: ", min=0, max=23)
    minutos = int_input("Minutos: ", min=0, max=59)
    segundos = int_input("Segundos: ", min=0, max=59)
    return horas, minutos, segundos


def convertir_tiempo(segundos: int) -> str:
    """Convierte un tiempo en segundos a horas, minutos y segundos

    :param segundos: tiempo en segundos
    :type segundos: int
    :return: tiempo en formato hh:mm:ss
    :rtype: str
    """
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"


def tiempo_a_segundos(horas: int, minutos: int, segundos: int) -> int:
    """Convierte el tiempo en segundos

    :param horas: horas
    :horas type: int
    :param minutos: minutos
    :minutos type: int
    :param segundos: segundos
    :segundos type: int
    :return: tiempo en segundos
    :rtype: int
    """
    return horas * 3600 + minutos * 60 + segundos


def calcular_ganador(tiempos: List[int]) -> int:
    """Calcula el ganador de la competencia

    :param tiempos: lista de tiempos
    :type tiempos: List[int]
    :return: ganador
    :rtype: int
    """
    ganador = 0
    for i, tiempo in enumerate(tiempos):
        if tiempo < tiempos[ganador]:
            ganador = i
    return ganador + 1


def main():
    for _ in range(PARTICIPANTES):
        tiempos.append(tiempo_a_segundos(entrada()))
    ganador = calcular_ganador(tiempos)
    print(f"El ganador es el participante {ganador}")
    tiempo = convertir_tiempo(tiempos[ganador - 1])
    print(f"El tiempo del ganador es {tiempo}")


if __name__ == "__main__":
    main()
