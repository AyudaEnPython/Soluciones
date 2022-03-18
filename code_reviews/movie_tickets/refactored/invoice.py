"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import csv
import pandas as pd
from typing import List, Tuple
from dataclasses import dataclass
from typing import Dict, List, Union

CONVERSION: Dict[str, Union[int, float]] = {"local": 1, "foreign": 0.27}
DATA = "data/registro.csv"


def write_csv_file(filename: str, s: List[str]) -> None:
    with open(filename, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(s)


def _get_price(day: str) -> int:
    prices = {
        (day == "lunes" or day == "martes") : 20_000,
        (day == "miércoles" or day == "jueves") : 15_000,
        (day == "viernes" or day == "sábado") : 30_000,
        (day == "domingo") : 35_000,
    }
    return prices[True]


@dataclass
class Invoice:
    id_: str
    quantity: int
    day: str
    movie: str
    type_: str

    def __post_init__(self) -> None:
        price = self.quantity * _get_price(self.day)
        self.price = round(price * CONVERSION[self.type_], 2)

    def get_price(self) -> str:
        return f"{self.price:.2f}"

    def to_list(self) -> List[str]:
        return [
            self.id_, str(self.quantity), self.day, self.movie, self.price
        ]

    def to_csv(self) -> None:
        write_csv_file(DATA, self.to_list())


class Search:

    def __init__(self, filename=DATA) -> None:
        self.df = pd.read_csv(filename, sep=",")

    def get_by(self, tag: str, query: str) -> Tuple[bool, pd.DataFrame]:
        if query.isdigit() and tag == "id":
            result = self.df[self.df[tag] == int(query)]
        else:
            result = self.df[self.df[tag].str.contains(query)]
        if result.empty:
            return False, None
        return True, result.to_numpy().tolist()
