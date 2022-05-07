"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import (
    Button,
    Entry,
    Label,
    Frame,
    Radiobutton,
    StringVar,
    Tk,
    Toplevel,
)
from typing import Dict, List, Tuple


CALIFICACIONES: Dict[str, Tuple[str, ...]] = {
    "PG": (
        "Práctica Calificada 1",
        "Práctica Calificada 2",
        "Proyecto Final",
        "Examen Final",
    ),
    "EPE": (
        "Práctica Calificada 1",
        "Práctica Calificada 2",
        "Trabajo Parcial",
        "Trabajo Final",
    ),
}


class Formulario(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self._mod = StringVar()
        self._mod.set("PG")
        self.setup_ui()

    def setup_ui(self):
        for i, label in enumerate(("Código", "Nombre completo")):
            Label(self, text=label).grid(row=i, column=0, sticky="e")
        self.codigo = Entry(self)
        self.nombre_completo = Entry(self)
        self.rbn_pg = Radiobutton(
            self, text="PG", variable=self._mod, value="PG"
        )
        self.rbn_epe = Radiobutton(
            self, text="EPE", variable=self._mod, value="EPE"
        )
        self.rbn_pg.grid(row=2, column=0, sticky="e")
        self.rbn_epe.grid(row=2, column=1, sticky="e")
        self.codigo.grid(row=0, column=1, padx=5, pady=5)
        self.nombre_completo.grid(row=1, column=1, padx=5, pady=5)
        self.registrar = Button(
            self, text="Registrar", command=self.registrar)
        self.registrar.grid(row=3, column=0, padx=5, pady=5)
        self.limpiar = Button(self, text="Limpiar", command=self.limpiar)
        self.limpiar.grid(row=3, column=1, padx=5, pady=5)

    def registrar(self):
        modalidad = self._mod.get()
        w = Toplevel()
        w.title("Registro")
        Calificaciones(modalidad, w).pack()

    def limpiar(self):
        self.codigo.delete(0, "end")
        self.nombre_completo.delete(0, "end")


class Calificaciones(Frame):

    def __init__(self, modalidad, master=None):
        super().__init__(master)
        self.modalidad = modalidad
        self.setup_ui()

    def setup_ui(self):
        for i, label in enumerate(CALIFICACIONES[self.modalidad]):
            Label(self, text=label).grid(row=i, column=0, sticky="e")
        self.pc1 = Entry(self)
        self.pc2 = Entry(self)
        self.x = Entry(self)
        self.y = Entry(self)
        self.pc1.grid(row=0, column=1, padx=5, pady=5)
        self.pc2.grid(row=1, column=1, padx=5, pady=5)
        self.x.grid(row=2, column=1, padx=5, pady=5)
        self.y.grid(row=3, column=1, padx=5, pady=5)
        self.guardar = Button(self, text="Guardar", command=self.guardar)
        self.guardar.grid(row=4, column=0, padx=5, pady=5)
        self.limpiar = Button(self, text="Limpiar", command=self.limpiar)
        self.limpiar.grid(row=4, column=1, padx=5, pady=5)

    def guardar(self):
        pass

    def limpiar(self):
        self.pc1.delete(0, "end")
        self.pc2.delete(0, "end")
        self.x.delete(0, "end")
        self.y.delete(0, "end")


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("AyudaEnPython")
        Formulario(self).pack()
        self.guardar = Button(self, text="To Excel", command=self.guardar)
        self.guardar.pack()

    def guardar(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
