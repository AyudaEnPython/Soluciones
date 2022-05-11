"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: stills needs some work
"""
from tkinter import Tk, Label, Button, Entry, Frame, Text, messagebox
from models import Empleado, Sistema


class App(Frame):

    def __init__(self):
        self.root = Tk()
        self.sistema = Sistema()
        self._widgets()
        self._layouts()
    
    def _widgets(self):
        for i, label in enumerate((
            "Nombre",
            "Cargo",
            "Sueldo",
            "Código",
        )):
            Label(self.root, text=label).grid(row=i, column=0, sticky="e")
        self.text = Text(self.root, width=20, height=4)
        self.nombre = Entry(self.root)
        self.cargo = Entry(self.root)
        self.sueldo = Entry(self.root)
        self.codigo = Entry(self.root)
        self.insertar = Button(self.root, text="Insertar")
        self.actualizar = Button(self.root, text="Actualizar")
        self.eliminar = Button(self.root, text="Eliminar")
        self.seleccionar = Button(self.root, text="Seleccionar")
        self.btn_salir = Button(self.root, text="Salir")

    def _layouts(self):
        self.nombre.grid(row=0, column=1, padx=5, pady=5)
        self.cargo.grid(row=1, column=1, padx=5, pady=5)
        self.sueldo.grid(row=2, column=1, padx=5, pady=5)
        self.codigo.grid(row=3, column=1, padx=5, pady=5)
        self.text.grid(columnspan=2, row=4, padx=5, pady=5, sticky="we")
        self.insertar.grid(row=5, column=1, padx=5, pady=5, sticky="we")
        self.actualizar.grid(row=6, column=1, padx=5, pady=5, sticky="we")
        self.eliminar.grid(row=7, column=1, padx=5, pady=5, sticky="we")
        self.seleccionar.grid(row=8, column=1, padx=5, pady=5, sticky="we")
        self.btn_salir.grid(row=9, column=1, padx=5, pady=5, sticky="we")
        self.insertar["command"] = self._insertar
        self.actualizar["command"] = self._actualizar
        self.eliminar["command"] = self._eliminar
        self.seleccionar["command"] = self._seleccionar
        self.btn_salir["command"] = self.root.destroy

    def _insertar(self):
        empleado = Empleado(*self._get_data())
        self.sistema.insertar(empleado)
        messagebox.showinfo("Insertar", "Agregado!")
        self._clear()

    def _actualizar(self):
        empleado = Empleado(*self._get_data())
        self.sistema.actualizar(empleado)

    def _eliminar(self):
        codigo = self.codigo.get()
        self.sistema.eliminar(codigo)
        messagebox.showinfo("Eliminar", "Eliminado!")
        self._clear()

    def _seleccionar(self):
        codigo = self.codigo.get()
        empleado = self.sistema.seleccionar(codigo)
        if empleado:
            self.text.insert(
                "1.0",
                empleado.to_str()
            )
        else:
            messagebox.showinfo("Seleccionar", "No existe!")

    def _get_data(self):
        nombre = self.nombre.get()
        cargo = self.cargo.get()
        sueldo = float(self.sueldo.get())
        return nombre, cargo, sueldo

    def _clear(self):
        self.nombre.delete(0, "end")
        self.cargo.delete(0, "end")
        self.sueldo.delete(0, "end")
        self.codigo.delete(0, "end")


if __name__ == "__main__":
    app = App()
    app.mainloop()
