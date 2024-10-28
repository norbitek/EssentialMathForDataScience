import pandas as pd
from scipy.stats import t
from math import sqrt

# Wczytujemy dane
punkty = list(pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",").itertuples())

n = len(punkty)

# Linia regresji
m = 1.75919315
b = 4.69359655

# Obliczamy przedział przewidywania dla x = 50
x_0 = 50
x_srednia = sum(p.x for p in punkty) / len(punkty)

wartosc_t = t(n - 2).ppf(.975)

blad_standardowy = sqrt(sum((p.y - (m * p.x + b)) ** 2 for p in punkty) / (n - 2))

margines_bledu = wartosc_t * blad_standardowy * \
   sqrt(1 + (1 / n) + (n * (x_0 - x_srednia) ** 2) / \
   (n * sum(p.x ** 2 for p in punkty) - \
   sum(p.x for p in punkty) ** 2))

przewidywane_y = m*x_0 + b

# Obliczamy przedział przewidywania
print(przewidywane_y - margines_bledu, przewidywane_y + margines_bledu)
# 50.792086501055955 134.51442159894404
