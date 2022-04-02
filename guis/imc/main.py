"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import (
    Frame, Tk, Label, Entry, Button, Radiobutton, StringVar, Toplevel, Text
)
from models import Persona


class Resultado(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.display = Text(self, width=24, height=10)
        self.display.pack()


class UiMainWindow(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.v = StringVar()
        self.v.set("H")
        self.setup_ui()

    def setup_ui(self):
        Label(self, text="Nombre").grid(row=0, column=0)
        self.nombre = Entry(self)
        self.nombre.grid(row=0, column=1)
        Label(self, text="Apellido").grid(row=1, column=0)
        self.apellido = Entry(self)
        self.apellido.grid(row=1, column=1)
        Label(self, text="Edad:").grid(row=2, column=0)
        self.edad = Entry(self)
        self.edad.grid(row=2, column=1)
        self.h = Radiobutton(self, text="Hombre", variable=self.v, value="H")
        self.h.grid(row=3, column=0)
        self.m = Radiobutton(self, text="Mujer", variable=self.v, value="M")
        self.m.grid(row=3, column=1)
        Label(self, text="Peso").grid(row=4, column=0)
        self.peso = Entry(self)
        self.peso.grid(row=4, column=1)
        Label(self, text="Altura").grid(row=5, column=0)
        self.altura = Entry(self)
        self.altura.grid(row=5, column=1)
        self.calcular = Button(self, text="Calcular")
        self.calcular.grid(row=6, column=0)
        self.limpiar = Button(self, text="Limpiar")
        self.limpiar.grid(row=6, column=1)


class App(Tk):

    def __init__(self):
        super().__init__()
        self.frame = UiMainWindow(self)
        self.frame.pack()
        self.frame.calcular.config(command=self.calcular)
        self.frame.limpiar.config(command=self.limpiar)

    def calcular(self):
        persona = Persona(
            nombre=self.frame.nombre.get(),
            apellido=self.frame.apellido.get(),
            edad=int(self.frame.edad.get()),
            sexo=self.frame.v.get(),
            peso=float(self.frame.peso.get()),
            altura=float(self.frame.altura.get()),
        )
        w = Toplevel()
        w.title("Resultado")
        r = Resultado(w)
        r.pack()
        r.display.insert(
            "end",
            persona.to_str() + "\n"
        )
        Button(r, text="OK", command=w.destroy).pack()

    def limpiar(self):
        self.frame.nombre.delete(0, "end")
        self.frame.apellido.delete(0, "end")
        self.frame.edad.delete(0, "end")
        self.frame.h.select()
        self.frame.peso.delete(0, "end")
        self.frame.altura.delete(0, "end")


if __name__ == "__main__":
    app = App()
    app.mainloop()
