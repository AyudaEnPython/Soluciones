"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import (
    Button,
    Entry,
    Frame,
    Label,
    Radiobutton,
    StringVar,
    ttk,
    Text,
)

from constants import Data, DataList, MOVIES, CFG, DIAS, LABELS, MAP


def read_file(filename: str) -> DataList:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


class Login(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self) -> None:
        Label(self, text="Usuario").pack(**CFG)
        self.user = Entry(self)
        self.user.pack()
        Label(self, text="Contraseña").pack(**CFG)
        self.password = Entry(self, show="*")
        self.password.pack(**CFG)
        self.login = Button(self, text="Iniciar sesión")
        self.login.pack(fill="x", **CFG)
        self.quit = Button(self, text="Salir", command=self.master.destroy)
        self.quit.pack(fill="x", **CFG)

    def clear(self):
        self.user.delete(0, "end")
        self.password.delete(0, "end")
        self.user.focus_set()


class Sales(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self._currency = StringVar()
        self._currency.set("local")
        self.create_widgets()

    def create_widgets(self) -> None:
        for i, label in enumerate(LABELS):
            Label(self, text=label).grid(row=i, column=0, sticky="e", **CFG)
        self.ent_id = Entry(self)
        self.ent_quantity = Entry(self)
        self.cbx_days = ttk.Combobox(self, values=DIAS)
        self.cbx_movies = ttk.Combobox(self, values=read_file(MOVIES))
        self.btn_pay_local = Button(self, text="Pagar en moneda local")
        self.btn_pay_foreign = Button(self, text="Pagar en moneda extranjera")
        self.rbn_local = Radiobutton(
            self, text="Local", variable=self._currency, value="local",
        )
        self.rbn_foreign = Radiobutton(
            self, text="Extranjera", variable=self._currency, value="foreign",
        )
        self.btn_calculate = Button(self, text="Calcular")
        self.btn_clear = Button(self, text="Limpiar", command=self.clear)
        self.display = Text(self, height=1, width=32, state="disabled")
        self.ent_id.grid(row=0, column=1, sticky="we", **CFG)
        self.ent_quantity.grid(row=1, column=1, sticky="we", **CFG)
        self.cbx_days.grid(row=2, column=1, sticky="we", **CFG)
        self.cbx_movies.grid(row=3, column=1, sticky="we", **CFG)
        self.rbn_local.grid(row=5, column=0, sticky="we")
        self.rbn_foreign.grid(row=5, column=1, sticky="we")
        self.btn_calculate.grid(row=7, column=0, pady=5)
        self.btn_clear.grid(row=7, column=1, pady=5)
        self.display.grid(row=8, column=0, columnspan=2, pady=5)

    def update_display(self, text: str) -> None:
        self.display.config(state="normal")
        self.display.delete("1.0", "end")
        self.display.insert("end", text)
        self.display.config(state="disabled")

    def clear_display(self) -> None:
        self.display.config(state="normal")
        self.display.delete("1.0", "end")
        self.display.config(state="disabled")

    def clear(self):
        self._currency.set("local")
        self.clear_display()
        self.ent_id.delete(0, "end")
        self.ent_quantity.delete(0, "end")
        self.cbx_days.delete(0, "end")
        self.cbx_movies.delete(0, "end")
        self.ent_id.focus_set()


class Query(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self._q = StringVar()
        self._q.set("id")
        self.create_widgets()

    def create_widgets(self) -> None:
        Label(self, text="Ingresar consulta").grid(
            row=0, column=0, sticky="we",
        )
        self.ent_query = Entry(self)
        self.rbn_day = Radiobutton(
            self, text="Por dia", variable=self._q, value="dia",
        )
        self.rbn_id = Radiobutton(
            self, text="Por identificación", variable=self._q, value="id",
        )
        self.btn_search = Button(self, text="Consultar")
        self.ent_query.grid(row=1, column=0, pady=15, sticky="we")
        self.rbn_id.grid(row=2, column=0, padx=15, sticky="w")
        self.rbn_day.grid(row=3, column=0, padx=15, sticky="w")
        self.btn_search.grid(row=4, column=0, pady=15)


class Result(Frame):

    def __init__(self, master=None) -> None:
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self) -> None:
        labels = tuple(MAP.values())
        self.view = ttk.Treeview(self, columns=labels, show="headings")
        for label in labels:
            self.view.heading(label, text=label)
        self.view.grid(row=0, column=0, sticky="w", **CFG)

    def update(self, data: Data) -> None:
        self.view.delete(*self.view.get_children())
        for row in data:
            self.view.insert("", "end", values=row)
