import random
import statistics
from pathlib import Path

print("zad1")


def znajdz_rozwiazania(limit=100, przesuniecie=150):
    """Szuka trojek (a, b, c) spelniajacych a+b+c = a*b*c - przesuniecie."""
    rozwiazania = []
    for a in range(1, limit + 1):
        for b in range(1, limit + 1):
            for c in range(1, limit + 1):
                if a + b + c == a * b * c - przesuniecie:
                    rozwiazania.append((a, b, c))
    return rozwiazania


rozwiazania = znajdz_rozwiazania()
print(
    f"Znaleziono {len(rozwiazania)} rozwiazan dla liczb naturalnych 1..100 "
    "(kolejnosc a, b, c ma znaczenie):"
)
for trojka in rozwiazania:
    print(trojka)

unikalne_zestawy = {tuple(sorted(tr)) for tr in rozwiazania}
print(
    f"Unikalne zestawy bez kolejnosci ({len(unikalne_zestawy)}): "
    f"{sorted(unikalne_zestawy)}"
)

print("\nzad2")


def symulacja_kwoty(poczatkowa=100.0, rzuty=21, rng=None):
    """Wykonuje jedna symulacje gry monetą."""
    generator = rng or random
    kwota = float(poczatkowa)
    for _ in range(rzuty):
        if generator.random() < 0.5:  # orzel
            kwota *= 1.5
        else:  # reszka
            kwota *= 0.75
    return kwota


def statystyki_symulacji(powtorzenia=1000, seed=123):
    rng = random.Random(seed)
    wyniki = [symulacja_kwoty(rng=rng) for _ in range(powtorzenia)]
    return wyniki


wyniki_symulacji = statystyki_symulacji()
mediana_kwoty = statistics.median(wyniki_symulacji)
print(f"Mediana kwoty po 21 rzutach (1000 symulacji): {mediana_kwoty:.2f} zl")
print(
    "Przyklady pierwszych 5 symulacji:",
    [round(wynik, 2) for wynik in wyniki_symulacji[:5]],
)
print(
    f"Min: {min(wyniki_symulacji):.2f} zl, "
    f"max: {max(wyniki_symulacji):.2f} zl, "
    f"srednia: {statistics.mean(wyniki_symulacji):.2f} zl"
)

print("\nzad3")

NUKLEOTYDY = ("A", "C", "G", "T")


def losowa_sekwencja(dlugosc, rng):
    if not isinstance(dlugosc, int):
        raise TypeError("Dlugosc sekwencji musi byc liczba calkowita.")
    if dlugosc <= 0:
        raise ValueError("Dlugosc sekwencji musi byc dodatnia.")
    return "".join(rng.choices(NUKLEOTYDY, k=dlugosc))


def policz_roznice_tymin(raw_a, raw_b, seed=321):
    """Symuluje dwie sekwencje o dlugosciach podanych przez uzytkownika."""
    try:
        a = int(raw_a)
        b = int(raw_b)
    except ValueError:
        print("Podane wartosci musza byc liczbami calkowitymi dodatnimi.")
        return None
    if a <= 0 or b <= 0:
        print("Podane wartosci musza byc liczbami calkowitymi dodatnimi.")
        return None

    rng = random.Random(seed)
    seq1 = losowa_sekwencja(a, rng)
    seq2 = losowa_sekwencja(b, rng)
    t1 = seq1.count("T")
    t2 = seq2.count("T")
    roznica = t1 - t2

    print(f"Sekwencja 1 (dl {a}): {seq1} -> T: {t1}")
    print(f"Sekwencja 2 (dl {b}): {seq2} -> T: {t2}")
    print(f"Roznica tymin (pierwsza - druga): {roznica}")
    return roznica


# Przyklad bez blokowania input() — w prawdziwej sesji mozna podmienic na input().
przyklad_a = "12"
przyklad_b = "15"
policz_roznice_tymin(przyklad_a, przyklad_b)

print("\nzad4")

OZDOBY = ["O", "*", "@", "0", "x"]


def ozdob_warstwe(szerokosc, rng):
    """Losuje ozdoby na pojedynczej warstwie choinki."""
    warstwa = ["+"] * szerokosc
    maks_ozdob = max(1, szerokosc // 2)
    liczba_ozdob = rng.randint(1, maks_ozdob)
    pozycje = rng.sample(range(szerokosc), k=liczba_ozdob)
    for idx in pozycje:
        warstwa[idx] = rng.choice(OZDOBY)
    return "".join(warstwa)


def generuj_choinke(warstwy=15, seed=2024):
    rng = random.Random(seed)
    linie = []
    linie.append(" " * warstwy + "X")
    for poziom in range(warstwy):
        szerokosc = 1 + 2 * poziom
        wciecie = warstwy - poziom
        linia = " " * wciecie + ozdob_warstwe(szerokosc, rng)
        linie.append(linia)
    linie.append(" " * (warstwy - 1) + "||")
    return "\n".join(linie)


choinka = generuj_choinke()
print(choinka)

print("\nzad5")


def przygotuj_przykladowe_pliki(folder):
    """Tworzy eksperymentalny zestaw plikow z ocenami."""
    sciezka = Path(folder)
    sciezka.mkdir(exist_ok=True)
    dane = {
        "Piotr": [4, 5, 3, 5],
        "Kamil": [3, 6, 3, 4],
        "Anna": [5, 5, 4, 5],
    }
    for osoba, oceny in dane.items():
        zawartosc = ",".join(str(o) for o in oceny)
        (sciezka / f"{osoba}.txt").write_text(zawartosc, encoding="utf-8")
    return sciezka


def wczytaj_oceny(folder):
    sciezka = Path(folder)
    if not sciezka.exists():
        raise FileNotFoundError(f"Folder {folder} nie istnieje.")

    oceny = {}
    for plik in sorted(sciezka.glob("*.txt")):
        zawartosc = plik.read_text(encoding="utf-8").strip()
        if not zawartosc:
            continue
        try:
            liczby = [float(elem.strip()) for elem in zawartosc.split(",") if elem.strip()]
        except ValueError as err:
            raise ValueError(f"Niepoprawna wartosc w pliku {plik.name}") from err
        if liczby:
            oceny[plik.stem] = liczby
    return oceny


def policz_srednie(oceny):
    srednie_osob = {osoba: statistics.mean(wartosci) for osoba, wartosci in oceny.items()}
    wszystkie = [wartosc for wartosci in oceny.values() for wartosc in wartosci]
    srednia_grupy = statistics.mean(wszystkie) if wszystkie else 0.0
    return srednie_osob, srednia_grupy


folder_ocen = przygotuj_przykladowe_pliki("oceny_zad5")
oceny_wczytane = wczytaj_oceny(folder_ocen)
srednie_osob, srednia_grupy = policz_srednie(oceny_wczytane)
for osoba, srednia in srednie_osob.items():
    print(f"Srednia dla {osoba}: {srednia:.2f}")
print(f"Srednia ocen calej grupy: {srednia_grupy:.3f}")
