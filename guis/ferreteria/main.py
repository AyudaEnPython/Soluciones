"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from tkinter import Frame, Tk, Label, Button, Entry, Text, Toplevel, ttk


@dataclass
class Cliente:
    dni: str
    nombres: str
    direccion: str
    telefono: str

    def __post_init__(self):
        self.fullname = f"{self.nombres}"


@dataclass
class Producto:
    descripcion: str
    precio: float
    cantidad: int

    def calculate(self):
        return self.precio * self.cantidad


class App(Tk):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.top = Frame(self)
        self.left = Frame(self)
        self.right = Frame(self)
        self.top.grid(row=0, columnspan=2, sticky="nsew")
        self.left.grid(row=1, column=0, sticky="nsew")
        self.right.grid(row=1, column=1, sticky="nsew")
        self.widgets()
        self.layout()

    def widgets(self):
        Label(self.top, text="DNI").grid(row=0, column=0)
        Label(self.top, text="Apellidos, Nombres").grid(row=0, column=2)
        Label(self.top, text="Direccion").grid(row=1, column=0)
        Label(self.top, text="Telefono").grid(row=1, column=2)
        ttk.Separator(
            self.top, orient="horizontal"
        ).grid(row=2, columnspan= 4, sticky="ew", pady=10)
        for i, text in enumerate(["Producto", "Precio", "Cantidad"]):
            Label(self.left, text=text).grid(row=i, column=0)
        self.dni = Entry(self.top)
        self.nombres = Entry(self.top)
        self.direccion = Entry(self.top)
        self.telefono = Entry(self.top)
        self.producto = Entry(self.left, width=40)
        self.precio = Entry(self.left)
        self.cantidad = Entry(self.left)
        self.registrar = Button(self.right, text="Registrar", command=self.calcular)
        self.reporte = Button(self.right, text="Reporte", command=self.reportar)

    def layout(self):
        self.dni.grid(row=0, column=1, padx=5, pady=5)
        self.nombres.grid(row=0, column=3, padx=5, pady=5)
        self.direccion.grid(row=1, column=1, padx=5, pady=5)
        self.telefono.grid(row=1, column=3, padx=5, pady=5)
        self.producto.grid(row=0, column=1, padx=5, pady=5)
        self.precio.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.cantidad.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.registrar.grid(row=0, column=0, padx=5, pady=5)
        self.reporte.grid(row=1, column=0, padx=5, pady=5)

    def calcular(self):
        nombre = self.nombres.get()
        dni = self.dni.get()
        direccion = self.direccion.get()
        telefono = self.telefono.get()
        producto = self.producto.get()
        precio = float(self.precio.get())
        cantidad = int(self.cantidad.get())
        cliente = Cliente(dni, nombre, direccion, telefono)
        producto = Producto(producto, precio, cantidad)
        total = producto.calculate()
        self.reporte = (
            f"Cliente: {cliente.fullname}\n"
            f"DNI: {cliente.dni}\n"
            f"Direccion: {cliente.direccion}\n"
            f"Telefono: {cliente.telefono}\n"
            f"Producto: {producto.descripcion}\n"
            f"Precio: {producto.precio}\n"
            f"Cantidad: {producto.cantidad}\n"
            f"Total: {total}"
        )
        self.clear()

    def clear(self):
        self.dni.delete(0, "end")
        self.nombres.delete(0, "end")
        self.direccion.delete(0, "end")
        self.telefono.delete(0, "end")
        self.producto.delete(0, "end")
        self.precio.delete(0, "end")
        self.cantidad.delete(0, "end")

    def reportar(self):
        top = Toplevel(self)
        top.title("Reporte")
        display = Text(
            top, width=30, height=8, font=("Arial", 12)
        )
        display.delete(1.0, "end")
        display.insert(
            "1.0", self.reporte
        )
        display.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
