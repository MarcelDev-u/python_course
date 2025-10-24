def przywitaj(imie):
    """Zwraca powitanie dla podanego imienia."""
    return f"Cześć, {imie}!"


def podnies_do_kwadratu(liczba):
    """Podnosi liczbę do kwadratu."""
    return liczba**2


def wypisz_liste(elementy):
    """Łączy elementy listy w napis rozdzielony przecinkami."""
    return ", ".join(str(elem) for elem in elementy)
