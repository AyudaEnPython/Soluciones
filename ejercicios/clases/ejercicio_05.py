"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import List

STAR = "\u2605"
WHITE = "\u2606"


@dataclass
class Person:
    fullname: str
    email: str


@dataclass
class User(Person):
    nickaname: str


@dataclass
class Instructor(Person):
    courses: int


class Rating:

    SPACES: int = 5

    def __init__(self, rate: float) -> None:
        self._rate = rate

    @property
    def rate(self) -> float:
        return self._rate

    @rate.setter
    def rate(self, rate: float) -> None:
        self._rate = rate

    def __str__(self) -> str:
        return f"Rating ({self._rate}): {STAR * round(self._rate)}"


class RatingSystem:

    def __init__(self) -> None:
        self._rating = []

    def give_rate(self, rate: float) -> None:
        self._rating.append(rate)

    def rating_mean(self) -> Rating:
        try:
            return Rating(round(sum(self._rating) / len(self._rating), 2))
        except ZeroDivisionError:
            return 0

    def reviews(self) -> int:
        return len(self._rating)


class Course:

    def __init__(
        self,
        title: str,
        instructor: Instructor,
        price: float,
    ) -> None:
        self.title = title
        self.instructor = instructor
        self.price = price
        self.conferences = 1
        self.users: List[User] = []
        self.rating = RatingSystem()

    def give_rating(self, rate: int) -> None:
        self.rating.give_rate(rate)

    def ratings(self) -> int:
        return self.rating.reviews()

    def rating_mean(self) -> Rating:
        return self.rating.rating_mean()

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def details(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Instructor: {self.instructor}\n"
            f"Price: $ {self.price}\n"
            f"Conferences: {self.conferences}\n"
            f"Users: {len(self.users)}\n"
            f"Ratings: {self.ratings()}\n"
            f"Rating mean: {self.rating_mean()}\n"
        )

    def __str__(self) -> str:
        return (
            f"Title: {self.title}\n"
            f"Instructor: {self.instructor}\n"
            f"Price: $ {self.price}\n"
        )


class VideoCourse(Course):

    def __init__(
        self,
        title: str,
        instructor: Instructor,
        price: float,
        lenght: float
    ) -> None:
        super().__init__(title, instructor, price)
        self.lenght = lenght


class PdfCourse(Course):

    def __init__(self, pages: int) -> None:
        super().__init__()
        self.pages = pages


if __name__ == "__main__":
    instructor = Instructor("Joe Satriani", "js@satriani.com", 1)
    course = VideoCourse(
        "Guitar Chords 101",
        instructor,
        99.99,
        8,
    )
    course.add_user(User("Steve Vai", "jem@vai.com", "vai"))
    course.add_user(User("Kirk H.", "kirk@metallica.com", "kirk"))
    print(course)
    course.conferences = 3
    course.give_rating(4.9)
    course.give_rating(4.7)
    course.give_rating(5)
    print(course.details())
    print(course.users)
