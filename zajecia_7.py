from __future__ import annotations

import math
from pathlib import Path

from points import Punkt

# Zadanie 1: klasa Prostokat
print("zad1")


class Prostokat:
    """Prosty prostokat z podstawowymi metodami geometrycznymi."""

    def __init__(self, dlugosc: float, szerokosc: float):
        if dlugosc <= 0 or szerokosc <= 0:
            raise ValueError("Dlugosc i szerokosc musza byc dodatnie.")
        self.dlugosc = float(dlugosc)
        self.szerokosc = float(szerokosc)

    def obwod(self) -> float:
        return 2 * (self.dlugosc + self.szerokosc)

    def pole(self) -> float:
        return self.dlugosc * self.szerokosc

    def przekatna(self) -> float:
        return math.hypot(self.dlugosc, self.szerokosc)

    def __str__(self) -> str:  # to co zobaczymy w print()
        return f"Prostokat {self.dlugosc} x {self.szerokosc}"


prost = Prostokat(3, 4.5)
print(prost)
print(f"Obwod: {prost.obwod()}")
print(f"Pole: {prost.pole()}")
print(f"Przekatna: {prost.przekatna():.3f}")

# Zadanie 2: klasa Punkt (importowana z points.py)
print("\nzad2")
p1 = Punkt(2, 3)
p2 = Punkt(-1, 4)

print(f"p1 = {p1}, p2 = {p2}")
print(f"Repr p1: {repr(p1)}")
print(f"p1 == p2? {p1 == p2}")
print(f"p1 + p2 = {p1 + p2}")
print(f"p1 - p2 = {p1 - p2}")
print(f"Iloczyn skalarny p1 * p2 = {p1 * p2}")
print(f"Dlugosc wektora p1: {p1.length():.3f}")
print(f"Iloczyn wektorowy p1 x p2: {p1.cross(p2)}")

# Zadanie 3: klasa Kolo
print("\nzad3")


class Kolo:
    """Klasa reprezentujaca kolo na plaszczyznie."""

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1):
        if radius < 0:
            raise ValueError("Promien nie moze byc ujemny.")
        self.pt = Punkt(x, y)
        self.radius = float(radius)

    def __repr__(self) -> str:
        return f"Kolo({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Kolo):
            return NotImplemented
        return self.pt == other.pt and math.isclose(self.radius, other.radius)

    def __ne__(self, other: object) -> bool:
        wynik = self.__eq__(other)
        if wynik is NotImplemented:
            return NotImplemented
        return not wynik

    def area(self) -> float:
        return math.pi * self.radius**2

    def move(self, x: float, y: float) -> "Kolo":
        """Przesuwa srodek kola o wektor (x, y) i zwraca nowe kolo."""
        return Kolo(self.pt.x + x, self.pt.y + y, self.radius)

    def tangent(self, other: "Kolo") -> bool:
        """Sprawdza, czy kola sa styczne (zewnetrznie lub wewnetrznie)."""
        if not isinstance(other, Kolo):
            return False
        dist = math.hypot(self.pt.x - other.pt.x, self.pt.y - other.pt.y)
        return math.isclose(dist, self.radius + other.radius) or math.isclose(
            dist, abs(self.radius - other.radius)
        )


k1 = Kolo(0, 0, 2)
k2 = Kolo(4, 0, 2)
k3 = k1.move(1, 1)
print(f"k1: {k1}")
print(f"k2: {k2}")
print(f"Pole k1: {k1.area():.3f}")
print(f"k1 przesuniete o (1,1): {k3}")
print(f"Czy k1 i k2 sa styczne? {k1.tangent(k2)}")
print(f"Czy k1 i k3 sa styczne? {k1.tangent(k3)}")

# Zadanie 4: klasa FunkcjaKwadratowa
print("\nzad4")


class FunkcjaKwadratowa:
    """Reprezentuje funkcje ax^2 + bx + c wraz z rozwiazywaniem."""

    def __init__(self, a: float, b: float, c: float):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def rozwiaz(self) -> tuple[float, ...]:
        """Zwraca miejsca zerowe (puste, jedno lub dwa)."""
        if math.isclose(self.a, 0.0):
            if math.isclose(self.b, 0.0):
                if math.isclose(self.c, 0.0):
                    raise ValueError("Nieskonczenie wiele rozwiazan (0x^2+0x+0).")
                return tuple()  # brak rozwiazan
            return (-self.c / self.b,)  # rownanie liniowe

        delta = self.b**2 - 4 * self.a * self.c
        if delta < 0:
            return tuple()
        if math.isclose(delta, 0.0):
            return (-self.b / (2 * self.a),)
        pierw = math.sqrt(delta)
        return (
            (-self.b - pierw) / (2 * self.a),
            (-self.b + pierw) / (2 * self.a),
        )

    def wierzcholek(self) -> tuple[float, float]:
        if math.isclose(self.a, 0.0):
            raise ValueError("Funkcja liniowa nie ma wierzcholka.")
        p = -self.b / (2 * self.a)
        q = self.wartosc(p)
        return p, q

    def wartosc(self, x: float) -> float:
        return self.a * x * x + self.b * x + self.c

    def __repr__(self) -> str:
        return f"FunkcjaKwadratowa(a={self.a}, b={self.b}, c={self.c})"


