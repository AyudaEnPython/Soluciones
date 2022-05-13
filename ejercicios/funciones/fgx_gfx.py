"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada dos funciones:
f(x) =sqrt( 2 + 5x)
g(x) =(4 + x )^3

Se debe evaluar, para un conjunto de entradas, f(g(x)) si x es par, o
g(f(x)) si x es impar. 

Entrada
La entrada contiene un conjunto de líneas con cada uno de los valores
de x por evaluar (0 < x < 1000) y termina con un valor de 0 que no debe
procesarse

Salida
La salida debe contener para cada entrada una línea con el resultado
correspondiente. 

Ejemplo de entrada :
4
15
382
0 

Ejemplo de salida:
50.61620293937506 
2084.8705484240154 
16957.661454339745
"""
from typing import List, Union


def f(x: int) -> Union[int, float]:
    return (2 + 5 * x) ** 0.5


def g(x: int) -> Union[int, float]:
    return (4 + x) ** 3


def get_data(a: int = 0, b: int = 1000, n: int = 0) -> List[int]:
    data = []
    while True:
        x = input()
        try:
            x = int(x)
            if x == n:
                break
            if a < x < b:
                data.append(x)
        except ValueError:
            print("Entrada inválida")
    return data


def es_par(x: int) -> bool:
    return x % 2 == 0


def calcular(data: List[int]) -> List[Union[int, float]]:
    return [f(g(x)) if es_par(x) else g(f(x)) for x in data]


def main():
    print("\n".join(map(str, calcular(get_data()))))


if __name__ == "__main__":
    main()
