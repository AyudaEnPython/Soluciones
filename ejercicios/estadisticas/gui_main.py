"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: needs to review, add buttons to generate new data
"""
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import Label, Tk


def load_data():
    return np.random.randint(0, 10, size=20)


class Plotter(Tk):

    def __init__(self, ser: pd.Series) -> None:
        super().__init__()
        self.title("Ayuda en Python")
        self.ser = ser
        self.figures = []
        self.setup_ui()

    def setup_ui(self) -> None:
        Label(self, text=f"Mean {self.ser.mean()}").grid(row=0, column=0)
        Label(self, text=f"Mode {self.ser.mode()}").grid(row=0, column=1)
        Label(self, text=f"Median {self.ser.median()}").grid(row=0, column=2)
        for i, type_ in enumerate(("bar", "pie")):
            fig = Figure(figsize=(3, 3), dpi=80)
            fig_ = self.ser.value_counts().plot(
                kind=type_, ax=fig.add_subplot(111),
            ).get_figure()
            canvas = FigureCanvasTkAgg(fig_, self)
            canvas.get_tk_widget().grid(row=1, column=i, padx=5, pady=5)
            self.figures.append(fig_)
        fig = Figure(figsize=(2, 3), dpi=80)
        fig_ = self.ser.quantile([0.25, 0.5, 0.75]).plot(
            kind="box", ax=fig.add_subplot(111),
        ).get_figure()
        canvas = FigureCanvasTkAgg(fig_, self)
        canvas.get_tk_widget().grid(row=1, column=2, padx=5, pady=5)
        self.figures.append(fig_)


if __name__ == "__main__":
    data = load_data()
    plotter = Plotter(pd.Series(data))
    plotter.mainloop()
