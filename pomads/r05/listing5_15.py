import pandas as pd
from math import sqrt

# Importujemy punkty z pliku CSV
punkty = list(pd.read_csv("https://bit.ly/2KF29Bd").itertuples())
n = len(punkty)

licznik = n * sum(p.x * p.y for p in punkty) - \
          sum(p.x for p in punkty) * sum(p.y for p in punkty)

mianownik = sqrt(n*sum(p.x**2 for p in punkty) - sum(p.x for p in punkty)**2) \
          * sqrt(n*sum(p.y**2 for p in punkty) - sum(p.y for p in punkty)**2)

korelacja = licznik / mianownik

print(korelacja)

# WYNIK:
# 0.9575860952087218
