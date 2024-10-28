import pandas as pd
from math import sqrt

# Wczytujemy dane
punkty = list(pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",").itertuples())

n = len(punkty)

# Linia regresji
m = 1.939
b = 4.733

# Obliczamy błąd standardowy estymacji
S_e = sqrt((sum((p.y - (m*p.x +b))**2 for p in punkty))/(n-2))

print(S_e)
# 1.87406793500129
