"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Optional

TIPO: Dict[int, str] = {
    4: "automovil",
    2: "motocicleta",
}


class Vehiculo:

    def __init__(self, marca: str, ruedas: int, color: str) -> None:
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.__en_marcha: bool = False

    def arrancar(self) -> None:
        self.__en_marcha = True

    def tipo(self) -> Optional[str]:
        return TIPO.get(self.ruedas)

    def info(self) -> None:
        print(self)

    def __str__(self) -> str:
        return (
            f"Marca: {self.marca}\n"
            f"Ruedas: {self.ruedas}\n"
            f"Color: {self.color}\n"
            f"En marcha: {self.__en_marcha}"
        )


if __name__ == "__main__":
    vehiculo = Vehiculo("BMW", 4, "rojo")
    vehiculo.info()
    print(f"Tipo de vehículo: {vehiculo.tipo()}")
    vehiculo.arrancar()
    vehiculo.info()
    otro_vehiculo = Vehiculo("Honda", 2, "azul")
    otro_vehiculo.info()
    print(f"Tipo de vehículo: {otro_vehiculo.tipo()}")
