# Liczba zwierząt domowych posiadanych przez każdą osobę
probka = [0, 1, 5, 7, 9, 10, 14]

def mediana(probka):
    uporzadkowane = sorted(probka)
    print(uporzadkowane)
    n = len(uporzadkowane)
    srodek = int(n / 2) - 1 if n % 2 == 0 else int(n/2)

    if n % 2 == 0:
        return (uporzadkowane[srodek] + uporzadkowane[srodek+1]) / 2.0
    else:
        return uporzadkowane[srodek]

print(mediana(probka)) # wypisuje 7
