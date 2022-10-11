"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from random import randint
from string import ascii_uppercase


@dataclass
class Persona:
    dni: str = ""
    nombre: str = ""
    apellido: str = ""
    edad: int = 0
    sexo: str = "H"
    peso: float = 0.0
    altura: float = 0.0

    def __post_init__(self) -> None:
        self.dni = self.generar_dni()

    def categoria_imc(self) -> str:
        imc = round(self.peso / (self.altura ** 2), 2)
        categories = {
            imc < 18.5: "Bajo peso",
            18.5 <= imc < 25: "Normal",
            25 <= imc < 30: "Sobrepeso",
            30 < imc: "Obesidad",
        }
        return categories[True]

    def es_mayor_edad(self) -> bool:
        return "Si" if self.edad >= 18 else "No"

    def _comprobar_sexo(self) -> None:
        if self.sexo not in ("H", "M"):
            self.sexo = "H"

    def generar_dni(self) -> str:
        letra = randint(0, 25)
        return str(randint(10000000, 99999999)) + ascii_uppercase[letra]

    def to_str(self):
        sexo = {"H": "Hombre", "M": "Mujer"}
        return (
            f"Nombre: {self.nombre}\n"
            f"Apellido: {self.apellido}\n"
            f"DNI: {self.dni}\n"
            f"Edad: {self.edad}\n"
            f"Sexo: {sexo[self.sexo]}\n"
            f"Peso: {self.peso}\n"
            f"Altura: {self.altura}\n"
            f"IMC: {self.categoria_imc()}\n"
            f"Es mayor de edad: {self.es_mayor_edad()}"
        )
