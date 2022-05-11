"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: needs some work due to poor details in the exercise. 
"""
from dataclasses import dataclass, field
from tkinter import Frame, Label, Tk, Entry
from typing import Dict, List

DEMANDA: Dict[int, str] = {
    1: "buena demanda",
    2: "poca demnada",
}


@dataclass
class Articulo:
    codigo: str
    precio: float
    existencias: int
    demanda: str

    def __post_init__(self):
        if self.demanda == DEMANDA[2] or self.existencia < 5:
            self.pedido = 20
        else:
            self.pedido = 0
        if self.demanda == DEMANDA[1] and self.existencia > 50:
            self.pedido = 100
        else:
            self.pedido = 200


@dataclass
class Informe:
    codigo: str
    cantidad: int
    costo_articulo: float = field(init=False)

    def __post_init__(self):
        self.costo_articulo = self.cantidad * Articulo.precio


@dataclass
class Informes:
    informe: List[Informe] = field(default_factory=list)
    total: float = field(init=False)
    pedidos: int = field(init=False)

    def __post_init__(self):
        self.total = sum(informe.costo_articulo for informe in self.informe)
        self.pedidos = sum(informe.cantidad for informe in self.informe)


class Data(Frame):

    def __init__(self, master=None):
        super().__init__(master)

    def setup_ui(self):
        for i, text in enumerate(("Seccion", "Codigo", "Cantidad")):
            Label(self, text=text).grid(row=i, column=0)
        seccion = Entry(self)
        seccion.grid(row=0, column=1)
        codigo = Entry(self)
        codigo.grid(row=1, column=1)
        cantidad = Entry(self)
        cantidad.grid(row=2, column=1)

    def evaluate(self):
        pass


class App:

    def __init__(self) -> None:
        self.root = Tk()
        self.widgets()

    def widgets(self):
        pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.mainloop()
