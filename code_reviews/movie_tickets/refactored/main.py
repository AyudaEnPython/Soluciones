"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import tkinter as tk

from invoice import Invoice, Search
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
        user = self.login.user.get()
        password = self.login.password.get()
        if user == "admin" and password == "admin":
            self.login.destroy()
            self.show_sales()
        else:
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
            tk.messagebox.showerror("Error", "Datos erróneos")
            self.sales.clear()

    def get_data(self) -> None:
        search = Search()
        ok, data = search.get_by(
            self.query._q.get(), self.query.ent_query.get(),
        )
        if ok:
            self.show_query()
            self.result.update(data)
        else:
            tk.messagebox.showerror("Error", "Datos no disponiibles")


if __name__ == "__main__":
    app = App()
    app.mainloop()
