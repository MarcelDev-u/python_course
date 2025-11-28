import re
from pathlib import Path

print("zad1")


def najdluzsze_powtorzenia(sekwencja, min_powtorzen=3):
    """
    Zwraca liste najdluzszych podsekwencji, ktore powtarzaja sie co
    najmniej `min_powtorzen` razy pod rzad w podanym napisie.
    """
    if not isinstance(sekwencja, str):
        raise TypeError("Sekwencja musi byc napisem.")
    if min_powtorzen < 2:
        raise ValueError("Liczba powtorzen musi byc >= 2.")

    seq = sekwencja.upper()
    znalezione = []
    widziane = set()
    n = len(seq)
    start = 0
    while start < n:
        max_len = (n - start) // min_powtorzen
        if max_len == 0:
            break
        najlepszy = ""
        najlepszy_powtorzenia = 0
        for dl in range(1, max_len + 1):
            motyw = seq[start : start + dl]
            pos = start + dl
            licznik = 1
            while pos + dl <= n and seq[pos : pos + dl] == motyw:
                licznik += 1
                pos += dl
            if licznik >= min_powtorzen and dl > len(najlepszy):
                najlepszy = motyw
                najlepszy_powtorzenia = licznik
        if najlepszy:
            if najlepszy not in widziane:
                znalezione.append(najlepszy)
                widziane.add(najlepszy)
            start += len(najlepszy) * max(najlepszy_powtorzenia, 1)
        else:
            start += 1
    return znalezione


sekwencja_przyklad = "ATTTGGCGAGAGACATCATCATCAT"
print(f"Sekwencja: {sekwencja_przyklad}")
print(f"Powtorzenia (>=3): {najdluzsze_powtorzenia(sekwencja_przyklad)}")

print("zad2")


def wstaw_spacje_miedzy_mala_a_duza(tekst):
    if not isinstance(tekst, str):
        raise TypeError("Tekst musi byc napisem.")
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", tekst)


tekst_spacji = "Mam na imie AdamNowak."
print(tekst_spacji)
print(wstaw_spacje_miedzy_mala_a_duza(tekst_spacji))

print("zad3")


def zamien_format_daty(tekst):
    if not isinstance(tekst, str):
        raise TypeError("Tekst musi byc napisem.")
    wzorzec = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
    return wzorzec.sub(r"\3-\2-\1", tekst)


tekst_dat = "Spotkanie 2025-11-28 i raport z 2024-01-05."
print(tekst_dat)
print(zamien_format_daty(tekst_dat))

print("zad4")


def popraw_podwojne_poczatki(tekst):
    if not isinstance(tekst, str):
        raise TypeError("Tekst musi byc napisem.")

    def poprawiaj(match):
        pierwsza, druga, reszta = match.groups()
        return pierwsza + druga.lower() + reszta.lower()

    wzorzec = re.compile(r"\b([A-Z])([A-Z])([a-z]+)")
    return wzorzec.sub(poprawiaj, tekst)


tekst_bledu = "DZisiaj jest czwartek. JUtro bedzie piatek."
print(tekst_bledu)
print(popraw_podwojne_poczatki(tekst_bledu))

print("zad5")


def zdania_od_duzej(tekst):
    if not isinstance(tekst, str):
        raise TypeError("Tekst musi byc napisem.")
    tekst_norm = tekst.strip().lower()

    def podnies_pierwsza(match):
        prefix, litera = match.groups()
        return prefix + litera.upper()

    return re.sub(r"(^|[.!?]\s+)([a-z])", podnies_pierwsza, tekst_norm)


tekst_zdania = (
    "to jest PIERWsze zdanie. DRUGIE zdanie TEZ tu jest! a TU? kolejny."
)
print(tekst_zdania)
print(zdania_od_duzej(tekst_zdania))

print("zad6")


def wczytaj_fasta_do_slownika(plik):
    sciezka = Path(plik)
    if not sciezka.exists():
        raise FileNotFoundError(f"Brak pliku: {plik}")
    dane = {}
    nazwa = None
    fragmenty = []
    with sciezka.open("r", encoding="utf-8") as handler:
        for linia in handler:
            linia = linia.strip()
            if not linia:
                continue
            if linia.startswith(">"):
                if nazwa is not None:
                    dane[nazwa] = "".join(fragmenty)
                nazwa = linia[1:].strip() or "bez_nazwy"
                fragmenty = []
            else:
                fragmenty.append(linia.replace(" ", "").upper())
        if nazwa is not None:
            dane[nazwa] = "".join(fragmenty)
    return dane


sciezka_fasta = Path("przyklad_zad6.fa")
if not sciezka_fasta.exists():
    sciezka_fasta.write_text(
        ">przyklad\nATGC\nATGC\nATGC\n", encoding="utf-8"
    )
print(wczytaj_fasta_do_slownika(sciezka_fasta))

print("zad7")


def filtruj_imiona(lista_osob):
    wzorzec = re.compile(r"^([A-Za-z])\w*\s+\1\w*$", re.I)
    return [osoba for osoba in lista_osob if wzorzec.search(osoba)]


lista_imion = ["Adam Nowak", "Kasia Klimczak", "Maria Rudzik"]
print(lista_imion)
print(filtruj_imiona(lista_imion))

print("zad8")


class DNA:
    def __init__(self, sekwencja):
        if not isinstance(sekwencja, str):
            raise TypeError("Sekwencja musi byc napisem.")
        self.sekwencja = sekwencja.upper()

    def komplementarna(self):
        dopelnienie = {"A": "T", "T": "A", "C": "G", "G": "C"}
        return "".join(dopelnienie.get(n, "N") for n in self.sekwencja)

    def ile_tymin(self):
        return self.sekwencja.count("T")


probna_dna = DNA("ATGCCTTAAGG")
print(f"Sekwencja: {probna_dna.sekwencja}")
print(f"Komplementarna: {probna_dna.komplementarna()}")
print(f"Liczba tymin: {probna_dna.ile_tymin()}")
