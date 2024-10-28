# Trzy egzaminy cząstkowe o wadze 0,20 każdy i egzamin końcowy o wadze 0,40
probka = [90, 80, 63, 87]
wagi = [.20, .20, .20, .40]

srednia_wazona = sum(s * w for s,w in zip(probka, wagi)) / sum(wagi)

print(srednia_wazona) # wypisuje 81.4
