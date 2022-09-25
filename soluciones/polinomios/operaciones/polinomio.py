"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from unittest import main, TestCase
from typing import List


def grado(p: int) -> int:
    """Calcula el grado de un polinomio

    :param p: polinomio
    :p type: list
    :return: grado del polinomio
    :rtype: int
    """
    return len(p)-1


def evaluar(p: List[float], x: float) -> float:
    """Evalua un polinomio en x

    :param p: polinomio
    :p type: list
    :param x: valor a evaluar
    :x type: float
    :return: valor del polinomio en x
    :rtype: float
    """
    return round(sum(p[i]*x**i for i in range(len(p))), 5)


def sumar_polinomios(p: List[float], q: List[float]) -> List[float]:
    """Suma dos polinomios

    :param p: polinomio
    :p type: list
    :param q: polinomio
    :q type: list
    :return: polinomio resultante
    :rtype: list
    """
    max_: int = max(len(p), len(q))
    p += [0]*(max_ - len(p))
    q += [0]*(max_ - len(q))
    return [p[i]+q[i] for i in range(max_)]


def derivar_polinomio(p: List[float]) -> List[float]:
    """Deriva un polinomio

    :param p: polinomio
    :p type: list
    :return: polinomio derivado
    :rtype: list
    """
    return [p[i]*i for i in range(1, len(p))]


def multiplicar_polinomios(p: List[float], q: List[float]) -> List[float]:
    """Multiplica dos polinomios

    :param p: polinomio
    :p type: list
    :param q: polinomio
    :q type: list
    :return: polinomio resultante
    :rtype: list
    """
    if len(q) > len(p):
        p, q = q, p
    result: List[float] = [0] * (len(p) + len(q) - 1)
    for i in range(len(p)):
        for j in range(len(q)):
            result[i + j] += p[i] * q[j]
    return result


class Test(TestCase):

    p = [1, 2, 1]
    q = [4, -17]
    r = [-1, 0, 0, -5, 0, 3]
    s = [0]*40 + [5] + [0]*39 + [2]

    def test_grado(self):
        self.assertEqual(grado(self.r), 5)
        self.assertEqual(grado(self.s), 80)

    def test_evaluar(self):
        self.assertEqual(evaluar(self.p, 3), 16)
        self.assertEqual(evaluar(self.q, 0.0), 4.0)
        self.assertEqual(evaluar(self.r, 1.1), -2.82347)
        self.assertEqual(evaluar([4, 3, 1], 3.14), 23.2796)

    def test_sumar_polinomios(self):
        self.assertEqual(
            sumar_polinomios(self.p, self.r), [0, 2, 1, -5, 0, 3]
        )

    def test_derivar_polinomios(self):
        self.assertEqual(derivar_polinomio(self.r), [0, 0, -15, 0, 15])

    def test_multiplicar_polinomios(self):
        self.assertEqual(
            multiplicar_polinomios(self.p, self.q), [4, -9, -30, -17]
        )


if __name__ == '__main__':
    main()
