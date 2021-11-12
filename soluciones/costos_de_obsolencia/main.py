"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa para calcular los costos de obsolescencia de 8
piezas de una maquinaria al cabo de 6 meses, conociendo que el
deterioro representa el 2% mensual respecto al periodo anterior.

Presentar el proceso de obsolescencia en un cuadro.
Utilizar el costo inicial simulado según criterio.


    +-------------+---------+-----------------------+--------+
    |             | Precio  | Obsolescencia Mensual | Precio |
    | Descripcion | Inicial |---+---+---+---+---+---| Final  |
    |             |         | 1 | 2 | 3 | 4 | 5 | 6 |        |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 1     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 2     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 3     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 4     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 5     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 6     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 7     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
    | Pieza 8     | S/.     |   |   |   |   |   |   | S/.    |
    +-------------+---------+---+---+---+---+---+---+--------+
                Obsolescencia: 2% periodo anterior.

Realizar la representación grafica comparativa en columnas.

        ^
        |     |
    P   |     |       |           |
    R   |     | *     |   |       |   |
    E   | |   | * |   | * |   |   | * | 
    C   | | * | * |	  | * |   | * | * | *
    I   | | * | * | * | * | * | * | * | *
    O   | | * | * | * | * | * | * | * | *
        | | * | * | * | * | * | * | * | *  
        +--------------------------------->
            P R O D U C T O S

TODO: needs to be refactored
"""
import pandas as pd
from dataclasses import dataclass, field
from tkinter import Tk, ttk, Frame, Label, Button, Entry, END

from utils import calcular, plot_comparativa


@dataclass
class Process:
    initial_serie: list
    final_serie: list = field(init=False)

    def __post_init__(self):
        self.data = calcular(self.initial_serie)
        self.final_serie = self.data[-1]

    def dataframe(self):
        x, y = self.data
        df = pd.DataFrame(x, columns=[str(i) for i in range(1, 9)])
        return df.round(2)


class App(Frame):

    def __init__(self):
        self.root = Tk()
        self.data = None
        self.initial_serie = [0 for _ in range(8)]
        self.final_serie = [0 for _ in range(8)]
        self.entries = {}
        self.widgets()
        self.layout()

    def widgets(self):
        self.treeview = ttk.Treeview(
            self.root,
            columns=("Inicial", "Obsolescencia", "Final"),
            height=15,
        )
        for i in range(8):
            Label(
                self.root,
                text=f"Pieza {i+1}").grid(
                    row=i, column=0, sticky="e", padx=5, pady=5,
                )
        for i in range(1, 9):
            self.entries[i] = Entry(self.root, width=15)
        self.btn_result = Button(
            self.root,
            text="Calcular",
            command= lambda: self._get_data(),
        )
        self.brn_clear = Button(
            self.root,
            text="Limpiar",
            command= lambda: self._clear_data(),
        )
        self.btn_plot = Button(
            self.root,
            text="Mostrar comparativa",
            command= lambda: plot_comparativa(
                self.initial_serie, self.final_serie,
            )
        )

    def layout(self):
        for i in range(8):
            self.entries[i+1].grid(row=i, column=1, padx=5, pady=5)
        self.btn_result.grid(row=8, column=0, padx=5,pady=5, sticky="ew")
        self.brn_clear.grid(row=8, column=1, padx=5,pady=5, sticky="we")
        self.btn_plot.grid(row=9, columnspan=2, padx=5, pady=5)
        self.treeview.grid(row=0, rowspan=10, column=2, padx=5, pady=5)
        self.treeview.heading("#0", text="Descripción")
        self.treeview.column("#0", width=80, anchor="center")
        self.treeview.heading("#1", text="Inicial")
        self.treeview.column("#1", width=60, anchor="center")
        self.treeview.heading("#2", text="Obsolescencia Mensual")
        self.treeview.column("#2", width=360, anchor="center")
        self.treeview.heading("Final", text="Final")
        self.treeview.column("Final", width=60, anchor="center")

    def _clear_data(self):
        for i in range(1, 9):
            self.entries[i].delete(0, 'end')
        self.treeview.delete(*self.treeview.get_children())

    def _get_data(self):
        self.data = [float(self.entries[i].get()) for i in range(1, 9)]
        p = Process(self.data)
        self.df = p.dataframe()
        self.initial_serie = p.initial_serie
        self.final_serie = p.final_serie
        self._df_to_treeview()

    def _df_to_treeview(self):
        self.treeview.delete(*self.treeview.get_children())
        for i in range(8):
            data = []
            data.append(self.initial_serie[i])
            data.append(self.df.iloc[i].values)
            data.append(self.df.iloc[i].values[-1])
            self.treeview.insert("", END, text=f"Pieza {i+1}", values=data)

    def run(self):
        self.root.geometry("760x350")
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()