"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import subprocess
from tkinter import Button, Entry, Tk

DB = {
    "Term 01": "ayudaenpython.com",
    "Term 02": "google.com",
    "Term 03": "facebook.com",
    "Term 04": "twitter.com",
    "Term 05": "youtube.error",
    "Term 06": "instagram.com",
    "Term 07": "linkedin.com",
    "Term 08": "github.com",
    "Term 09": "stackoverflow.error",
    "Term 10": "reddit.com",
}
TERMINALES = len(DB)


def ping(hostname):
    try:
        stdout = subprocess.Popen(["ping", "-n", "1", hostname]).wait()
        if stdout == 0:
            return "Conectado"
        else:
            return "---------"
    except subprocess.CalledProcessError:
        return "---------"


class Terminals(Tk):

    def __init__(self):
        super().__init__()
        self.title("Ayuda en Python")
        self.entries = []
        self.buttons = []
        self.widgets()
        self.read_db()

    def widgets(self):
        for i in range(1, TERMINALES + 1):
            button = Button(self, text=f"Term {i:02}")
            button.config(command=lambda button=button: self.scan(button))
            entry = Entry(self, width=24)
            button.grid(row=i, column=0, padx=5, pady=5)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)
            self.buttons.append(button)

    def read_db(self):
        for i, entry in enumerate(self.entries):
            entry.insert("end", DB[f"Term {i + 1:02}"])
        for entry in self.entries:
            entry.config(state="disabled")

    def scan(self, button):
        index = self.buttons.index(button)
        state = ping(self.entries[index].get())
        self.entries[index].config(state="normal")
        self.entries[index].delete(0, "end")
        self.entries[index].insert("end", state)
        self.entries[index].config(state="disabled")


if __name__ == "__main__":
    app = Terminals()
    app.mainloop()
