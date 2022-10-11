"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Partially functional (more information needed)
"""
import datetime
from dataclasses import dataclass, field
from tkinter import Button, Entry, Frame, Label, Text, Toplevel, Tk, ttk


def _today_date():
    return datetime.date.today().strftime("%d/%m/%Y")


@dataclass
class Formulario:
    fecha: str
    turno: int
    hora_inicial: str = field(default="00:00")
    hora_final: str = field(default="00:00")
    jefe_turno: str = ""
    maquinaria: str = ""
    preforma: str = ""
    envase: str = ""
    produccion_total: str = ""
    total_desperdicio: str = field(init=False)
    produccion_conforme: str = field(init=False)

    def __post_init__(self):
        try:
            desperdicio = float(self.preforma) + float(self.envase)
            conforme = float(self.produccion_total) - desperdicio
            self.total_desperdicio = str(desperdicio)
            self.produccion_conforme = str(conforme)
        except ValueError:
            self.total_desperdicio = "0"
            self.produccion_conforme = "0"

    def to_str(self):
        return (
            f"Fecha: {self.fecha}\n"
            f"Turno: {self.turno}\n"
            f"Hora inicial: {self.hora_inicial}\n"
            f"Hora final: {self.hora_final}\n"
            f"Jefe turno: {self.jefe_turno}\n"
            f"Maquinaria: {self.maquinaria}\n"
            f"Preforma: {self.preforma}\n"
            f"Envase: {self.envase}\n"
            f"Producción total: {self.produccion_total}\n"
            f"Total desperdicio: {self.total_desperdicio}\n"
            f"Producción conforme: {self.produccion_conforme}\n"
        )


class Widget(Frame):

    def __init__(self, master, turno):
        super().__init__(master)
        self.turno = turno
        self.setup_ui()
        for widget in self.winfo_children():
            widget.grid_configure(padx=5, pady=5)

    def setup_ui(self):
        Label(self, text="Hora inicial").grid(row=1, column=0, sticky="e")
        self.ent_hora_inicial = Entry(self)
        self.ent_hora_inicial.grid(row=1, column=1)
        Label(self, text="Hora final").grid(row=2, column=0, sticky="e")
        self.ent_hora_final = Entry(self)
        self.ent_hora_final.grid(row=2, column=1)
        Label(self, text="Jefe de turno").grid(row=3, column=0, sticky="e")
        self.ent_jefe_turno = Entry(self)
        self.ent_jefe_turno.grid(row=3, column=1)
        Label(self, text="Maquinaria").grid(row=4, column=0, sticky="e")
        self.ent_maquinaria = Entry(self)
        self.ent_maquinaria.grid(row=4, column=1)
        Label(self, text="Nombre de la Referencia").grid(row=5, columnspan=2)
        Label(self, text="P.T.").grid(row=6, column=0, sticky="e")
        self.ent_pt = Entry(self)
        self.ent_pt.grid(row=6, column=1)
        Label(self, text="M.P.").grid(row=7, column=0, sticky="e")
        self.ent_mp = Entry(self)
        self.ent_mp.grid(row=7, column=1)
        Label(self, text="Produccion Turno").grid(row=8, columnspan=2)
        Label(self, text="Desperdicio Preforma").grid(
            row=9, column=0, sticky="e"
        )
        self.ent_preforma = Entry(self)
        self.ent_preforma.grid(row=9, column=1)
        Label(self, text="Desperdicio Envase").grid(
            row=10, column=0, sticky="e"
        )
        self.ent_envase = Entry(self)
        self.ent_envase.grid(row=10, column=1)
        Label(self, text="Produccion Total").grid(
            row=11, column=0, sticky="e"
        )
        self.ent_produccion_total = Entry(self)
        self.ent_produccion_total.grid(row=11, column=1)

    def calcular(self):
        formulario = Formulario(
            fecha=_today_date(),
            turno=self.turno,
            hora_inicial=self.ent_hora_inicial.get(),
            hora_final=self.ent_hora_final.get(),
            jefe_turno=self.ent_jefe_turno.get(),
            maquinaria=self.ent_maquinaria.get(),
            preforma=self.ent_preforma.get(),
            envase=self.ent_envase.get(),
            produccion_total=self.ent_produccion_total.get(),
        )
        self.f = formulario
        return (
            float(self.f.total_desperdicio),
            float(self.f.produccion_conforme),
        )

    def informe(self):
        display = Toplevel()
        display.title("Informe")
        w = Text(display, width=36, height=12)
        w.insert("end", self.f.to_str())
        w.config(state="disabled")
        w.pack()

    def limpiar(self):
        self.ent_hora_inicial.delete("0", "end")
        self.ent_hora_final.delete("0", "end")
        self.ent_jefe_turno.delete("0", "end")
        self.ent_maquinaria.delete("0", "end")
        self.ent_preforma.delete("0", "end")
        self.ent_envase.delete("0", "end")
        self.ent_produccion_total.delete("0", "end")


class Container(Frame):

    def __init__(self, master, turno):
        super().__init__(master)
        self.N = 3
        self.widgets = []
        self.turno = turno
        Label(self, text=f"Turno {self.turno}").grid(
            row=0, column=0, sticky="w"
        )
        Label(self, text=f"Fecha: {_today_date()}").grid(row=0, column=1)
        self.setup_ui()

    def setup_ui(self):
        for n in range(self.N):
            w = Widget(self, n + 1)
            w.grid(row=1, column=n, padx=15, pady=15)
            self.widgets.append(w)
        self.btn_calcular = Button(
            self, text="Calcular", bg="#EFDAD7", command=self.calcular
        )
        self.btn_calcular.grid(row=12, column=0)
        self.btn_limpiar = Button(
            self, text="Limpiar", bg="#EFDAD7", command=self.limpiar
        )
        self.btn_limpiar.grid(row=12, column=1)
        self.btn_informe = Button(
            self, text="Informe", bg="#EFDAD7", command=self.informe
        )
        self.btn_informe.grid(row=12, column=2)
        self.lbf_informe = ttk.LabelFrame(self)
        self.lbf_informe.grid(row=13, columnspan=self.N, sticky="we")
        Label(self.lbf_informe, text="Total de desperdicio").grid(
            row=0, column=0,
        )
        self.lbl_total_desperdicio = Label(self.lbf_informe, text="")
        self.lbl_total_desperdicio.grid(row=0, column=1)
        Label(self.lbf_informe, text="Producción Conforme").grid(
            row=1, column=0,
        )
        self.lbl_produccion_conforme = Label(self.lbf_informe, text="")
        self.lbl_produccion_conforme.grid(row=1, column=1)

    def calcular(self):
        data = []
        for w in self.widgets:
            data.append(w.calcular())
        desperdicio, produccion_conforme = zip(*data)
        self.lbl_total_desperdicio.config(text=sum(desperdicio))
        self.lbl_produccion_conforme.config(text=sum(produccion_conforme))

    def informe(self):
        for w in self.widgets:
            w.informe()

    def limpiar(self):
        for w in self.widgets:
            w.limpiar()


class App(Tk):

    def __init__(self, N):
        super().__init__()
        self.widgets = []
        self.N = N
        self.setup()

    def setup(self):
        Label(
            self,
            text="Arranque de Producción Máquina y control de eficiencia",
        ).grid(row=0, columnspan=self.N)
        for n in range(self.N):
            w = Container(self, n + 1)
            w.grid(row=n, column=0, padx=15, pady=15)
            self.widgets.append(w)


if __name__ == "__main__":
    app = App(N=2)
    app.mainloop()
