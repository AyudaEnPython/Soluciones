"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Tk, Label, Button, Entry, messagebox, IntVar

DATABASE = {
    "user": "admin",
    "password": "1234"
}

root = Tk()
intentos = IntVar()
intentos.set(0)


def accept(user, password):
    if (
        user.get() == DATABASE["user"] and
        password.get() == DATABASE["password"]
    ):
        messagebox.showinfo("Bienvenido", "Bienvenido {}".format(user.get()))
        root.destroy()
    else:
        intentos.set(intentos.get() + 1)
        if intentos.get() == 3:
            messagebox.showerror("Error", "Ha superado el número de intentos")
            root.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrecta")


def cancel(root):
    root.destroy()


def setup_ui(root):
    Label(root, text="Usuario: ").grid(row=0, column=0)
    user = Entry(root)
    user.grid(row=0, column=1)
    Label(root, text="Contraseña: ").grid(row=1, column=0)
    password = Entry(root)
    password.grid(row=1, column=1)
    password.config(show="*")
    btn_accept = Button(root, text="Aceptar")
    btn_accept["command"] = lambda: accept(user, password)
    btn_accept.grid(row=2, column=0)
    btn_cancel = Button(root, text="Cancelar")
    btn_cancel["command"] = lambda: cancel(root)
    btn_cancel.grid(row=2, column=1)


if __name__ == "__main__":
    setup_ui(root)
    root.mainloop()
