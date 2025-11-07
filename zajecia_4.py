import time
from collections.abc import Iterable

print("zad1")


def bubble_sort_desc(values):
    if not isinstance(values, list):
        if isinstance(values, Iterable):
            values = list(values)
        else:
            raise TypeError(f"Oczekiwano listy liczb, dostano {type(values).__name__}")
    result = values.copy()
    n = len(result)
    while n > 1:
        swapped = False
        for i in range(n - 1):
            left = result[i]
            right = result[i + 1]
            if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
                raise TypeError(f"Elementy muszą być liczbami, trafiono {left!r} lub {right!r}")
            if left < right:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break
        n -= 1
    return result


sample_numbers = [1, 2, 300, 4, -6, 2, 8, 122, -55]
print(bubble_sort_desc(sample_numbers))

print("zad2")


def fib_iter(n):
    if not isinstance(n, int):
        raise TypeError("Argument musi byc liczba calkowita.")
    if n <= 0:
        raise ValueError("Argument musi byc dodatni.")
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def fib_rec(n):
    if not isinstance(n, int):
        raise TypeError("Argument musi byc liczba calkowita.")
    if n <= 0:
        raise ValueError("Argument musi byc dodatni.")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def compare_fib_timings(n=40):
    start = time.perf_counter()
    value_iter = fib_iter(n)
    time_iter = time.perf_counter() - start

    start = time.perf_counter()
    value_rec = fib_rec(n)
    time_rec = time.perf_counter() - start
    return (value_iter, time_iter), (value_rec, time_rec)


(val_i, time_i), (val_r, time_r) = compare_fib_timings()
print(f"Iteracyjne: {val_i} w {time_i:.7f}s")
print(f"Rekurencyjne: {val_r} w {time_r:.7f}s")

print("zad3")


def silnia_rekurencyjna(n):
    if not isinstance(n, int):
        raise TypeError("Argument musi byc liczba calkowita.")
    if n < 0:
        raise ValueError("Silnia niezdefiniowana dla liczb ujemnych.")
    if n in (0, 1):
        return 1
    return n * silnia_rekurencyjna(n - 1)


print(silnia_rekurencyjna(5))

print("zad4")


def sumy_kwadratow(list_of_lists):
    if not isinstance(list_of_lists, list):
        raise TypeError("Argumentem musi byc lista list.")
    wyniki = []
    for idx, sublist in enumerate(list_of_lists, start=1):
        if not isinstance(sublist, (list, tuple)):
            raise TypeError(f"Element nr {idx} nie jest lista: {sublist!r}")
        suma = 0
        for element in sublist:
            if not isinstance(element, (int, float)):
                raise TypeError(f"Element {element!r} nie jest liczba.")
            suma += element ** 2
        wyniki.append(suma)
    return wyniki


print(sumy_kwadratow([[1, 2], [3, 4, 5], [4]]))

print("zad5")


def policz_parzyste(n):
    if not isinstance(n, int):
        raise TypeError("Argument musi byc liczba calkowita.")
    if n < 0:
        raise ValueError("Argument musi byc nieujemny.")
    licznik = 0
    for i in range(n):
        if i % 2 == 0:
            licznik += 1
            print(f"Ta liczba jest podzielna przez 2: {i}")
    return licznik


print(policz_parzyste(10))

print("zad6")


def licz_tyminy_map(sekwencje):
    return list(map(lambda seq: seq.upper().count("T"), sekwencje))


def licz_tyminy_comp(sekwencje):
    return [seq.upper().count("T") for seq in sekwencje]


sekwencje_przyklad = ["ATTGC", "AGGC", "TTTGC"]
print(licz_tyminy_map(sekwencje_przyklad))
print(licz_tyminy_comp(sekwencje_przyklad))

print("zad7")


def filtruj_tg_filter(sekwencje):
    return list(filter(lambda seq: "TG" in seq.upper(), sekwencje))


def filtruj_tg_comp(sekwencje):
    return [seq for seq in sekwencje if "TG" in seq.upper()]


sekwencje_tg = ["ATGCC", "TATC", "GGATGGGG"]
print(filtruj_tg_filter(sekwencje_tg))
print(filtruj_tg_comp(sekwencje_tg))

print("zad8")


def potegi_listy_skladanej():
    return [x ** x for x in [1, 2, 3, 4, 5, 6]]


print(potegi_listy_skladanej())

print("zad9")


def posortuj_po_uracylach(sekwencje_raw):
    sekwencje = [elem.strip() for elem in sekwencje_raw.split(",") if elem.strip()]
    return sorted(sekwencje, key=lambda seq: seq.upper().count("U"), reverse=True)


rna_ciag = (
    "UGAGGUAGUAGGUUUUUUUUUU, UGAGGUAGUAGGUUGAUUUUUU, UGAGGUAGUAGGUUGUUUUUUU, "
    "UGAGGUAGUAGGUUGUGAUUUU, UGAGGUAGUAGGUUGUAUGGUU"
)
print(posortuj_po_uracylach(rna_ciag))
