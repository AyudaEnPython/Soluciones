"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


class Controlador:

    def __init__(self, modelo: object, vista: object) -> None:
        self.model = modelo
        self.vista = vista

    def configurar(self) -> None:
        size = self.vista.read("Tamaño: ")
        min = self.vista.read("Mínimo: ")
        max = self.vista.read("Máximo: ")
        self.model.generar(size, min, max)
        self.vista.info("Números generados!")

    def numeros(self) -> None:
        self.vista.show(self.model.numeros)

    def pares(self) -> None:
        data = self.model.pares()
        self.vista.show(data)

    def impares(self) -> None:
        data = self.model.impares()
        self.vista.show(data)
