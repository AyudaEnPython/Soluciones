"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Entry, Button

w, botones = [], []


def leer_datos(archivo="datos.txt"):
    with open(archivo, "r", encoding="utf-8") as f:
        return f.read()


def insertar_datos():
    w[0].insert("end", f"{leer_datos()}\n")


def limpiar():
    w[0].delete(0, "end")


def widgets(master):
    texto = Entry(master)
    texto.grid(row=0, column=0, columnspan=3, padx=5, pady=5)
    w.append(texto)
    for i, texto in enumerate(("Ver", "Limpiar", "Salir")):
        boton = Button(master, text=texto)
        boton.grid(row=1, column=i)
        botones.append(boton)


def config(master):
    botones[0].config(command=insertar_datos)
    botones[1].config(command=limpiar)
    botones[2].config(command=master.quit)


if __name__ == "__main__":
    root = Tk()
    widgets(root)
    config(root)
    root.mainloop()
