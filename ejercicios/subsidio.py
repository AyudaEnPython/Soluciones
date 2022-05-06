"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se requiere una función que permita calcular si las personas son
beneficiarias de un subsidio de vivienda que da el estado, para lo cual
debe cumplir los siguientes requisitos:

Mayor de 25 años y menores de 40 años y tener menos de 2 hijos: se le
da de subsidio $ 12.000.000

Mayores de 40 años y mas de 2 hijos: se le otorga $ 15.000.000

Mayor de 40 años o mas de 2 hijos: se le otorga $ 13.000.000

En otro caso se le da $ 5000.000 de subsidio

El programa debe ejecutar hasta que se indique que se desea terminar.

Realizar otra función que, basado en el cálculo anterior, calcule el
valor total que recibe la persona en ayudas para vivienda. Si el
municipio le otorga $ 8000.000 a las mujeres y $ 7000.000 a los
hombres.

NOTE: Los requisitos a cumplir no son claros.
"""
# pip install prototools
from prototools import int_input, menu_input, main_loop

GENERO = "masculino", "femenino"


def calcular_subsidio(edad: int, hijos: int) -> int:
    if 25 <= edad < 40 and hijos < 2:
        return 12_000
    elif 40 <= edad and hijos > 2:
        return 15_000
    elif 40 <= edad or hijos > 2:
        return 13_000
    else:
        return 5_000


def calcular_total(genero: str, subsidio: int) -> int:
    return subsidio + {"masculino": 7000, "femenino": 8000}[genero]


def main():
    genero = menu_input(GENERO, numbers=True, lang="es")
    edad = int_input("Ingrese su edad: ", min=0, lang="es")
    hijos = int_input("Ingrese la cantidad de hijos: ", min=0, lang="es")
    subsidio = calcular_subsidio(edad, hijos)
    total = calcular_total(genero, subsidio)
    print(f"El subsidio que recibe es: ${subsidio}")
    print(f"El total que recibe es: ${total}")


if __name__ == "__main__":
    main_loop(main)
