"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Mockup, not functional yet (more information needed)
"""
import datetime
from dataclasses import dataclass, field
from tkinter import Label, Entry, StringVar, Tk, Frame


def _today_date():
    return datetime.date.today().strftime("%d/%m/%Y")


@dataclass
class Formulario:
    fecha: str
    turno: int
    hora_inicial: str
    hora_final: str
    jefe_turno: str
    maquinaria: str
    preforma: str
    envase: str
    produccion_total: str
    produccion_conforme: str = field(init=False)

    def __post_init__(self):
        desperdicio = float(self.preforma) + float(self.envase)
        conforme = float(self.produccion_total) - desperdicio
        self.produccion_conforme = str(conforme)


class Widget(Frame):

    def __init__(self, master, turno):
        super().__init__(master)
        self.turno = turno
        self.fecha = StringVar()
        self.hora_inicial = StringVar()
        self.hora_final = StringVar()
        self.setup_ui()

    def setup_ui(self):
        Label(self, text=f"Turno {self.turno}").grid(row=0, column=0)
        Label(self, text=f"Fecha: {_today_date()}").grid(row=0, column=1)
        Label(self, text="Hora inicial").grid(row=1, column=0)
        self.ent_hora_inicial = Entry(self, textvariable=self.hora_inicial)
        self.ent_hora_inicial.grid(row=1, column=1)
        Label(self, text="Hora final").grid(row=2, column=0)
        self.ent_hora_final = Entry(self, textvariable=self.hora_final)
        self.ent_hora_final.grid(row=2, column=1)
        Label(self, text="Jefe de turno").grid(row=3, column=0)
        self.ent_jefe_turno = Entry(self)
        self.ent_jefe_turno.grid(row=3, column=1)
        Label(self, text="Maquinaria").grid(row=4, column=0)
        self.ent_maquinaria = Entry(self)
        self.ent_maquinaria.grid(row=4, column=1)
        Label(self, text="Nombre de la Referencia").grid(row=5, column=0)
        Label(self, text="P.T.").grid(row=6, column=0)
        self.ent_pt = Entry(self)
        self.ent_pt.grid(row=6, column=1)
        Label(self, text="M.P.").grid(row=7, column=0)
        self.ent_mp = Entry(self)
        self.ent_mp.grid(row=7, column=1)
        Label(self, text="Produccion Turno").grid(row=8, column=0)
        Label(self, text="Desperdicio Preforma").grid(row=9, column=0)
        self.ent_preforma = Entry(self)
        self.ent_preforma.grid(row=9, column=1)
        Label(self, text="Desperdicio Envase").grid(row=10, column=0)
        self.ent_envase = Entry(self)
        self.ent_envase.grid(row=10, column=1)
        Label(self, text="Produccion Total").grid(row=11, column=0)
        self.ent_produccion_total = Entry(self)
        self.ent_produccion_total.grid(row=11, column=1)
        Label(self, text="Produccion Conforme").grid(row=12, column=0)
        self.ent_produccion_conforme = Entry(self)
        self.ent_produccion_conforme.grid(row=12, column=1)


class App(Tk):

    def __init__(self):
        super().__init__()
        self.widgets = []
        self.setup()

    def setup(self):
        Label(
            self,
            text="Arranque de Producción Máquina y control de eficiencia",
        ).grid(row=0, columnspan=3)
        for n in range(3):
            w = Widget(self, n + 1)
            w.grid(row=1, column=n, padx=15, pady=15)
            self.widgets.append(w)


if __name__ == "__main__":
    app = App()
    app.mainloop()
