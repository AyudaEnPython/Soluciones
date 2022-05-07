"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import (
    Button,
    Entry,
    Label,
    Frame,
    Radiobutton,
    StringVar,
)
from typing import Dict, Tuple

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


class Calificaciones(Frame):

    def __init__(self, modalidad, master=None) -> None:
        super().__init__(master)
        self.modalidad = modalidad
        self.setup_ui()

    def setup_ui(self) -> None:
        for i, label in enumerate(CALIFICACIONES[self.modalidad]):
            Label(self, text=label).grid(row=i, column=0, sticky="e")
        self.n1 = Entry(self)
        self.n2 = Entry(self)
        self.n3 = Entry(self)
        self.n4 = Entry(self)
        self.guardar = Button(self, text="Guardar")
        self.limpiar = Button(self, text="Limpiar", command=self.clear)
        self.n1.grid(row=0, column=1, padx=5, pady=5)
        self.n2.grid(row=1, column=1, padx=5, pady=5)
        self.n3.grid(row=2, column=1, padx=5, pady=5)
        self.n4.grid(row=3, column=1, padx=5, pady=5)
        self.guardar.grid(row=4, column=0, padx=5, pady=5)
        self.limpiar.grid(row=4, column=1, padx=5, pady=5)

    def clear(self) -> None:
        self.n1.delete(0, "end")
        self.n2.delete(0, "end")
        self.n3.delete(0, "end")
        self.n4.delete(0, "end")


class Formulario(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self._mod = StringVar()
        self._mod.set("PG")
        self.setup_ui()

    def setup_ui(self) -> None:
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
        self.registrar = Button(self, text="Registrar")
        self.limpiar = Button(self, text="Limpiar", command=self.clear)
        self.codigo.grid(row=0, column=1, padx=5, pady=5)
        self.nombre_completo.grid(row=1, column=1, padx=5, pady=5)
        self.rbn_pg.grid(row=2, column=0, sticky="e")
        self.rbn_epe.grid(row=2, column=1, sticky="e")
        self.registrar.grid(row=3, column=0, padx=5, pady=5)
        self.limpiar.grid(row=3, column=1, padx=5, pady=5)

    def clear(self) -> None:
        self.codigo.delete(0, "end")
        self.nombre_completo.delete(0, "end")
