import math
import random
import statistics
from pathlib import Path

print("zad1")


def na_kelwina(temp_c):
    return temp_c + 273.15


print(na_kelwina(25))

print("zad2")


def suma_elementow_par(pary):
    suma = []
    for idx, element in enumerate(pary, start=1):
        try:
            pierwsza, druga = element
        except (TypeError, ValueError) as err:
            raise ValueError(f"Element nr {idx} nie jest dwuelementową kolekcją: {element}") from err
        if not isinstance(pierwsza, (int, float)) or not isinstance(druga, (int, float)):
            raise TypeError(f"Element nr {idx} zawiera wartości nieliczbowe: {element}")
        suma.append(pierwsza + druga)
    return suma


przyklad_par = [[1, 2], [4, 5], [6, 7], [-2, 3]]
print(suma_elementow_par(przyklad_par))

print("zad3")


def wartosc_wyrazenia(a, b, c=0):
    licznik = a**2 - b**2
    mianownik = c**4 + 1
    return licznik / mianownik


print(wartosc_wyrazenia(3, 2))
print(wartosc_wyrazenia(3, 2, 1))

print("zad4")


def ile_tymin(*sekwencje):
    suma_tymin = 0
    for idx, seq in enumerate(sekwencje, start=1):
        if not isinstance(seq, str):
            raise TypeError(f"Sekwencja nr {idx} nie jest napisem: {seq!r}")
        suma_tymin += seq.upper().count("T")
    return suma_tymin


print(ile_tymin("ATAA", "GG", "TTC"))

print("zad5")


def srednia_z_inputu(stop_token="q", inputs=None):
    liczby = []
    iterator = iter(inputs) if inputs is not None else None
    while True:
        if iterator is not None:
            try:
                raw = next(iterator)
            except StopIteration:
                break
        else:
            raw = input(f"Podaj liczbę lub {stop_token}, aby zakończyć: ")
        if raw.lower() == stop_token.lower():
            break
        try:
            liczby.append(float(raw))
        except ValueError:
            print(f"Pomijam niepoprawną wartość: {raw}")
    if not liczby:
        return None
    return sum(liczby) / len(liczby)


print(srednia_z_inputu(inputs=["10", "5", "q"]))

print("zad6")


def zapisz_liczby_do_pliku(liczby, filename="zad6_wyniki.txt"):
    liczby_float = [float(x) for x in liczby]
    srednia = sum(liczby_float) / len(liczby_float) if liczby_float else 0.0
    with open(filename, "w", encoding="utf-8") as handler:
        for liczba in liczby_float:
            handler.write(f"{liczba}\n")
        handler.write(f"srednia = {srednia}\n")
    return filename


plik_zad6 = zapisz_liczby_do_pliku([1, 2, 3, 5, 9])
print(f"Wyniki zapisano w pliku {plik_zad6}")

print("zad7")


def przygotuj_plik_sekwencje(filepath="sekwencje"):
    sciezka = Path(filepath)
    if sciezka.exists():
        return sciezka
    zawartosc = "seq1 ATGCGT\nseq2 TTTAAA\nseq3 CCGTTA\n"
    sciezka.write_text(zawartosc, encoding="utf-8")
    return sciezka


def wczytaj_sekwencje(filepath="sekwencje"):
    dane = {}
    with open(filepath, "r", encoding="utf-8") as handler:
        for line_number, line in enumerate(handler, start=1):
            line = line.strip()
            if not line:
                continue
            czesci = line.split()
            if len(czesci) != 2:
                raise ValueError(f"Niepoprawny format w linii {line_number}: {line}")
            nazwa, sekwencja = czesci
            dane[nazwa] = sekwencja
    return dane


sciezka_sekwencji = przygotuj_plik_sekwencje()
print(wczytaj_sekwencje(sciezka_sekwencji))

print("zad8")

import zajecia_3_module as z3m

print(z3m.przywitaj("Adrian"))
print(z3m.podnies_do_kwadratu(5))
print(z3m.wypisz_liste(["a", "b", "c"]))

print("zad9")


def oblicz_wyrazenie_zad9():
    licznik = math.sin(math.pi / 4) + math.factorial(6)
    mianownik = math.e**4 + math.log10(5)
    return licznik / mianownik


print(oblicz_wyrazenie_zad9())

print("zad10")


def statystyki_gaussa(liczba_prob=100, srednia=3, odchylenie=2, seed=42):
    random.seed(seed)
    wartosci = [random.gauss(srednia, odchylenie) for _ in range(liczba_prob)]
    srednia_arytmetyczna = statistics.mean(wartosci)
    if all(value > 0 for value in wartosci):
        srednia_geometryczna = math.exp(sum(math.log(value) for value in wartosci) / len(wartosci))
    else:
        srednia_geometryczna = None
    odchylenie_standardowe = statistics.pstdev(wartosci)
    return wartosci, srednia_arytmetyczna, srednia_geometryczna, odchylenie_standardowe


values, mean_val, geom_val, std_val = statystyki_gaussa()
print(f"Srednia arytmetyczna: {mean_val:.3f}")
if geom_val is None:
    print("Srednia geometryczna: brak (trafila się liczba niedodatnia)")
else:
    print(f"Srednia geometryczna: {geom_val:.3f}")
print(f"Odchylenie standardowe: {std_val:.3f}")
