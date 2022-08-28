"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El seguimiento del IMC es una forma útil de comprobar si se mantiene un
peso saludable. Se calcula a partir del peso y la altura de una persona,
utilizando esta fórmula: peso / altura²

El número resultante indica una de las siguientes categorías:
Underweight = menos de 18.5
Normal = 18.5 - 24.9
Overweight = 25 - 29.9
Obesity = 30 o más

Hagamos que averiguar tu IMC sea más rápido y fácil, creando un script 
que tome el peso y la altura de una persona como entrada y genere la 
categoría de IMC correspondiente.
"""
from unittest import main, TestCase
# pip install prototools
from prototools import int_input, float_input


def imc(peso: float, estatura: float) -> float:
    """Devuele el IMC

    :param peso: Peso en kg
    :peso type: float
    :param estatura: Estatura en m
    :estatura type: float
    :return: IMC
    :rtype: float

    >>> imc(78, 1.83)
    23.29
    """
    return round(peso/(estatura**2), 2)


def solucion_a(imc: float) -> str:
    """Devuelve una categoría de acuerdo al imc

    :param imc: Índice de masa corporal
    :imc type: float
    :return: Categoría
    :rtype: str
    """
    if imc < 18.5:
        return "Underweight"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Overweight"
    else:
        return "Obesity"


def solucion_b(imc: float) -> str:
    """Devuelve una categoría de acuerdo al imc

    :param imc: Índice de masa corporal
    :imc type: float
    :return: Categoría
    :rtype: str
    """
    categories = {
        imc < 18.5: "Underweight",
        18.5 <= imc < 25: "Normal",
        25 <= imc < 30: "Overweight",
        30 < imc: "Obesity",
    }
    return categories[True]


def solucion_c(imc: float) -> str:
    """Devuelve una categoría de acuerdo al imc

    :param imc: Índice de masa corporal
    :imc type: float
    :return: Categoría
    :rtype: str
    """
    categorias = {
        imc < 16: "criterio de ingreso hospitalario",
        16 <= imc < 17: "infrapeso",
        17 <= imc < 18: "bajo peso",
        18 <= imc < 25: "saludable",
        25 <= imc < 30: "sobrepeso",
        30 <= imc < 35: "sobrepeso crónico",
        35 <= imc < 40: "sobrepeso premórbida",
        40 <= imc: "obesidad mórbida",
    }
    return categorias[True]


def solver():
    peso = float(input("Peso: "))
    estatura = float(input("Estatura: "))
    return solucion_b(imc(peso, estatura))


def _datos():
    nombre = input("Nombre: ")
    peso = float_input("Peso: ")
    altura = float_input("Altura: ")
    return nombre, peso, altura


def main_list():
    data = []
    n = int_input("Cantidad de personas: ", min=1)
    for _ in range(n):
        nombre, peso, altura = _datos()
        resultado = solucion_c(imc(peso, altura))
        data.append((nombre, peso, altura, resultado))
    for nombre, peso, altura, resultado in data:
        print(
            f"{nombre} pesa {peso}kg y mide {altura}m,",
            f"tiene un IMC de {resultado}.",
        )


def main_dict():
    data = {}
    n = int_input("Cantidad de personas: ", min=1)
    for _ in range(n):
        nombre, peso, altura = _datos()
        resultado = solucion_c(imc(peso, altura))
        data[nombre] = (peso, altura, resultado)
    for nombre, (peso, altura, resultado) in data.items():
        print(
            f"{nombre} pesa {peso}kg y mide {altura}m,",
            f"tiene un IMC de {resultado}.",
        )


class Test(TestCase):

    def test_imc(self):
        self.assertAlmostEqual(imc(85, 1.9), 23.55)

    def test_soluciones(self):
        self.assertEqual(solucion_a(18.42), "Underweight")
        self.assertEqual(solucion_b(23.00), "Normal")
        self.assertEqual(solucion_a(25.24), "Overweight")
        self.assertEqual(solucion_b(31.04), "Obesity")


if __name__ == "__main__":
    # import doctest

    # doctest.testmod()
    # main()             # Uncomment the above lines to run tests
    # print(solver())    # for single solution without name
    main_dict()         # or use main_list()
