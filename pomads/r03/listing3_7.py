from math import sqrt 

# Liczba zwierząt posiadanych przez każdą osobę
dane = [0, 1, 5, 7, 9, 10, 14]

def wariancja(wartosci):
    srednia = sum(wartosci) / len(wartosci)
    _wariancja = sum((v - srednia) ** 2 for v in wartosci) / len(wartosci)
    return _wariancja

def odch_std(wartosci):
    return sqrt(wariancja(wartosci))

print(odch_std(dane)) # wypisuje 4.624689730353898
