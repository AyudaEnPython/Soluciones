"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class User:
    _username: str
    _password: str

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    def __repr__(self) -> str:
        return f"Username: {self._username}"


@dataclass
class UserManager:
    _users: Dict[str, User] = field(default_factory=dict)

    def add_user(self, username: str, password: str) -> None:
        if username in self._users:
            raise ValueError(f"User {username} already exists.")
        self._users[username] = User(username, password)

    def get_user(self, username: str) -> User:
        if username not in self._users:
            raise KeyError(f"User {username} does not exist.")
        return self._users[username]


@dataclass
class LoginService:
    _user_manager: UserManager

    def login(self, username: str, password: str) -> bool:
        user = self._user_manager.get_user(username)
        if user.password != password:
            raise ValueError(f"Password incorrect for user {username}")
        assert user.password == password
        return True
