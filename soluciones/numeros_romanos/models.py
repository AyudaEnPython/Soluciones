"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import re
from typing import Any, Dict, Union


class Number:

    _nr: Dict[int, str] = {
        1000: "M", 900: "CM", 500: "D", 400: "CD",
        100: "C", 90: "XC", 50: "L", 40: "XL",
        10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I",
    }
    _rn: Dict[str, int] = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
    }

    def __init__(self, n: Union[int, str]) -> None:
        self._validate(n)
        self.value: int = self._convert(n)
        self.roman: str = self._to_roman(self.value)

    @staticmethod
    def is_valid_roman(r: str) -> bool:
        return bool(re.match(
            "^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", r
        ))

    @staticmethod
    def _validate_boundaries(n: int) -> None:
        if not (0 <= n <= 3999):
            raise ValueError(f"Number must be between 0 and 3999")

    def _validate(self, n: Any) -> None:
        if not isinstance(n, (int, str)):
            raise TypeError(
                "Number must be an integer or Roman numeral string"
            )
        if isinstance(n, int):
            self._validate_boundaries(n)
        elif isinstance(n, str):
            if n.isdigit():
                self._validate_boundaries(int(n))
            elif not self.is_valid_roman(n):
                raise ValueError("Invalid Roman numeral")

    def _convert(self, n: Union[int, str]) -> int:
        return n if isinstance(n, int) else (
            int(n) if n.isdigit() else self._to_int(n)
        )

    def _to_roman(self, n: int) -> str:
        r = []
        for k, v in self._nr.items():
            while n >= k:
                r.append(v)
                n -= k
        return "".join(r)

    def _to_int(self, r: str) -> int:
        n = prev = 0
        for s in r[::-1]:
            c = self._rn[s]
            n += c if c >= prev else - c
            prev = c
        return n

    def __add__(self, other: Any) -> "Number":
        if isinstance(other, Number):
            other_value = other.value
        else:
            self._validate(other)
            other_value = self._convert(other)
        result = self.value + other_value
        self._validate_boundaries(result)
        return Number(result)

    def __str__(self) -> str:
        return f"Integer: {self.value} | Roman: {self.roman}"
