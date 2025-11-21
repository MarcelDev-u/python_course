import random
import re
import sys
from collections import Counter
from pathlib import Path

print("zad1")

S2 = "ATGGAAGAAtcACAGGCAGAACTCAATGtggAGCCCCCTCTGAGTCagGAGACATTttCCGACTTGTGGTGA"
S2 = S2.upper()
S2 = S2.replace("T", "U")
print(S2)

if S2.startswith("AUG"):
    print("Sekwencja zaczyna sie od kodonu start.")
else:
    print("Sekwencja nie zaczyna sie od kodonu start.")

stop_codony = ("UAA", "UGA", "UAG")
if any(S2.endswith(codon) for codon in stop_codony):
    print("Sekwencja konczy sie kodonem stop.")
else:
    print("Sekwencja nie konczy sie kodonem stop.")

podsekwencja = S2[3:-3]
print(f"Podsekwencja bez pierwszych i ostatnich 3 nukleotydow: {podsekwencja}")

ma_cuc = "CUC" in S2
print(f"Czy wystepuje CUC w S2? {ma_cuc}")

kodony = [S2[i : i + 3] for i in range(0, len(S2), 3) if len(S2[i : i + 3]) == 3]
print(f"Czy CUC wystepuje jako kodon? {'CUC' in kodony}")

print("zad2")

random.seed(42)
rzuty = [random.randint(1, 6) for _ in range(100)]
print(rzuty)

licznik = Counter(rzuty)
czestosci = {oczko: round(licznik.get(oczko, 0) / len(rzuty), 2) for oczko in range(1, 7)}
print(czestosci)

print("zad3")


def iloczyn_i_srednia_z_argow(args=None):
    dane = args if args is not None else sys.argv[1:]
    if len(dane) != 3:
        raise ValueError("Podaj dokladnie trzy liczby.")
    liczby = [float(element) for element in dane]
    iloczyn = liczby[0] * liczby[1] * liczby[2]
    srednia = sum(liczby) / 3
    return iloczyn, srednia


try:
    if len(sys.argv) > 1:
        iloczyn_arg, srednia_arg = iloczyn_i_srednia_z_argow()
        print(f"Iloczyn (argv): {iloczyn_arg}")
        print(f"Srednia (argv): {srednia_arg}")
    else:
        przyklad = ["2", "3", "4"]
        iloczyn_demo, srednia_demo = iloczyn_i_srednia_z_argow(przyklad)
        print(f"Iloczyn (demo {przyklad}): {iloczyn_demo}")
        print(f"Srednia (demo {przyklad}): {srednia_demo}")
except ValueError as err:
    print(f"Blad argumentow: {err}")

print("zad4")

folder_cwiczenia = Path("cwiczenia5")
folder_cwiczenia.mkdir(exist_ok=True)
plik_tekstowy = folder_cwiczenia / "notatki.txt"
plik_tekstowy.write_text("To jest przykladowa zawartosc pliku tekstowego.\n", encoding="utf-8")
print(f"Zapisano plik: {plik_tekstowy.resolve()}")

print("zad5")


def wczytaj_fasta(plik):
    sekwencje = []
    naglowek = None
    fragmenty = []
    with open(plik, "r", encoding="utf-8") as handler:
        for linia in handler:
            linia = linia.strip()
            if not linia:
                continue
            if linia.startswith(">"):
                if naglowek is not None:
                    sekwencje.append((naglowek, "".join(fragmenty)))
                naglowek = linia[1:] or "bez_nazwy"
                fragmenty = []
            else:
                fragmenty.append(linia)
        if naglowek is not None:
            sekwencje.append((naglowek, "".join(fragmenty)))
    return sekwencje


def przygotuj_przykladowe_fa(folder):
    folder.mkdir(parents=True, exist_ok=True)
    istnieja = list(folder.glob("*.fa"))
    if istnieja:
        return istnieja
    probki = {
        "przyklad1.fa": [(">seq1", "ATGCGA"), (">seq2", "TTTTGGGGA")],
        "przyklad2.fa": [(">seqA", "AUGGCUAUGCUA"), (">seqB", "GGGCCC")],
    }
    for nazwa_pliku, sekwencje in probki.items():
        linie = []
        for naglowek, sekwencja in sekwencje:
            linie.append(naglowek)
            linie.append(sekwencja)
        (folder / nazwa_pliku).write_text("\n".join(linie) + "\n", encoding="utf-8")
    return list(folder.glob("*.fa"))


