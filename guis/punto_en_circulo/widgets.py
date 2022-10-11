"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Frame, Label, ttk


class Form(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.setup_ui()

    def setup_ui(self) -> None:
        self.circulo = ttk.LabelFrame(self, text="Circulo")
        self.circulo.grid(rowspan=2, column=0, padx=10, pady=10)
        self.h = Entry(self.circulo)
        self.k = Entry(self.circulo)
        self.r = Entry(self.circulo)
        Label(self.circulo, text="h").grid(row=0, column=0)
        Label(self.circulo, text="k").grid(row=1, column=0)
        Label(self.circulo, text="r").grid(row=2, column=0)
        self.h.grid(row=0, column=1, padx=5, pady=5)
        self.k.grid(row=1, column=1, padx=5, pady=5)
        self.r.grid(row=2, column=1, padx=5, pady=5)
        self.punto = ttk.LabelFrame(self, text="Punto")
        self.punto.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
        self.x = Entry(self.punto)
        self.y = Entry(self.punto)
        Label(self.punto, text="x").grid(row=0, column=0)
        Label(self.punto, text="y").grid(row=1, column=0)
        self.x.grid(row=0, column=1, padx=5, pady=5)
        self.y.grid(row=1, column=1, padx=5, pady=5)
        self.calcular = Button(self, text="Calcular")
        self.calcular.grid(row=1, column=1, padx=10, pady=10)
        self.clear = Button(self, text="Limpiar")
        self.clear.grid(row=1, column=2, padx=10, pady=10)

    def clear_form(self) -> None:
        self.h.delete(0, "end")
        self.k.delete(0, "end")
        self.r.delete(0, "end")
        self.x.delete(0, "end")
        self.y.delete(0, "end")
