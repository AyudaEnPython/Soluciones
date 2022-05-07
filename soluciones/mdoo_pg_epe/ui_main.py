"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import (
    Button,
    Entry,
    Label,
    Frame,
    messagebox,
    Radiobutton,
    StringVar,
    Tk,
    Toplevel,
)
from typing import Dict, List, Tuple

from models import Estudiante, Calificacion, Registrar
from utils import validar_notas

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

    def __init__(self, estudiante: Estudiante, master=None):
        super().__init__(master)
        self.estudiante = estudiante
        self.estudiantes = []
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
        estudiante = self.estudiante(
            codigo=self.codigo.get(),
            nombre_completo=self.nombre_completo.get(),
            modalidad=self._mod.get(),
        )
        self.estudiantes.append(estudiante)
        w = Toplevel()
        w.title("Registro")
        self.calificacion = Calificaciones(self._mod.get(), w)
        self.calificacion.pack()

    def get_estudiantes(self):
        return self.estudiantes

    def limpiar(self):
        self.codigo.delete(0, "end")
        self.nombre_completo.delete(0, "end")


class Calificaciones(Frame):

    def __init__(self, modalidad, master=None):
        super().__init__(master)
        self.modalidad = modalidad
        self.calificaciones = []
        self.setup_ui()

    def setup_ui(self):
        for i, label in enumerate(CALIFICACIONES[self.modalidad]):
            Label(self, text=label).grid(row=i, column=0, sticky="e")
        self.n1 = Entry(self)
        self.n2 = Entry(self)
        self.n3 = Entry(self)
        self.n4 = Entry(self)
        self.n1.grid(row=0, column=1, padx=5, pady=5)
        self.n2.grid(row=1, column=1, padx=5, pady=5)
        self.n3.grid(row=2, column=1, padx=5, pady=5)
        self.n4.grid(row=3, column=1, padx=5, pady=5)
        self.guardar = Button(self, text="Guardar", command=self.guardar)
        self.guardar.grid(row=4, column=0, padx=5, pady=5)
        self.limpiar = Button(self, text="Limpiar", command=self.limpiar)
        self.limpiar.grid(row=4, column=1, padx=5, pady=5)

    def guardar(self):
        try:
            n1 = validar_notas(self.n1.get())
            n2 = validar_notas(self.n2.get())
            n3 = validar_notas(self.n3.get())
            n4 = validar_notas(self.n4.get())
        except ValueError:
            messagebox.showerror("Error", "Notas inválidas")
        calificacion = Calificacion(
            n1, n2, n3, n4, self.modalidad
        )
        self.calificaciones.append(calificacion)

    def get_calificaciones(self):
        return self.calificaciones

    def limpiar(self):
        self.n1.delete(0, "end")
        self.n2.delete(0, "end")
        self.n3.delete(0, "end")
        self.n4.delete(0, "end")


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("AyudaEnPython")
        self.formulario = Formulario(Estudiante, self)
        self.formulario.pack()
        self.guardar = Button(self, text="To Excel", command=self.guardar)
        self.guardar.pack()

    def guardar(self):
        estudiantes = self.formulario.get_estudiantes()
        calificaciones = self.formulario.calificacion.get_calificaciones()
        registro = Registrar(estudiantes, calificaciones)
        registro.to_excel()
        messagebox.showinfo("Exito", "Archivo guardado")


if __name__ == "__main__":
    app = App()
    app.mainloop()
