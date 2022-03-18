"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import json
import tkinter as tk
from tkinter import messagebox

from invoice import Invoice, Search
from constants import CREDENTIALS, Token
from widgets import Login, Sales, Query, Result


class App(tk.Tk):
    
    def __init__(self) -> None:
        super().__init__()
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")
        self.login = Login(self)
        self.login.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.login.login.config(command=self.is_authorized)
    
    def is_authorized(self) -> None:
        token = self._read_json(CREDENTIALS)
        user = self.login.user.get()
        password = self.login.password.get()
        if token["user"] == user and token["password"] == password:
            self.login.destroy()
            self.show_sales()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
            self.login.clear()

    def show_sales(self) -> None:
        self.sales = Sales(self.container)
        self.query = Query(self.container)
        self.sales.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.query.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        self.sales.btn_calculate.config(command=self.calculate_sales)
        self.query.btn_search.config(command=self.get_data)

    def show_query(self) -> None:
        self.window = tk.Toplevel(self.container)
        self.window.title("Resultados")
        self.result = Result(self.window)
        self.result.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def calculate_sales(self) -> None:
        try:
            invoice = Invoice(
                self.sales.ent_id.get(),
                int(self.sales.ent_quantity.get()),
                self.sales.cbx_days.get(),
                self.sales.cbx_movies.get(),
                self.sales._currency.get(),
            )
            text = f"Total a pagar: {invoice.get_price()}"
            self.sales.update_display(text)
            invoice.to_csv()
        except ValueError:
            messagebox.showerror("Error", "Datos erróneos")
            self.sales.clear()

    def get_data(self) -> None:
        search = Search()
        tag = self.query._q.get()
        query = self.query.ent_query.get()
        if query == "":
            messagebox.showerror("Error", "Consulta errónea")
        else:
            ok, data = search.get_by(tag, query)
            if ok:
                self.show_query()
                self.result.update(data)
            else:
                messagebox.showerror("Error", "Datos no disponiibles")

    def _read_json(self, filename: str) -> Token:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    app = App()
    app.mainloop()
