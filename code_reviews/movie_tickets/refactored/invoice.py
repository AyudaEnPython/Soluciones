"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import csv
import pandas as pd
from dataclasses import dataclass

from constants import DataList, QueryResult, CONVERSION, DATA, PRICE


@dataclass
class Invoice:
    id_: str
    quantity: int
    day: str
    movie: str
    type_: str

    def __post_init__(self) -> None:
        price = self.quantity * self._get_price(self.day)
        self.price = round(price * CONVERSION[self.type_], 2)

    def _get_price(day: str) -> int:
        prices = {
            (day == "lunes" or day == "martes") : PRICE["lun-mar"],
            (day == "miércoles" or day == "jueves") : PRICE["mie-jue"],
            (day == "viernes" or day == "sábado") : PRICE["vie-sab"],
            (day == "domingo") : PRICE["dom"],
        }
        return prices[True]

    def get_price(self) -> str:
        return f"{self.price:.2f}"

    def to_list(self) -> DataList:
        return [
            self.id_, str(self.quantity), self.day, self.movie, self.price
        ]

    def to_csv(self) -> None:
        with open(DATA, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.to_list())


class Search:

    def __init__(self, filename: str = DATA) -> None:
        self.df = pd.read_csv(filename, sep=",")

    def get_by(self, tag: str, query: str) -> QueryResult:
        if query.isdigit() and tag == "id":
            result = self.df[self.df[tag] == int(query)]
        elif not query.isdigit() and tag == "dia":
            result = self.df[self.df[tag].str.contains(query)]
        else:
            return False, None
        if result.empty:
            return False, None
        return True, result.to_numpy().tolist()
