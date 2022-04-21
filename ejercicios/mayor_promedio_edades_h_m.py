"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar la edad y género ([M]: Masculino, [F]: Femenino) de N personas
y luego mostrar:
- Promedio de las edades
- Promedio de las edades de los hombres
- Cantidad de mujeres con edad mayor a 30 años
- Mayor edad ingresada
"""
import unittest
from typing import List, Tuple
# pip install prototools
from prototools import int_input, menu_input


def promedio(arr: List[int]) -> float:
    return sum(arr)/len(arr)


def cantidad(arr: List[int], n: int) -> int:
    return len([e for e in arr if e > n]) 


def get_data() -> Tuple[List[float], List[float]]:
    n = int_input("Ingresar cantidad de personas: ", min=1)
    hombres, mujeres = [], []
    for _ in range(n):
        edad = int_input("Ingresar la edad: ", min=1, max=100)
        genero = menu_input(["masculino", "femenino"], numbers=True)
        if genero == "masculino":
            hombres.append(edad)
        else:
            mujeres.append(edad)
    return hombres, mujeres


def main():
    h, m = get_data()
    print(f"Promedio de edades: {promedio(h + m)}")
    print(f"Promedio de edad de hombres: {promedio(h)}")
    print(f"Cantidad de mujeres con edad mayor a 30 años: {cantidad(m, 30)}")
    print(f"Mayor edad ingresada: {max(h + m)}")


class Test(unittest.TestCase):

    def test_promedio(self):
        self.assertEquals(promedio([20, 15, 18, 22]), 18.75)

    def test_cantidad(self):
        self.assertEquals(cantidad([32, 23, 52, 40, 30, 28, 18], 30), 3)


if __name__ == "__main__":
    # unittest.main()
    main()
