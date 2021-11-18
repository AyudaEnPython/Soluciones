"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado Original -------------------------
Usando tkinter implementar. Un sensor de temperatura de un criadero de 
truchas, toma lecturas de agua (grados centígrados) y el nivel de ruido
(decibelios) todos lo meses y los almacena en una matriz de orden 12x2.
Construyda un programa que determine mensualmente los valores promedios
y mínimos y máximos del sensor de temperatura y de ruido. NOTA 1:
Mostrar los resultados en un edit text.
# ---------------------------------------------------------------------

NOTE: El enunciado original no es muy claro y tiene errores
    ortográficos.
"""
import numpy as np
from dataclasses import dataclass, field
from tkinter import Button, Frame, Text, Tk
from typing import Tuple


T_MIN, T_MAX = 5, 20
R_MIN, R_MAX = 50, 70


def calcular(arr: np.ndarray, i: int) -> Tuple[float]:
    return (
        np.min(arr[:, i]),
        np.max(arr[:, i]),
        np.mean(arr[:, i], axis=0),
    )


@dataclass
class Sensor:
    temperatura: float = field(default=0.0)
    ruido: float = field(default=0.0)

    def __post_init__(self):
        self.temperatura = np.random.uniform(low=T_MIN, high=T_MAX, size=30)
        self.ruido = np.random.uniform(low=R_MIN, high=R_MAX, size=30)

    def data(self):
        return np.stack((self.temperatura, self.ruido), axis=1)


class App(Frame):

    def __init__(self) -> None:
        self.root = Tk()
        self.widgets()

    def widgets(self) -> None:
        self.btn_clear = Button(self.root, text="Clear", command=self.clear)
        self.btn_load = Button(self.root, text="Load", command=self.calcular)
        self.txt_data = Text(self.root, width=28, height=25)
        self.btn_load.grid(row=0, column=0, sticky="we")
        self.btn_clear.grid(row=0, column=1, sticky="we")
        self.txt_data.grid(row=1, column=0, columnspan=2)

    def calcular(self) -> None:
        self.txt_data.insert("end", f"{'Min':>12}{'Max':>7}{'Mean':>7}\n")
        for i in range(1, 13):
            sensor = Sensor()
            for j in range(2):
                min_, max_, mean = calcular(sensor.data(), j)
                i = i if j == 0 else " "
                j = "°C" if j == 0 else "dB"
                self.txt_data.insert(
                    "end",
                    f"{i:>2} {j} {min_:>6.2f} {max_:>6.2f} {mean:>6.2f}\n",
                )

    def clear(self) -> None:
        self.txt_data.delete("1.0", "end")

    def run(self) -> None:
        self.root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()