def policz_srednia_dlugosc_fasta(folder):
    pliki = przygotuj_przykladowe_fa(folder)
    wszystkie_sekwencje = []
    for sciezka in pliki:
        wszystkie_sekwencje.extend(wczytaj_fasta(sciezka))
    dlugosci = [len(seq) for _, seq in wszystkie_sekwencje]
    if not dlugosci:
        return 0.0, None
    srednia_dlugosc = sum(dlugosci) / len(dlugosci)
    wynik = folder / "wszystkie_polaczone.fa"
    with open(wynik, "w", encoding="utf-8") as handler:
        for idx, (naglowek, seq) in enumerate(wszystkie_sekwencje, start=1):
            nazwa = naglowek or f"seq{idx}"
            handler.write(f">{nazwa}\n{seq}\n")
    return srednia_dlugosc, wynik


folder_fasta = folder_cwiczenia / "fasta"
srednia, plik_wyjsciowy = policz_srednia_dlugosc_fasta(folder_fasta)
print(f"Srednia dlugosc sekwencji: {srednia:.2f}")
if plik_wyjsciowy is not None:
    print(f"Polaczone sekwencje zapisano w pliku: {plik_wyjsciowy.resolve()}")
else:
    print("Brak sekwencji do zapisania.")

print("zad6")

wyrazenia = [
    ("ab*c", "a, potem zero lub wiele b, na koncu c", "abbbc"),
    ("ab+c", "a, co najmniej jedno b, na koncu c", "abbc"),
    ("ab?c", "a, opcjonalne b, na koncu c", "ac"),
    ("ab{3}c", "a, dokladnie trzy b, na koncu c", "abbbc"),
    ("ab{2,8}c", "a, od dwoch do osmiu b, na koncu c", "abbbbc"),
    ("a.*c", "a, dowolny ciag (takze pusty), na koncu c", "aXYZc"),
    ("a.+c", "a, co najmniej jeden dowolny znak, na koncu c", "abc"),
    ("a.?c", "a, zero lub jeden dowolny znak, na koncu c", "acc"),
    ("a.{3}c", "a, dokladnie trzy dowolne znaki, na koncu c", "a123c"),
    ("a.{2,8}c", "a, 2-8 dowolnych znakow, na koncu c", "aHELLOc"),
    ("a[bc]d", "a, nastepnie b lub c, na koncu d", "abd"),
    ("b[^a]d", "b, znak inny niz a, na koncu d", "bbd"),
    ("^a[bc]d$", "caly napis musi byc abd lub acd", "acd"),
    ("^a[^\\s]+", "napis zaczyna sie od a i co najmniej jednego nie-spacji", "alpha123"),
]
for pattern, opis, przyklad in wyrazenia:
    dop = bool(re.fullmatch(pattern, przyklad))
    print(f"{pattern:10} -> {opis}; przyklad: {przyklad}; dopasowanie: {dop}")

print("Przyklady re.findall / re.sub / re.search")
tekst_przyklad = "He rested his head on his hand"
t1 = re.findall(r"h..d", tekst_przyklad)
print(t1)
t2 = re.sub(r"h..d", "X", tekst_przyklad)
print(t2)
t3 = re.search(r"h..d", tekst_przyklad)
print(t3.span())

print("cwiczenie (regex odpowiednik startswith / endswith)")
probka = "ATGGTC"
print(f"Poczatek ATG? {bool(re.match(r'^ATG', probka))}")
print(f"Koniec TC? {bool(re.search(r'TC$', probka))}")

print("zad7")

zestawy = [
    (["mama", "mem", "mom"], r"^m[aeo]m(?:a)?$"),
    (["ac", "abc", "abbc", "abbbc"], r"^ab*c$"),
    (["tab", "teb", "teab", "teaab"], r"^te?a*b$"),
]
for slowa, wzorzec in zestawy:
    dopasowane = [s for s in slowa if re.fullmatch(wzorzec, s)]
    wszystko_ok = len(dopasowane) == len(slowa)
    print(f"{wzorzec}: {dopasowane} (wszystkie: {wszystko_ok})")

print("zad8")

tekst_marie = (
    "Marie Sklodowska Curie (1867-1934) was the first person ever to receive two Nobel Prizes: "
    "the first in 1903 in physics, shared with Pierre Curie (her husband) and Henri Becquerel "
    "for the discovery of the phenomenon of radioactivity, and the second in 1911 in chemistry "
    "for the discovery of the radioactive elements polonium and radium. "
    "Zrodlo: https://www.sciencehistory.org/historical-profile/marie-sklodowska-curie"
)
lata = re.findall(r"\b\d{4}\b", tekst_marie)
print(lata)

print("zad9")


def usun_male_litery(ciag):
    return re.sub(r"[a-z]", "", ciag)


przyklad_9 = "ATTTGgccTaC"
print(przyklad_9, "->", usun_male_litery(przyklad_9))

print("zad10")


def znajdz_emaile(tekst):
    wzor_email = r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}"
    return re.findall(wzor_email, tekst)


tekst_mailowy = (
    "Kontakt: joe.doe@example.com lub admin@mail.edu. "
    "Dodatkowo mozna pisac na wsparcie@firma.co.uk w razie problemow."
)
print(znajdz_emaile(tekst_mailowy))
