# Liczba zwierząt posiadanych przez każdą osobę
dane = [0, 1, 5, 7, 9, 10, 14]

def wariancja(wartosci):
    srednia = sum(wartosci) / len(wartosci)
    _wariancja = sum((v - srednia) ** 2 for v in wartosci) / len(wartosci)
    return _wariancja

print(wariancja(dane)) # wypisuje 21.387755102040813