f1 = FunkcjaKwadratowa(1, -3, 2)  # ma dwa rozwiazania: 1 i 2
f2 = FunkcjaKwadratowa(0, 2, 4)  # rownanie liniowe, jedno rozwiazanie
f3 = FunkcjaKwadratowa(1, 0, 5)  # delta < 0, brak rozwiazan

print(f"{f1} -> pierwiastki: {f1.rozwiaz()}, wierzcholek: {f1.wierzcholek()}")
print(f"{f2} -> pierwiastki: {f2.rozwiaz()}")
print(f"{f3} -> pierwiastki: {f3.rozwiaz()}")

# Zadanie 5: klasa DNAseq
print("\nzad5")


class DNAseq:
    """Klasa operujaca na sekwencjach DNA."""

    def __init__(self, name: str, seq: str):
        if not name:
            raise ValueError("Nazwa sekwencji nie moze byc pusta.")
        if not isinstance(seq, str):
            raise TypeError("Sekwencja musi byc napisem.")
        self.name = str(name)
        self.seq = seq.replace(" ", "").upper()

    def __repr__(self) -> str:
        return f">{self.name}\n{self.seq}"

    __str__ = __repr__

    def __add__(self, other: "DNAseq") -> "DNAseq":
        if not isinstance(other, DNAseq):
            return NotImplemented
        return DNAseq(f"{self.name}_{other.name}", self.seq + other.seq)

    def __len__(self) -> int:
        return len(self.seq)

    def __getitem__(self, key) -> "DNAseq":
        return DNAseq(self.name, self.seq[key])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DNAseq):
            return NotImplemented
        return self.name == other.name and self.seq == other.seq

    def __contains__(self, value: str) -> bool:
        if not isinstance(value, str):
            return False
        return value.upper() in self.seq

    def komplementarna(self) -> "DNAseq":
        mapa = str.maketrans("ACGT", "TGCA")
        dop = self.seq.translate(mapa)
        return DNAseq(f"komplementarna_do_{self.name}", dop)

    def odwrotnie_komplementarna(self) -> "DNAseq":
        odw = self.komplementarna().seq[::-1]
        return DNAseq(f"odwrotnie_komplementarna_do_{self.name}", odw)

    def zapisz(self) -> Path:
        """Zapisuje sekwencje do pliku FASTA o nazwie odpowiadajacej sekwencji."""
        nazwa_pliku = f"{self.name}.fa"
        Path(nazwa_pliku).write_text(repr(self) + "\n", encoding="utf-8")
        return Path(nazwa_pliku)

    def sklad(self) -> dict[str, float]:
        """Zwraca czestosci A/C/G/T w sekwencji."""
        dl = len(self.seq)
        if dl == 0:
            return {nt: 0.0 for nt in "ACGT"}
        return {nt: round(self.seq.count(nt) / dl, 3) for nt in "ACGT"}

    def doklej(self, x: str) -> "DNAseq":
        return DNAseq(self.name, self.seq + str(x).upper())


s1 = DNAseq("sekwencja1", "ATGGC")
print(s1)

s2 = DNAseq("sekwencja2", "TCA")
s3 = s1 + s2
print("s1 + s2 ->")
print(s3)

print(f"Dlugosc s3: {len(s3)}")
print("Wyciecie s3[2:5]:")
print(s3[2:5])
print(f"s1 == s2? {s1 == s2}")
print(f"Czy 'AT' w s1? {'AT' in s1}")

print("Komplementarna do s1:")
print(s1.komplementarna())
print("Odwrotnie komplementarna do s1:")
print(s1.odwrotnie_komplementarna())

s4 = s1.doklej("AA")
print("s1 doklejone 'AA':")
print(s4)
print(f"Sklad procentowy s4: {s4.sklad()}")

plik = s1.zapisz()
print(f"Sekwencje s1 zapisano do pliku: {plik.resolve()}")
