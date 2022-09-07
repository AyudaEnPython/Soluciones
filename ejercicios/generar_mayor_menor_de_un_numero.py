"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un programa que reciba un número natural de máximo 9 cifras y
que encuentre e imprima el número mayor y el menor que se pueden formar
con las cifras del número.

De preferencia hacer uso de funciones para:
a. Realizar la validación que el número sea mayor que cero y no exceda
    las nueve cifras.
b. Determinar el número mayor que se puede formar.
c. Determinar el número menor que se puede formar.

No podrá hacer uso de cálculo de potencia o logaritmo, sean en
funciones propias ni de la librería math.h. Asímismo, no podrá hacer
uso de arreglos ni tipo string.

En la siguiente tabla se muestran algunos ejemplos:

    +-------------+----------------------+----------------------+
    | Número dado | Número mayor formado | Número menor formado |
    +-------------+----------------------+----------------------+
    | 6174        | 7641                 | 1467                 |
    | 35499       | 99543                | 34599                |
    | 111         | 111                  | 111                  |
    +-------------+----------------------+----------------------+

"""
#  numero = sorted(input("Ingrese un número: "))
#  print(f"Mayor: {''.join(numero)} | Menor: {''.join(numero[::-1])}")
import unittest
from typing import Callable


def obtener_numero() -> int:
    return int(input("Ingrese un número: "))


def validar_numero(numero: int) -> None:
    if numero < 0:
        raise ValueError("El número debe ser mayor que cero")
    if numero > 9:
        raise ValueError("El número debe ser menor que 10")


def cantidad_de_digitos(numero: int) -> int:
    i = 0
    while numero > 0:
        numero //= 10
        i += 1
    return i


def obtener_mayor(numero: int) -> int:
    j = cantidad_de_digitos(numero)
    mayor = numero % 10
    k = 0
    for i in range(j):
        actual = numero % 10
        if actual > mayor:
            mayor = actual
            k = i
        numero //= 10
    return mayor, k


def obtener_menor(numero: int) -> int:
    j = cantidad_de_digitos(numero)
    menor = numero % 10
    k = 0
    for i in range(j):
        actual = numero % 10
        if actual < menor:
            menor = actual
            k = i
        numero //= 10
    return menor, k


def remover_digito(numero: int, posicion: int) -> int:
    izq = numero // 10 ** (posicion + 1)
    der = numero % 10 ** posicion
    if izq == 0:
        return der
    elif der == 0:
        return izq
    else:
        return izq * 10 ** posicion + der


def calcular(n: int, f: Callable) -> str:
    i = cantidad_de_digitos(n)
    r = ""
    while i > 0:
        res, k = f(n)
        r += str(res)
        n = remover_digito(n, k)
        i -= 1
    return r


def main():
    n = obtener_numero()
    print(f"Ingrese un número: {n}")
    print(f"Mayor: {calcular(n, obtener_mayor)}")
    print(f"Mayor: {calcular(n, obtener_menor)}")


class Test(unittest.TestCase):

    cases_mayor_menor = (
        (7614, (7, 3), (1, 1)),
        (6174, (7, 1), (1, 2)),
        (35499, (9, 0), (3, 4)),
        (111, (1, 0), (1, 0)),
    )
    cases = (
        (6174, "7641", "1467"),
        (35499, "99543", "34599"),
        (111, "111", "111"),
    )

    def test_validar(self):
        with self.assertRaises(ValueError):
            validar_numero(-1)
        with self.assertRaises(ValueError):
            validar_numero(10)

    def test_obtener_mayor_menor(self):
        for n, mayor, menor in self.cases_mayor_menor:
            self.assertEqual(obtener_mayor(n), mayor)
            self.assertEqual(obtener_menor(n), menor)

    def test_calcular(self):
        for n, mayor, menor in self.cases:
            self.assertEqual(calcular(n, obtener_mayor), mayor)
            self.assertEqual(calcular(n, obtener_menor), menor)


if __name__ == "__main__":
    # main()
    unittest.main()
