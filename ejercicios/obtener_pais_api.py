"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Se le pide implementar un programa que entregue el nombre completo de
un país recibiendo como input el código abreviado de dicho país.
Para ello, debe ayudarse de la siguiente API:

    https://restcountries.com/v3/alpha/[codigo]

Ejemplo, si se quiere saber el nombre del país con código "co", hacer
lo siguiente:
https://restcountries.com/v3/alpha/co
Y mostrar el campo name/oficial

Escriba una función getCountry(codigo) que devuelva el resultado
esperado.
# ---------------------------------------------------------------------
NOTE: se opta a cambiar el nombre de la función (PEP8).
"""
import requests
from unittest import main, TestCase

# or get_country (PEP8)
def obtener_pais(codigo: str) -> str:
    """Obtiene el nombre del país a partir del código.
    
    :param codigo: Código del país.
    :codigo type: str
    :return: Nombre del país.
    :rtype: str
    """
    url = f"https://restcountries.com/v3/alpha/{codigo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[0]["name"]["nativeName"]["spa"]["official"]
    else:
        return "No se encontró el país"


class Test(TestCase):

    def test_obtener_pais(self):
        self.assertEqual(obtener_pais("co"), "República de Colombia")


if __name__ == "__main__":
    main()