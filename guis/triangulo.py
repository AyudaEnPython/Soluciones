"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: the person that needed help didn't post the description of the
    problem...
"""
from tkinter import Tk, Label, Entry, Button, Radiobutton, IntVar
from typing import Callable, Dict


def hipotenusa(a: float, b: float, _: None) -> float:
    return (a**2 + b**2)**0.5


def semiperimetro(a: float, b: float, h: float) -> float:
    return (a + b + h) / 2


def perimetro(a: float, b: float, h: float) -> float:
    return a + b + h


def area(a: float, b: float, h: float) -> float:
    sp = semiperimetro(a, b, h)
    return (sp * ((sp - a) * (sp - b) * (sp - h))) ** 0.5


class App(Tk):

    options: Dict[int, Callable] = {
        1: hipotenusa,
        2: semiperimetro,
        3: perimetro,
        4: area,
    }

    def __init__(self) -> None:
        super().__init__()
        self.title("Ayuda en Python")
        self.option = IntVar()
        self.setup_ui()

    def setup_ui(self) -> None:
        Label(self, text="Primer cateto").grid(row=0, column=0)
        Label(self, text="Segundo cateto").grid(row=1, column=0)
        Label(self, text="Hipotenusa").grid(row=2, column=0)
        self.a = Entry(self)
        self.b = Entry(self)
        self.h = Entry(self)
        self.calcular = Button(self, text="Calcular", command=self.f)
        self.salir = Button(self, text="Salir", command=self.destroy)
        self.resultado = Entry(self, state="readonly")
        self.a.grid(row=0, column=1)
        self.b.grid(row=1, column=1)
        self.h.grid(row=2, column=1)
        for v, f_ in self.options.items():
            Radiobutton(
                self, text=f_.__name__, value=v, variable=self.option
            ).grid(row=v+2, columnspan=2, sticky="ew")
        self.calcular.grid(row=7, columnspan=2, sticky="ew")
        self.salir.grid(row=8, columnspan=2, sticky="ew")
        self.resultado.grid(row=9, columnspan=2, sticky="ew")

    def _write(self, text) -> None:
        self.resultado["state"] = "normal"
        self.resultado.delete(0, "end")
        self.resultado.insert(0, text)
        self.resultado["state"] = "readonly"

    def f(self) -> None:
        try:
            a = float(self.a.get())
            b = float(self.b.get())
            h = float(self.h.get())
        except ValueError:
            self._write("Ingrese valores correctos")
            return
        resultado = self.options[self.option.get()](a, b, h)
        self._write(resultado)


if __name__ == "__main__":
    app = App()
    app.mainloop()
