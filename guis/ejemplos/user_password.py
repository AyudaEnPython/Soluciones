"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Label, Button, Entry, messagebox

DATABASE = {
    "user": "admin",
    "password": "1234"
}


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.tries = 0
        self.setup_ui()

    def setup_ui(self):
        Label(self, text="Usuario: ").grid(row=0, column=0)
        self.user = Entry(self)
        self.user.grid(row=0, column=1)
        Label(self, text="Contraseña: ").grid(row=1, column=0)
        self.password = Entry(self)
        self.password.grid(row=1, column=1)
        self.password.config(show="*")
        self.btn_accept = Button(self, text="Aceptar", command=self.accept)
        self.btn_accept.grid(row=2, column=0)
        self.btn_cancel = Button(self, text="Cancelar", command=self.cancel)
        self.btn_cancel.grid(row=2, column=1)

    def accept(self):
        user = self.user.get()
        password = self.password.get()
        if user == DATABASE["user"] and password == DATABASE["password"]:
            messagebox.showinfo("Bienvenido", "Bienvenido {}".format(user))
            self.destroy()
        else:
            self.tries += 1
            if self.tries == 3:
                messagebox.showerror(
                    "Error",
                    "Ha superado el número de intentos"
                )
                self.destroy()
            else:
                messagebox.showerror(
                    "Error",
                    "Usuario o contraseña incorrecta"
                )

    def cancel(self):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
