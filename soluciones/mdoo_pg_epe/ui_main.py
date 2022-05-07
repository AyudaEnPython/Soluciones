"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import tkinter as tk

from models import Estudiante, Calificacion, Registrar
from widgets import Formulario, Calificaciones
from utils import validar_notas



class App(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("AyudaEnPython")
        self.setup_ui()
        self.estudiantes = []
        self.registro_calificaciones = []

    def setup_ui(self) -> None:
        self.formulario = Formulario(self)
        self.formulario.pack()
        self.formulario.registrar.config(command=self.registrar_notas)
        self.guardar = tk.Button(self, text="To Excel", command=self.save)
        self.guardar.pack()

    def registrar(self) -> None:
        estudiante = Estudiante(
            codigo=self.formulario.codigo.get(),
            nombre_completo=self.formulario.nombre_completo.get(),
            modalidad=self.formulario._mod.get(),
        )
        self.estudiantes.append(estudiante)

    def save(self) -> None:
        registro = Registrar(self.estudiantes, self.registro_calificaciones)
        registro.guardar_calificacion()
        tk.messagebox.showinfo("Exito", "Archivo guardado")

    def registrar_notas(self) -> None:
        self.registrar()
        w = tk.Toplevel()
        w.title("Registro")
        self.calificaciones = Calificaciones(self.formulario._mod.get(), w)
        self.calificaciones.guardar.config(command=self.registrar_calificaciones)
        self.calificaciones.pack()

    def registrar_calificaciones(self) -> None:
        try:
            n1 = validar_notas(self.calificaciones.n1.get())
            n2 = validar_notas(self.calificaciones.n2.get())
            n3 = validar_notas(self.calificaciones.n3.get())
            n4 = validar_notas(self.calificaciones.n4.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Notas inválidas")
        calificacion = Calificacion(
            self.calificaciones.modalidad, n1, n2, n3, n4
        )
        self.registro_calificaciones.append(calificacion)
        self.calificaciones.clear()


if __name__ == "__main__":
    app = App()
    app.mainloop()
