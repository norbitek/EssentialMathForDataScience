# Liczba zwierząt posiadanych przez każdą osobę
from collections import defaultdict

probka = [1, 3, 2, 5, 7, 0, 2, 3]

def dominanta(wartosci):
    wystapienia = defaultdict(lambda: 0)

    for s in wartosci:
        wystapienia[s] += 1
    
    najwiecej_wystapien = max(wystapienia.values())
    dominanty = [v for v in set(wartosci) if wystapienia[v] == najwiecej_wystapien]
    return dominanty

print(dominanta(probka)) # [2, 3]
