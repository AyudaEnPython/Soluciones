"""
Leer una duración del usuario como un número de días, horas, minutos y
segundos. Calcular y mostrar el número total de segundos representados
por esta duración.
"""
import doctest
from random import randint


def en_segundos(tiempo: str) -> int:
    """Convierte un tiempo en segundos

    :param tiempo: Tiempo expresado en dias:horas:minutos:segundos
    :tiempo type: str
    :return: Tiempo en segundos
    :rtype: int

    .. nota::
        u: unidad
        t: tiempo(int)
    
    >>> en_segundos('1:0:0:0')
    86400
    >>> en_segundos('1:0:10:4')
    87004
    >>> en_segundos('2:12:46:29')
    218789
    """
    unidades = [60*60*24, 60*60, 60, 1]
    return sum([u*t for u, t in zip(unidades, map(int, tiempo.split(":")))])


def obtener_tiempo_usuario(dias: int = 7) -> str:
    """Retorna una cadena de forma aleatoria

    :param dias: Máximo de días
    :dias type: int
    :return: Tiempo aleatorio
    :rtype: str
    """
    return f"{randint(0, dias)}:{randint(0, 24)}:{randint(0, 12)}:{randint(0, 60)}"


def main():
    tiempo = obtener_tiempo_usuario()
    print(f"Tiempo original: {tiempo}")
    print(f"Tiempo en segundos: {en_segundos(tiempo)}")


if __name__ == "__main__":
    doctest.testmod()
    main()