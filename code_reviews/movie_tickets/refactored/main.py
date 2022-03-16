from dataclasses import dataclass
from tkinter import Tk, Label, Button, Entry

MOVIES = (
    "El conjuro",
    "La noche del demonio",
    "Ouija",
    "Interestelar",
    "Cuando las luces se apagan",
    "La huerfana",
    "Hereditary",
    "Annabelle",
    "Cadaver",
    "El silencio",
    "Verdad o reto",
    "Doctor sueño",
    "Mamá",
    "Ma",
    "Descendientes",
    "El privilegio",
    "Sin respiro",
    "Perdona nuestras ofensas",
)
DAYS = (
    "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"
)

def read_file():
    ...


def write_file():
    ...


def _calculate():
    ...


def _validate():
    ...


@dataclass
class Boleto:
    ...


class Login:
    ...


class App:

    def __init__(self) -> None:
        self.root = Tk()
        self.widgets()
        self.layouts()

    def widgets(self):
        ...

    def layouts(self):
        ...

    def config(self):
        self.root.title("MundoCine")
        self.root.geometry("800x250")
        self.root.resizable(0, 0)

    def run(self):
        self.config()
        self.root.mainloop()



if __name__ == "__main__":
    app = App()
    app.run()
