"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""


class User:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return f'{self.name} {self.last_name}'


if __name__ == '__main__':
    # dummy example
    user_1 = User("Joe", "Satriani")
    user_2 = User("Steve", "Vai")
    user_3 = User("Eric", "Johnson")

    print("G3: Live in Concert 1997")
    for user in (user_1, user_2, user_3):
        print(f"- {user}")
