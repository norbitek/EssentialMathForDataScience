# Trzy egzaminy cząstkowe o wadze 1 każdy i egzamin końcowy o wadze 2
probka = [90, 80, 63, 87]
wagi = [1.0, 1.0, 1.0, 2.0]

srednia_wazona = sum(s * w for s,w in zip(probka, wagi)) / sum(wagi)

print(srednia_wazona) # wypisuje 81.4
