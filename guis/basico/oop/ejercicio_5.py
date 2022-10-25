"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Button, Entry, Label, messagebox, Tk
from typing import Dict

CREDENTIALS: Dict[str, str] = {
    "username": "pythonista",
    "password": "AyudaEnPython",
}


class App(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.title("AyudaEnPython Platform")
        self.geometry("215x105")
        self.setup_ui()
        self.login["command"] = self.validate

    def setup_ui(self) -> None:
        Label(self, text="Username").grid(row=0, column=0, padx=5, pady=5)
        Label(self, text="Password").grid(row=1, column=0, padx=5, pady=5)
        self.user = Entry(self)
        self.password = Entry(self, show="*")
        self.login = Button(self, text="Log In")
        self.user.grid(row=0, column=1)
        self.password.grid(row=1, column=1, padx=5, pady=5)
        self.login.grid(row=2, columnspan=2, padx=5, pady=5)

    def validate(self) -> None:
        user = self.user.get()
        password = self.password.get()
        if (
            user == CREDENTIALS["username"] and
            password == CREDENTIALS["password"]
        ):
            messagebox.showinfo("Success", "Access granted!")
        else:
            messagebox.showerror("Error", "Access denied!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
