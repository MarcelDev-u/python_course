"""Prosty modul z klasa Punkt wykorzystywany w zadaniach z zajec7."""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Punkt:
    """Klasa reprezentujaca punkt/wektor na plaszczyznie."""

    x: float = 0
    y: float = 0

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Punkt({self.x}, {self.y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Punkt):
            return NotImplemented
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)

    def __ne__(self, other: object) -> bool:
        wynik = self.__eq__(other)
        if wynik is NotImplemented:
            return NotImplemented
        return not wynik

    def __add__(self, other: "Punkt") -> "Punkt":
        if not isinstance(other, Punkt):
            return NotImplemented
        return Punkt(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Punkt") -> "Punkt":
        if not isinstance(other, Punkt):
            return NotImplemented
        return Punkt(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Punkt") -> float:
        if not isinstance(other, Punkt):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    def length(self) -> float:
        """Dlugosc wektora."""
        return math.hypot(self.x, self.y)

    def cross(self, other: "Punkt") -> float:
        if not isinstance(other, Punkt):
            raise TypeError("Iloczyn wektorowy tylko dla punktu.")
        return self.x * other.y - self.y * other.x
