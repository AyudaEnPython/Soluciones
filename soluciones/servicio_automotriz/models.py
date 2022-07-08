"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import Any, List

from utils import Arr, read_file, save_file


@dataclass
class Order:
    id_: int
    code: int
    quantity: int

    def to_list(self) -> List[Any]:
        return [self.id_, self.code, self.quantity]


@dataclass
class Catalog:
    filename: str
    data: Arr = field(init=False)

    def __post_init__(self) -> None:
        self.data = read_file(self.filename)

    def add_item(self, code: int, description: str, price: int) -> None:
        self.data.append([code, description, price])

    def save(self, filename: str) -> None:
        save_file(filename, self.data)

    def get_price(self, code: int) -> int:
        for id_, _, price in self.data:
            if id_ == code:
                return price
        return 0

    def calculate(self, orders: List[Order]) -> List[int]:
        total = [0] * len(orders)
        for order in orders:
            total[order.id_-1] += self.get_price(order.code) * order.quantity
        return total
