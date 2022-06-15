"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Usando tkinter implementar. Construya un programa que me permita crear
una matriz de dimensión nxn con datos enteros aleatorios de 0 a 50 y
que me de 2 opciones, "derecha" significa que la última columna pasa a
ser primera. "arriba" significa que la última fila pasa a ser la
primera fila. NOTA1: Recordar que no se pierden los datos, solo se
cambian filas y columnas según sea el caso. NOTA2: Puede mostrar la
matriz original y el resultado en el shell o en interfaz.
NOTA3: n > 4

Usando tkinter implementar. Construya un programa que me permita crear
una matriz de dimensión nxn con datos enteros aleatorios de 0 a 50 y
que lo ordene las columnas pares en orden ascendente y las impares en
forma descendente. Mostrar la matriz original y la resultante. NOTA1:
Puede mostrar la matriz original y la resultante resultado en el shell
o en interfaz.
NOTA2: n > 4 y n es par
# ---------------------------------------------------------------------

NOTE: El enunciado original tiene demasiados errores ortográficos.
    Ambos ejercicios se pueden realizar en una sola aplicación.
"""
import numpy as np
from dataclasses import dataclass
from tkinter import Button, Entry, Frame, Label, Text, Tk

MIN, MAX = 0, 50


@dataclass
class Matrix:
    m: int
    n: int
    
    def __post_init__(self) -> None:
        self.arr = np.random.randint(MIN, MAX, size=(self.m, self.n))
        self.copy = self.arr.copy()

    def revert(self) -> None:
        self.arr = self.copy

    def shift_right(self) -> None:
        self.arr = np.roll(self.arr, 1, axis=1)

    def shift_up(self) -> None:
        self.arr = np.roll(self.arr, 1, axis=0)

    def sort_even_odd(self) -> None:
        even_cols = self.arr[:, ::2]
        odd_cols = self.arr[:, 1::2]
        even_cols.sort(axis=0)
        odd_cols[::-1].sort(axis=0)
        self.arr[:, ::2] = even_cols
        self.arr[:, 1::2] = odd_cols

    def __str__(self) -> str:
        return str(self.arr)


class App(Frame):

    def __init__(self) -> None:
        self.root = Tk()
        self.matrix = None
        self.widgets()
        self.layout()
    
    def widgets(self) -> None:
        self.lbl_m = Label(self.root, text="M")
        self.lbl_n = Label(self.root, text="N")
        self.ent_m = Entry(self.root, width=3)
        self.ent_n = Entry(self.root, width=3)
        self.text = Text(self.root, width=20, height=10)
        self.btn_show = Button(self.root, text="Show", command=self.show)
        self.btn_right = Button(self.root, text="Derecha", command=self.right)
        self.btn_up = Button(self.root, text="Arriba", command=self.up)
        self.btn_sort = Button(self.root, text="Ordenar", command=self.sort)

    def layout(self):
        self.btn_show.grid(row=0, column=4, sticky="we")
        self.lbl_m.grid(row=0, column=0, sticky="e")
        self.ent_m.grid(row=0, column=1, sticky="w")
        self.lbl_n.grid(row=0, column=2, sticky="e")
        self.ent_n.grid(row=0, column=3, sticky="w")
        self.text.grid(row=1, column=0, columnspan=5)
        self.btn_right.grid(row=2, column=0, columnspan=2, sticky="we")
        self.btn_up.grid(row=2, column=2, columnspan=2, sticky="we")
        self.btn_sort.grid(row=2, column=4, sticky="we")

    def right(self) -> None:
        self.matrix.shift_right()
        self._write()

    def up(self) -> None:
        self.matrix.shift_up()
        self._write()

    def sort(self) -> None:
        self.matrix.sort_even_odd()
        self._write()

    def show(self) -> None:
        self.matrix = Matrix(int(self.ent_m.get()), int(self.ent_n.get()))
        self._write()

    def _write(self) -> None:
        self.text.delete(1.0, "end")
        self.text.insert("end", f"Original:\n{self.matrix.copy}\n")
        self.text.insert("end", f"\nResultado:\n{self.matrix}")

    def run(self) -> None:
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
