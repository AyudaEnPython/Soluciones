"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import logging

logging.basicConfig(level=logging.INFO)


class Elevador:

    _table = {1: "Subiendo", -1: "Bajando"}

    def __init__(self, piso_actual: int = 1) -> None:
        self.piso = piso_actual
        self.display = ""

    def handler(self, destino: int) -> None:
        self.mover(1) if self.piso < destino else self.mover(-1)

    def mover(self, x: int) -> None:
        self.piso += x
        self.display = f"{self._table[x]} al piso {self.piso}"
        logging.info(self.display)

    def goto(self, destino: int) -> None:
        while self.piso != destino:
            self.handler(destino)
        self.display = "Parada en el piso {}".format(destino)
        logging.info(self.display)


class Panel:

    def __init__(self, elevador: Elevador) -> None:
        self.elevador = elevador

    def press(self, x: int) -> None:
        self.elevador.goto(x)


class PanelInterno(Panel):

    def presionar(self, destino: int) -> None:
        super().press(destino)


class PanelExterno(Panel):

    def llamar_desde(self, en_piso: int) -> None:
        super().press(en_piso)


if __name__ == "__main__":
    elevador = Elevador()
    interno = PanelInterno(elevador)
    externo = PanelExterno(elevador)
    externo.llamar_desde(5)
    interno.presionar(2)
    externo.llamar_desde(6)
    interno.presionar(4)
    interno.presionar(5)
    externo.llamar_desde(1)
