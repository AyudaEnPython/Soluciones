"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Se tiene un diccionario donde el nombre de un platillo es la clave y
valor es una lista de nombres de personas que lo consumen. Escribe una
función ordenarDiccionario(diccionario) que ordena el diccionario
basado en la cantidad de personas que consumen cada platillo.

    +------------------------------------------------------+
    | dicccionario = {                                     |
    |     "Lomo saltado": ["Kevin", "Fernando", "Kathia"], |
    |     "Arroz chaufa": ["Alessandra"],                  |
    |     "Causa": ["Mateo", "Camila"],                    |
    | }                                                    |
    |                                                      |
    | resultado = {                                        |
    |     "Arroz chaufa": ["Alessandra"],                  |
    |     "Causa": ["Mateo", "Camila"],                    |
    |     "Lomo saltado": ["Kevin", "Fernando", "Kathia"], |
    | }                                                    |
    +------------------------------------------------------+
# ---------------------------------------------------------------------
NOTE: Se mejoro el ejemplo y se opta por usar otro nombre para la
    función (PEP8)
"""
from typing import Dict, List
from unittest import main, TestCase


def ordenar(diccionario: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Funcion que ordena el diccionario basado en la cantidad de personas
    que consumen cada platillo.

    :param diccionario: Diccionario con los datos a ordenar
    :diccionario: Dict[str, List[str]]
    :return: Diccionario ordenado
    :rtype: Dict[str, List[str]]
    """
    return {
        key: diccionario[key]
        for key in sorted(diccionario, key=lambda x: len(diccionario[x]))
    }


class Test(TestCase):

    datos = {
        "Lomo saltado": ["Kevin", "Fernando", "Kathia"],
        "Arroz chaufa": ["Alessandra"],
        "Causa": ["Mateo", "Camila"],
    }

    def test_ordenar(self):
        self.assertEqual(
            ordenar(self.datos),
            {
                "Arroz chaufa": ["Alessandra"],
                "Causa": ["Mateo", "Camila"],
                "Lomo saltado": ["Kevin", "Fernando", "Kathia"],
            },
        )


if __name__ == "__main__":
    main()