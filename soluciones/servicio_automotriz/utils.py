"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import csv
from typing import Any, List

Arr = List[List[Any]]
FILENAME = "data/catalogo.csv"


def read_file(filename: str) -> Arr:
    data = []
    with open(filename, "r") as f:
        next(f)
        reader = csv.reader(f)
        for code, description, price in reader:
            data.append([int(code), description, int(price)])
    return data


def save_file(filename: str, data: Arr) -> None:
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "description", "price"])
        writer.writerows(data)
