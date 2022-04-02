"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from datetime import datetime
from tkinter import Button, Entry, Frame, Label, Text, Toplevel
from models import Empleado, ReporteAsistencia, db


class Registro(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.widgets()

    def widgets(self):
        Label(self, text="Cédula").pack()
        self.cedula = Entry(self)
        self.cedula.pack(padx=5, pady=5)
        Label(self, text="Nombres").pack()
        self.nombres = Entry(self)
        self.nombres.pack(padx=5, pady=5)
        Label(self, text="Apellidos").pack()
        self.apellidos = Entry(self)
        self.apellidos.pack(padx=5, pady=5)
        self.guardar = Button(self, text="Guardar", command=self.guardar)
        self.guardar.pack(side="left", padx=5, pady=5)
        self.limpiar = Button(self, text="Limpiar", command=self.limpiar)
        self.limpiar.pack(side="right", padx=5, pady=5)

    def guardar(self):
        cedula = self.cedula.get()
        nombres = self.nombres.get()
        apellidos = self.apellidos.get()
        empleado = Empleado(cedula, nombres, apellidos)
        empleado.to_db()
    
    def limpiar(self):
        self.cedula.delete(0, "end")
        self.nombres.delete(0, "end")
        self.apellidos.delete(0, "end")


class Asistencia(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.widgets()

    def widgets(self):
        Label(self, text="Ingresar cédula").pack()
        self.cedula = Entry(self)
        self.cedula.pack(padx=5, pady=5)
        self.entrada = Button(
            self, text="Hora de entrada", command=self.registrar_entrada,
        )
        self.entrada.pack(fill="both", padx=5, pady=5)
        self.salida = Button(
            self, text="Hora de salida", command=self.registrar_salida,
        )
        self.salida.pack(fill="both", padx=5, pady=5)

    def registrar_entrada(self):
        cedula = self.cedula.get()
        fecha = self.obtener_fecha()
        entrada = self.obtener_hora()
        reporte = ReporteAsistencia(cedula, fecha, entrada, "")
        reporte.to_db()

    def registrar_salida(self):
        cedula = self.cedula.get()
        salida = self.obtener_hora()
        db.update("asistencia", f"salida='{salida}'", f"cedula='{cedula}'")

    def obtener_fecha(self):
        return datetime.now().strftime("%d/%m/%Y")

    def obtener_hora(self):
        return datetime.now().strftime("%H:%M:%S")


class Reporte(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.widgets()

    def widgets(self):
        self.reporte = Button(
            self, text="Ver Reporte", command=self.ver_reporte,
        )
        self.reporte.pack(fill="both", padx=5, pady=5)

    def ver_reporte(self):
        reporte = Toplevel()
        texto = Text(reporte, width=45, height=10)
        texto.pack(padx=5, pady=5)
        texto.insert(
            "1.0",
            f"{'Cedula':<8}|{'Fecha':<12}|{'Entrada':<10}|{'Salida':<10}\n",
        )
        datos = db.get_all("asistencia")
        for cedula, fecha, entrada, salida in datos:
            texto.insert(
                "end", f"{cedula:<8}|{fecha:<12}|{entrada:<10}|{salida:<10}\n"
            )
        texto.config(state="disabled")
