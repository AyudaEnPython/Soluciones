"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Button, Toplevel, messagebox

from models import Estudiante, Calificacion, Registrar
from widgets import Formulario, Calificaciones
from utils import validar_notas, validar_codigos


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("AyudaEnPython")
        self.setup_ui()
        self.estudiantes = []
        self.registro_calificaciones = []

    def setup_ui(self) -> None:
        self.formulario = Formulario(self)
        self.guardar = Button(self, text="To Excel", command=self.save)
        self.quit = Button(self, text="Salir", command=self.destroy)
        self.formulario.registrar.config(command=self.registrar_notas)
        self.formulario.pack()
        self.guardar.pack(fill="x")
        self.quit.pack(fill="x")

    def registrar(self) -> None:
        try:
            estudiante = Estudiante(
                codigo=validar_codigos(
                    self.estudiantes, self.formulario.codigo.get()
                ),
                nombre_completo=self.formulario.nombre_completo.get(),
                modalidad=self.formulario._mod.get(),
            )
            self.estudiantes.append(estudiante)
        except ValueError:
            messagebox.showerror("Error", "Código ya registrado")
            return False
        return True

    def save(self) -> None:
        registro = Registrar(self.estudiantes, self.registro_calificaciones)
        registro.guardar_calificacion()
        messagebox.showinfo("Exito", "Archivo guardado")

    def registrar_notas(self) -> None:
        if not self.registrar():
            return
        self.w = Toplevel()
        self.w.title("Registro")
        self.calificaciones = Calificaciones(
            self.formulario._mod.get(), self.w)
        self.calificaciones.guardar.config(
            command=self.registrar_calificaciones)
        self.calificaciones.pack()

    def registrar_calificaciones(self) -> None:
        try:
            n1 = validar_notas(self.calificaciones.n1.get())
            n2 = validar_notas(self.calificaciones.n2.get())
            n3 = validar_notas(self.calificaciones.n3.get())
            n4 = validar_notas(self.calificaciones.n4.get())
        except ValueError:
            messagebox.showerror("Error", "Notas inválidas")
        calificacion = Calificacion(
            self.calificaciones.modalidad, n1, n2, n3, n4
        )
        self.registro_calificaciones.append(calificacion)
        self.w.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
