"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: implement it later
"""
from dataclasses import dataclass
from tkinter import Button, Entry, Label, Frame, Tk, ttk, Scrollbar

LABELS = ("código", "nombre", "formato", "proveedor", "existencia")


@dataclass
class Registro:
    codigo: str
    nombre: str
    formato: str
    proveedor: str
    existencia: str


class App(Frame):

    def __init__(self):
        self.root = Tk()
        self.entries = {}
        self.frm_datos = Frame(self.root, bg="navy")
        self.frm_header = Frame(self.root, bg="gray22")
        self.frm_viewer = Frame(self.root)
        self.frm_control = Frame(self.root, bg="black")
        self.frm_header.grid(columnspan=2, row=0, column=0)
        self.frm_datos.grid(row=1, column=0)
        self.frm_control.grid(row=2, column=0)
        self.frm_viewer.grid(row=1, rowspan=2, column=1)
        self.header_widgets()
        self.control_widgets()
        self.viewer_widgets()

    def header_widgets(self):
        Label(
            self.frm_header, text="Registro de datos", bg="gray22", fg="white",
            font=("Rockwell", 15, "bold"),
        ).grid(row=0, column=0)
        Label(
            self.frm_datos, text="Agregar nuevos datos", bg="navy", fg="white",
            font=("Rockwell", 13, "bold"),
        ).grid(row=0, column=0, columnspan=2)
        for i, label in enumerate(LABELS):
            Label(
                self.frm_datos, text=label.title(), bg="navy", fg="white",
                font=("Rockwell", 12, "bold"),
            ).grid(row=i+1, column=0, sticky="e", pady=15)
            entry = Entry(self.frm_datos, font=("Arial", 12))
            entry.grid(row=i+1, column=1, sticky="w", padx=5)
            self.entries[label] = entry

    def control_widgets(self):
        Label(self.frm_control, text="Control", fg="white", bg="black").grid(
            columnspan=3, row=0, column=0, pady=1, padx=4,
        )
        Button(self.frm_control, text="Agregar").grid(
            row=1, column=0, sticky="ew", pady=5, padx=5
        )
        Button(self.frm_control, text="Limpiar").grid(
            row=1, column=1, sticky="ew", pady=5, padx=5
        )
        Button(self.frm_control, text="Mostrar").grid(
            row=2, column=0, sticky="ew", pady=5, padx=5
        )

    def viewer_widgets(self):
        self.table = ttk.Treeview(self.frm_viewer, height=21)
        x = Scrollbar(
            self.frm_viewer, orient="horizontal", command=self.table.xview
        )
        y = Scrollbar(
            self.frm_viewer, orient="vertical", command=self.table.yview
        )
        self.table.grid(row=0, column=0)
        x.grid(row=1, column=0, sticky="ew")
        y.grid(row=0, column=1, sticky="ns")
        self.table.configure(xscrollcommand=x.set, yscrollcommand=y.set)
        self.table["columns"] = LABELS[1:]
        for i, label in enumerate(LABELS):
            self.table.column(
                f"#{i}", minwidth=100, width=115, anchor="center"
            )
            self.table.heading(
                f"#{i}", text=label.title(), anchor="center"
            )
        style = ttk.Style(self.frm_viewer)
        style.theme_use("alt")
        style.configure(".", font=("Helvetica", 12, "bold"), foreground="red2")
        style.configure(
            "Treeview",
            font=("Helvetica", 10, "bold"),
            foreground="black",
            background="white",
        )
        style.map(
            "Treeview",
            background=[("selected", "green2")],
            foreground=[("selected", "black")],
        )

    def run(self):
        self.root.title("Registro de datos")
        self.root.geometry("900x500")
        self.root.config(bg="gray22")
        self.root.resizable(0, 0)
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
