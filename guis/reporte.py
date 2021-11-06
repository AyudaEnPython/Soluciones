"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import pandas as pd
from dataclasses import dataclass
from dataclasses import dataclass, field, asdict
from tkinter import Frame, Tk, Label, Entry, Button


@dataclass
class Reporte:
    proveedor: str = field(default="")
    cliente: str = field(default="")
    servicio: str = field(default="")
    precio: float = field(default=0.0)
    descuento: float = field(default=0.0)
    total: float = field(default=0.0)
    
    def calcular_total(self):
        self.total = self.precio - self.descuento

    def generar(self):
        return asdict(self)


class App(Frame):
    
    def __init__(self):
        self.root = Tk()

    def setup(self):
        self.root.title("Reporte")
        self.root.geometry("220x230")
        self.data = []

    def widgets(self):
        for i, label in enumerate(
            ("Proveedor", "Cliente", "Servicio", "Precio", "Descuento")):
            Label(self.root, text=label).grid(row=i, column=0, sticky="e")
        self.txt_proveedor = Entry(self.root)
        self.txt_cliente = Entry(self.root)
        self.txt_servicio = Entry(self.root)
        self.txt_precio = Entry(self.root)
        self.txt_descuento = Entry(self.root)
        self.btn_guardar = Button(self.root, text="Guardar")
        self.btn_salir = Button(self.root, text="Generar y Salir")

    def layout(self):
        self.txt_proveedor.grid(row=0, column=1, padx=5, pady=5)
        self.txt_cliente.grid(row=1, column=1, padx=5, pady=5)
        self.txt_servicio.grid(row=2, column=1, padx=5, pady=5)
        self.txt_precio.grid(row=3, column=1, padx=5, pady=5)
        self.txt_descuento.grid(row=4, column=1, padx=5, pady=5)
        self.btn_guardar.grid(row=5, column=1, padx=5, pady=5, sticky="we")
        self.btn_salir.grid(row=6, column=1, padx=5, pady=5, sticky="we")

    def generar_reporte(self, event):
        reporte = Reporte()
        reporte.cliente = self.txt_cliente.get()
        reporte.proveedor = self.txt_proveedor.get()
        reporte.servicio = self.txt_servicio.get()
        reporte.precio = float(self.txt_precio.get())
        reporte.descuento = float(self.txt_descuento.get())
        reporte.calcular_total()
        self.data.append(reporte.generar())
        self._clear_entries()

    def salir(self, event):
        self._export_to_excel()
        self.root.destroy()

    def _clear_entries(self):
        self.txt_cliente.delete(0, "end")
        self.txt_proveedor.delete(0, "end")
        self.txt_servicio.delete(0, "end")
        self.txt_precio.delete(0, "end")
        self.txt_descuento.delete(0, "end")

    def _export_to_excel(self):
        df = pd.DataFrame(self.data)
        df.to_excel("reporte.xlsx")

    def run(self):
        self.setup()
        self.widgets()
        self.layout()
        self.btn_guardar.bind("<Button-1>", self.generar_reporte)
        self.btn_salir.bind("<Button-1>", self.salir)
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()