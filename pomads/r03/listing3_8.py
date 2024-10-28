from math import sqrt

# Liczba zwierząt posiadanych przez każdą osobę
dane = [0, 1, 5, 7, 9, 10, 14]

def wariancja(wartosci, czy_probka: bool = False):
    srednia = sum(wartosci) / len(wartosci)
    _wariancja = sum((v - srednia) ** 2 for v in wartosci) / (len(wartosci) - (1 if czy_probka else 0))
    return _wariancja

def odch_std(wartosci, czy_probka: bool = False):
    return sqrt(wariancja(wartosci, czy_probka))

print("WARIANCJA = {}".format(wariancja(dane, czy_probka=True))) # 24.95238095238095
print("ODCH STD = {}".format(odch_std (dane, czy_probka=True))) # 4.99523582550223
