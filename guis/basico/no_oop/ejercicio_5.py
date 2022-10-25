"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, messagebox, Tk
from typing import Dict

CREDENTIALS: Dict[str, str] = {
    "username": "pythonista",
    "password": "AyudaEnPython",
}


def validate(user, password):
    if (
        user == CREDENTIALS["username"] and
        password == CREDENTIALS["password"]
    ):
        messagebox.showinfo("Success", "Access granted!")
    else:
        messagebox.showerror("Error", "Access denied!")


def setup_ui(master):
    Label(master, text="Username").grid(row=0, column=0, padx=5, pady=5)
    Label(master, text="Password").grid(row=1, column=0, padx=5, pady=5)
    user = Entry(master)
    password = Entry(master, show="*")
    login = Button(master, text="Log In")
    login["command"] = lambda: validate(user.get(), password.get())
    user.grid(row=0, column=1)
    password.grid(row=1, column=1, padx=5, pady=5)
    login.grid(row=2, columnspan=2, padx=5, pady=5)


if __name__ == "__main__":
    root = Tk()
    setup_ui(root)
    root.mainloop()
