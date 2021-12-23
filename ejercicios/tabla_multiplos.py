"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Desarrollar un módulo Python con la función tabla_multiplos que reciba
tres números por parámetros: inicio, fin y num_base. Deberá recorrer y
mostrar: los números de una secuencia comprendida entre "ini" y "fin",
ambos incluidos, el texto "múltiplo de" seguido de num_base solo en el
caso de que el número de la secuencia sea múltiplo de "num_base" y el
valor de la suma acumulada de dichos múltiplos. También deberá devolver
el valor de la suma acumulada.
La función debe estar documentada correctamente.
Por ejemplo, para los valores: ini=3, fin=8 y num_base=4 deberá mostrar:
    3
    4 múltiplo de 4 - suma acumulada: 4
    5
    6
    7
    8 múltiplo de 4 - suma acumulada: 12
(Y deberá devolver: 12, para este ejemplo)
Hacer la prueba con otros valores además de los dados en el ejemplo.
# ---------------------------------------------------------------------
NOTE: Se opta por cambiar los identificadores de los parámetros y
    utilizar el estilo sphinx para la documentación.
"""
from unittest import main, TestCase


def tabla_mulitplos(inicio: int, fin: int, base: int) -> int:
    """Imprime una secuencia comprendida entre "inicio" y "fin"
    (ambos incluidos) con el texto "múltiplo de" si el número de la
    secuencia es múltiplo de "base" y la suma acumulada de dichos
    múltiplos.

    :param inicio: Número inicial de la secuencia.
    :inicio type: int
    :param fin: Número final de la secuencia.
    :fin type: int
    :param base: Número base para el cálculo de los múltiplos.
    :base type: int
    :return: La suma acumulada de los múltiplos.
    :return type: int
    """
    suma = 0
    for numero in range(inicio, fin + 1):
        if numero % base == 0:
            suma += numero
            print(f"{numero} múltiplo de {base} - suma acumulada: {suma}")
        else:
            print(numero)
    return suma


class Test(TestCase):

    def test_tabla_multiplos(self):
        self.assertEqual(tabla_mulitplos(3, 8, 4), 12)
        self.assertEqual(tabla_mulitplos(1, 10, 2), 30)
        self.assertEqual(tabla_mulitplos(1, 10, 3), 18)


if __name__ == "__main__":
    main()