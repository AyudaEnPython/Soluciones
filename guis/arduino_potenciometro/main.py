"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: el potenciometro esta simulado a traves de un slider.
"""
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Scale


class Potenciometro:

    def __init__(self):
        self.root = Tk()
        self.fig, self.ax = plt.subplots()
        self.data = deque(maxlen=10)
        self.widgets()
        self.plot()

    def widgets(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side="left", fill="both")
        self.slider = Scale(
            self.root, from_=6, to=0, resolution=0.1, orient="vertical"
        )
        self.slider.pack(fill="both", expand=True)

    def plot(self):
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 6)
        self.ax.grid(True)
        self.line, = self.ax.plot(
            [], [], lw=2, color='red', label='Potenciómetro'
        )
        self.ani = animation.FuncAnimation(
            self.fig, self.update, interval=100, blit=True)

    def get_data_from_serial_port(self):
        """Modificar por el puerto serial que se utilice"""
        return self.slider.get()

    def update(self, _):
        self.data.append(self.get_data_from_serial_port())
        self.line.set_data(range(len(self.data)), self.data)
        return self.line,

    def run(self):
        self.root.title("Ayuda En Python")
        self.root.resizable(False, False)
        self.root.mainloop()


if __name__ == "__main__":
    app = Potenciometro()
    app.run()
