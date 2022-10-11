from random import randint
from tkinter import Tk, Frame
from datetime import datetime, timedelta
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def cpu_percent():
    return randint(16, 35)


class CpuUsage(Frame):

    def __init__(self, master, points):
        super().__init__(master)
        self.figure = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M:%S"))
        date_t = datetime.now() + timedelta(seconds=-points)
        self.x_data = [date_t + timedelta(seconds=i) for i in range(points)]
        self.y_data = [0 for i in range(points)]
        self.plot = self.ax.plot(self.x_data, self.y_data, label='CPU')[0]
        self.ax.set_ylim(0, 100)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget(
            ).pack(side="bottom", fill="both", expand=True)
        self.animate()

    def animate(self):
        self.x_data.append(datetime.now())
        self.y_data.append(cpu_percent())
        self.x_data, self.y_data = self.x_data[1:], self.y_data[1:]
        self.plot.set_xdata(self.x_data)
        self.plot.set_ydata(self.y_data)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        self.canvas.draw_idle()
        self.after(1000, self.animate)


class MainWindwow(Tk):

    def __init__(self):
        super().__init__()
        CpuUsage(self, points=1000).pack()


if __name__ == "__main__":
    app = MainWindwow()
    app.mainloop()
