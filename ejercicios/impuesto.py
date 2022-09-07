"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# Ejercicio 1

Se necesita que elabore un programa que calcule el valor del impuesto a
pagar para un vehículo, los datos de entrada para realizar este calculo
son: Placa, Modelo del vehículo, tipo del vehículo, y el valor comercial
del vehículo.

Antes de realizar los cálculos, los datos deben validarse de la
siguiente forma:
- La placa no podrá tener mas de 6 caracteres.
- El modelo no podrá ser menor que el año 2000 ni mayor que el año 2022.
- El tipo de vehículo solo podrá ser 1, 2 o 3.

El impuesto a pagar de un vehículo se calculade la siguiente manera:

    +---------+------+-------------------------+
    | Modelo  | Tipo | Impuesto                |
    +---------+------+-------------------------+
    | >= 2010 | 1, 2 | 10% del valor comercial |
    | >= 2010 | 3    | 15% del valor comercial |
    | < 2010  | 1, 2 | 20% del valor comercial |
    | < 2010  | 3    | 55% del valor comercial |
    +---------+------+-------------------------+

---

# Ejercicio 2

Se necesita que elabore un programa que calcule el valor del impuesto
para un predio, los datos de entrada para cada predio son: número de
matrícula, estrato socioeconómico y valor comercial del predio.

Antes de realizar el cálculo del impuesto, los datos deben validarse de
la siguiente forma:
- El número de matrícula solo podrá tener 7 caracteres.
- El estrato socioeconómico solo podrá ser un número entre 1 y 6.
- El número de pisos deberá ser entre 1 y 3.

El impuesto a pagar por un predio se calcula de la siguiente manera:

+--------------+----------------------------------------------------------+
|   Estrato    |                        Impuesto                          |
|socioeconómico|                                                          |
+--------------+----------------------------------------------------------+
|      1       |1% del valor comercial multiplicado por el número de pisos|
|      2       |2% del valor comercial multiplicado por el número de pisos|
|      3       |3% del valor comercial multiplicado por el número de pisos|
|      4       |4% del valor comercial multiplicado por el número de pisos|
|      5       |5% del valor comercial multiplicado por el número de pisos|
|      6       |6% del valor comercial multiplicado por el número de pisos|
+--------------+----------------------------------------------------------+

NOTE: Ambos ejercicios son practicamente iguales.
"""
from typing import Callable, List


def _int(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        raise ValueError("Debe ser un número entero")


def validar_caracteres(s: str, u: bool = False, n: int = None) -> str:
    if u and n is not None:
        if len(s) != n:
            raise ValueError(f"Debe tener {n} caracteres")
        else:
            return s
    if len(s) > n:
        raise ValueError(f"Máximo {n} caracteres")
    return s


def validar_rango(n: int, minimo: int, maximo: int) -> int:
    if n < minimo or n > maximo:
        raise ValueError(f"Debe estar entre {minimo} y {maximo}")
    return n


def calcular_impuesto_1(modelo: int, tipo: int, valor: int) -> int:
    impuesto = {
        (modelo >= 2010 and tipo in (1, 2)): valor * 0.1,
        (modelo >= 2010 and tipo == 3): valor * 0.15,
        (modelo < 2010 and tipo in (1, 2)): valor * 0.2,
        (modelo < 2010 and tipo == 3): valor * 0.55
    }
    return impuesto[True]


def calcular_impuesto_2(estrato: int, valor: int, pisos: int) -> int:
    return valor * (estrato/100) * pisos


def main(
    f: Callable, ss: List[str], min: int, max: int, u: bool, n: int
) -> None:
    try:
        a = validar_caracteres(input(f"{ss[0]}: "), u=u, n=n)
        b = validar_rango(_int(input(f"{ss[1]}: ")), minimo=min, maximo=max)
        c = validar_rango(_int(input(f"{ss[2]}: ")), minimo=1, maximo=3)
        d = _int(input(f"{ss[3]}: "))
        print(f"[{a}] Impuesto: ${f(b, c, d):.2f}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    funciones = calcular_impuesto_1, calcular_impuesto_2
    etiquetas = (
        ["Placa", "Modelo", "Tipo", "Valor"],
        ["Matrícula", "Estrato", "Pisos", "Valor"],
    )
    valores = (
        (2000, 2022, False, 6),
        (1, 6, False, 7),
    )
    for funcion, etiqueta, valor in zip(funciones, etiquetas, valores):
        main(funcion, etiqueta, *valor)
