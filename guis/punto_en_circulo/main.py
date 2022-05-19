"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Label, Tk, messagebox

from models import Punto, Circulo
from widgets import Form


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("AyudaEnPython")
        self.form = Form(self)
        self.form.calcular.config(command=self.calcular)
        self.form.clear.config(command=self.clear)
        self.form.pack()
        self.ubicacion = Label(self, text="")
        self.ubicacion.pack()
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(
            side="bottom", fill="both", expand=True,
        )

    def calcular(self) -> None:
        try:
            self.r = float(self.form.r.get())
            self.p = Punto(float(self.form.x.get()), float(self.form.y.get()))
            self.c = Circulo(
                Punto(float(self.form.h.get()), float(self.form.k.get())),
                self.r,
            )
            self.ubicacion.config(text=self.c.posicion_punto(self.p))
            self.plot()
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numericos")

    def clear(self) -> None:
        self.form.clear_form()
        self.ax.clear()
        self.canvas.draw()

    def plot(self) -> None:
        self.ax.add_patch(Rectangle(
            (self.c.x - self.r, self.c.y - self.r),
            2 * self.r, 2 * self.r, color="g", fill=False,
        ))
        self.ax.add_artist(plt.Circle(
            (self.c.x, self.c.y), self.r, color="b", fill=False,
        ))
        self.ax.set_aspect(1)
        self.ax.scatter(self.p.x, self.p.y, c="r")
        self.canvas.draw()


if __name__ == "__main__":
    app = App()
    app.mainloop()
