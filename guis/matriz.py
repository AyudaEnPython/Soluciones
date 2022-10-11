"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñar en tkinter las opciones de crear matrices con dimensiones
especificas, y en un combo mostrar las opciones con matrices.
"""
from dataclasses import dataclass
from tkinter import Tk, Button, Label, Frame, ttk, Text, Entry
from random import randint
from operator import add, sub, mul, truediv
from typing import List


MIN, MAX = 1, 20
ACTION = {
    "sumar": add,
    "restar": sub,
    "multiplicar": mul,
    "dividir": truediv,
}


def draw_matrix(matrix: List[List[float]]) -> None:
    row = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            row += f"{matrix[i][j]:>6}"
        row += "\n"
    return row


@dataclass
class Matrix:
    m: int
    n: int

    def __post_init__(self) -> None:
        self.arr = [
            [randint(MIN, MAX) for _ in range(self.n)] for _ in range(self.m)
        ]

    def sol(self, action: str, other: object) -> List[List[float]]:
        try:
            return [[
                ACTION[action](self.arr[i][j], other.arr[i][j])
                for j in range(self.n)
            ] for i in range(self.m)]
        except ZeroDivisionError:
            print("No se puede dividir por 0")

    def __str__(self) -> str:
        return draw_matrix(self.arr)


class Display(Frame):

    def __init__(self, master) -> None:
        super().__init__(master)
        self.setup_ui()

    def setup_ui(self):
        self.upper = Text(self, width=40, height=12)
        self.upper.pack(side="top", fill="both", expand=True)
        self.lower = Text(self, width=40, height=6)
        self.lower.pack(side="bottom", fill="both", expand=True)

    def write_upper(self, a: str, b: str) -> None:
        self.upper.delete("1.0", "end")
        self.upper.insert("1.0", a)
        self.upper.insert("1.0", "\n")
        self.upper.insert("1.0", b)

    def write_lower(self, text: str) -> None:
        self.lower.delete("1.0", "end")
        self.lower.insert("1.0", text)

    def clear(self, pos: str) -> None:
        if pos == "upper":
            self.upper.delete("1.0", "end")
        elif pos == "lower":
            self.lower.delete("1.0", "end")


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("Ayuda en Python")
        self.left = Frame(self)
        self.right = Frame(self)
        self.left.pack(side="left", fill="both", expand=True)
        self.right.pack(side="right", fill="both", expand=True)
        self.setup_ui()

    def setup_ui(self):
        Label(self.left, text="M").grid(row=0, column=0)
        self.m = Entry(self.left, width=3)
        self.m.grid(row=0, column=1)
        Label(self.left, text="N").grid(row=1, column=0)
        self.n = Entry(self.left, width=3)
        self.n.grid(row=1, column=1)
        self.create_matrix = Button(
            self.left, text="Crear", command=self.create
        )
        self.create_matrix.grid(row=2, columnspan=2)
        self.combo = ttk.Combobox(
            self.left, values=tuple(ACTION.keys()), state="readonly"
        )
        self.combo.grid(row=3, columnspan=2)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.on_combo_changed)
        self.display = Display(self.right)
        self.display.grid(row=0, column=0)

    def create(self):
        self.matrix = []
        for _ in range(2):
            self.matrix.append(Matrix(int(self.m.get()), int(self.n.get())))
        self.display.write_upper(str(self.matrix[0]), str(self.matrix[1]))

    def on_combo_changed(self, event):
        self.display.write_upper(str(self.matrix[0]), str(self.matrix[1]))
        self.display.write_lower(
            draw_matrix(
                self.matrix[0].sol(self.combo.get(), self.matrix[1])
            )
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
