"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from tkinter import Entry, Frame, Label, Tk, messagebox
from tkinter.ttk import Button
from typing import Tuple

from models import UserManager, LoginService


class LoginWindow(Frame):

    def __init__(
        self,
        master,
        manager: UserManager,
        service: LoginService,
    ) -> None:
        super().__init__(master)
        self.setup_ui()
        self.manager = manager()
        self.service = service

    def setup_ui(self):
        Label(
            self, text="Welcome back!", font=("Arial", 24)
        ).grid(row=0, columnspan=2, padx=10, pady=10)
        for i, text in enumerate(("Username", "Password"), 1):
            Label(self, text=text).grid(row=i, column=0)
        self.username = Entry(self)
        self.username.grid(row=1, column=1)
        self.password = Entry(self, show="*")
        self.password.grid(row=2, column=1)
        self.signup = Button(self, text="Sign Up", command=self.signup_user)
        self.signup.grid(row=3, column=0, ipadx=5, ipady=5, padx=10, pady=10)
        self.login = Button(self, text="Log In", command=self.login_user)
        self.login.grid(row=3, column=1, ipadx=5, ipady=5, padx=10, pady=10)

    def login_user(self):
        service = self.service(self.manager)
        try:
            service.login(*self._validated_data())
            messagebox.showinfo("Success", "User logged in")
        except Exception as e:
            messagebox.showerror("Error", e)

    def signup_user(self) -> None:
        try:
            self.manager.add_user(*self._validated_data())
            self._clear()
            messagebox.showinfo("Success", "User created")
        except Exception as e:
            messagebox.showerror("Error", e)

    def _clear(self):
        self.username.delete(0, "end")
        self.password.delete(0, "end")

    def _validated_data(self) -> Tuple[str, str]:
        username, password = self.username.get(), self.password.get()
        if not username and not password:
            raise Exception("Username and password are required")
        if not password:
            raise Exception("Password is required")
        if not username:
            raise Exception("Username is required")
        return username, password


class App(Tk):

    def __init__(self, manager: UserManager, service: LoginService) -> None:
        super().__init__()
        self.title("Ayuda en Python")
        self.geometry("260x160")
        LoginWindow(self, manager, service).pack()


if __name__ == "__main__":
    app = App(UserManager, LoginService)
    app.mainloop()
