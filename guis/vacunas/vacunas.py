"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Label, Entry, Button, Text


class Vacunas:

    STOCK = 5_000_000
    MARCAS = "pfizer", "moderna", "aztraseneca"

    def __init__(self) -> None:
        self.root = Tk()
        self.widgets()
        self.layouts()

    def widgets(self):
        for i, marcas in enumerate(self.MARCAS):
            Label(self.root, text=marcas).grid(row=i, column=0)
        self.pfizer = Entry(self.root)
        self.moderna = Entry(self.root)
        self.aztra = Entry(self.root)
        self.btn_calcular = Button(self.root, text="Calcular", command=self.f)
        self.text_box = Text(self.root, width=28, height=6)

    def layouts(self):
        self.pfizer.grid(row=0, column=1, padx=5, pady=5)
        self.moderna.grid(row=1, column=1, padx=5, pady=5)
        self.aztra.grid(row=2, column=1, padx=5, pady=5)
        self.btn_calcular.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.text_box.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def mayor(self, datos):
        mayor = 0
        for k, v in datos.items():
            if v > mayor:
                mayor = v
                marca = k
        return marca

    def f(self):
        self.text_box.delete(1.0, "end")
        a, b, c = self.pfizer.get(), self.moderna.get(), self.aztra.get()
        vacunas = {k: v for k, v in zip(self.MARCAS, (int(a), int(b), int(c)))}
        mas_aplicada = self.mayor(vacunas)
        for marcas in self.MARCAS:
            self.text_box.insert(
                "end",
                f"{marcas:>14}: {vacunas[marcas]:>11}\n",
            )
        self.text_box.insert(
            "end",
            f"{'Aplicadas: ':>16}{sum(vacunas.values()):>11}\n",
        )
        self.text_box.insert(
            "end",
            f"{'Disponibles: ':>16}{self.STOCK - sum(vacunas.values()):>11}\n",
        )
        self.text_box.insert(
            "end",
            f"{'Mas aplicada: ':>16}{mas_aplicada:>11}\n",
        )

    def run(self):
        self.root.title("Ayuda en Python")
        self.root.geometry("240x240")
        self.root.mainloop()


if __name__ == "__main__":
    app = Vacunas()
    app.run()
