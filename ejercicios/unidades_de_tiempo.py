"""
Leer una duración del usuario como un número de días, horas, minutos y
segundos. Calcular y mostrar el número total de segundos representados
por esta duración.
"""
from unittest import main, TestCase

def en_segundos(tiempo: str) -> int:
    """Convierte un tiempo en segundos

    :param tiempo: Tiempo expresado en dias:horas:minutos:segundos
    :tiempo type: str
    :return: Tiempo en segundos
    :rtype: int

    .. nota::
        u: unidad
        t: tiempo(int)
    
    >>> en_segundos('0:0:0:1')
    1
    """
    unidades = [60*60*24, 60*60, 60, 1]
    return sum([u*t for u, t in zip(unidades, map(int, tiempo.split(":")))])


class Test(TestCase):

    def test_en_segundos(self):
        self.assertEqual(en_segundos("1:0:0:0"), 86400)
        self.assertEqual(en_segundos("1:0:10:4"), 87004)
        self.assertEqual(en_segundos("2:12:46:29"), 218789)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()