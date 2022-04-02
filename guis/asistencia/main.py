"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import tkinter as tk
from frames import Reporte, Registro, Asistencia


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.left = tk.Frame(self)
        self.right = tk.Frame(self)
        self.left.pack(side="left")
        self.right.pack(side="right")
        self.setup()

    def setup(self):
        self.registro = Registro(self.left)
        self.asistencia = Asistencia(self.right)
        self.reporte = Reporte(self.right)
        self.registro.pack()
        self.asistencia.pack()
        self.reporte.pack()

    def run(self):
        self.title("Ayuda en Python")
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
