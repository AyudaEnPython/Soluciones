"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import (
    Label, Entry, Button, Radiobutton, messagebox, IntVar, ttk, Frame
)


class UiMainWindow(Frame):

    def __init__(self) -> None:
        super().__init__()
        self.v = IntVar()
        self.v.set(0)
        self.setup_ui()

    def setup_ui(self):
        Label(self, text="Nombre").grid(row=0, column=0, pady=5)
        self.nombre = Entry(self)
        self.nombre.grid(row=0, column=1, padx=5)
        Label(self, text="Edad").grid(row=1, column=0, pady=5)
        self.edad = Entry(self)
        self.edad.grid(row=1, column=1, padx=5)
        Label(self, text="Inscribió la cédula?").grid(row=2, column=0)
        self.si = Radiobutton(self, text="Si", variable=self.v, value=1)
        self.si.grid(row=3, column=0)
        self.no = Radiobutton(self, text="No", variable=self.v, value=0)
        self.no.grid(row=3, column=1)
        ttk.Separator(self, orient="horizontal").grid(
            row=4, column=0, columnspan=2, sticky="ew", pady=10)
        self.verificar = Button(self, text="Verificar")
        self.verificar.grid(row=5, column=0)
        self.limpiar = Button(self, text="Limpiar")
        self.limpiar.grid(row=5, column=1)
        ttk.Separator(self, orient="horizontal").grid(
            row=6, column=0, columnspan=2, sticky="ew", pady=10)
        Label(self, text="Ayuda en Python").grid(row=8, column=1, sticky="e")


class App(UiMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.verificar["command"] = self.f
        self.limpiar["command"] = self.clear
        self.pack()

    def f(self) -> None:
        nombre = self.nombre.get()
        edad = int(self.edad.get())
        if (18 <= edad <= 70) and self.v.get():
            messagebox.showinfo(message=f"{nombre}, puedes votar")
        else:
            messagebox.showerror(message=f"{nombre}, no puedes votar")

    def clear(self) -> None:
        self.nombre.delete(0, "end")
        self.edad.delete(0, "end")
        self.no.select()


if __name__ == "__main__":
    app = App()
    app.mainloop()
