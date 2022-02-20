"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Label, Entry, Button, Text

STOCK = 5_000_000
MARCAS = "pfizer", "moderna", "aztraseneca"
entries, text_boxes = [], []


def mayor(datos):
    mayor = 0
    for k, v in datos.items():
        if v > mayor:
            mayor = v
            marca = k
    return marca


def f():
    text_boxes[0].delete(1.0, "end")
    a, b, c = entries[0].get(), entries[1].get(), entries[2].get()
    vacunas = {k:v for k, v in zip(MARCAS, (int(a), int(b), int(c)))}
    mas_aplicada = mayor(vacunas)
    for marcas in MARCAS:
        text_boxes[0].insert(
            "end",
            f"{marcas:>14}: {vacunas[marcas]:>11}\n",
        )
    text_boxes[0].insert(
        "end", f"{'Aplicadas: ':>16}{sum(vacunas.values()):>11}\n",
    )
    text_boxes[0].insert(
        "end", f"{'Disponibles: ':>16}{STOCK - sum(vacunas.values()):>11}\n",
    )
    text_boxes[0].insert(
        "end", f"{'Mas aplicada: ':>16}{mas_aplicada:>11}\n",
    )


def widgets(root):
    for i, marcas in enumerate(MARCAS):
        Label(root, text=marcas).grid(row=i, column=0)
        entries.append(Entry(root))
    for i, entry in enumerate(entries):
        entry.grid(row=i, column=1, padx=5, pady=5)
    Button(
        root, text="Calcular", command=f
    ).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    text_boxes.append(Text(root, width=28, height=6))
    text_boxes[0].grid(row=4, column=0, columnspan=2, padx=5, pady=5)


if __name__ == "__main__":
    app = Tk()
    app.title("Ayuda en Python")
    app.geometry("240x240")
    widgets(app)
    app.mainloop()
