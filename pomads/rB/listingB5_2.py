import pandas as pd

# Wczytujemy dane do ramki danych Pandas
df = pd.read_csv('https://bit.ly/3C8JzrM', delimiter=",")

# Wypisujemy korelacje między zmiennymi
korelacje = df.corr(method='pearson')
print(korelacje)

# WYNIKI:
#                x            y
# x  1.00000 0.92421
# y  0.92421 1.00000

# Testujemy pod kątem istotności statystycznej
from scipy.stats import t
from math import sqrt

# Rozmiar próby
n = df.shape[0]
print(n)
dolna_wk = t(n - 1).ppf(.025)
gorna_wk = t(n - 1).ppf(.975)

# Współczynnik korelacji
r = korelacje["y"]["x"]

# Przeprowadzamy test
wartosc_testowa = r / sqrt((1 - r ** 2) / (n - 2))

print("WARTOŚĆ TESTOWA: {}".format(wartosc_testowa))
print("ZAKRES KRYTYCZNY: {}, {}".format(dolna_wk, gorna_wk))

if wartosc_testowa < dolna_wk or wartosc_testowa > gorna_wk:
    print("KORELACJA POTWIERDZONA, MOŻNA ODRZUCIĆ H0")
else:
    print("KORELACJA NIEPOTWIERDZONA, NIE MOŻNA ODRZUCIĆ H0")

# Obliczamy wartość p
if wartosc_testowa > 0:
    wartosc_p = 1.0 - t(n-1).cdf(wartosc_testowa)
else:
    wartosc_p = t(n-1).cdf(wartosc_testowa)

# Test dwustronny, więc mnożymy przez 2
wartosc_p = wartosc_p * 2
print("WARTOŚĆ P: {}".format(wartosc_p))
"""
WARTOŚĆ TESTOWA: 23.835515323677328
ZAKRES KRYTYCZNY: -1.9844674544266925, 1.984467454426692
KORELACJA POTWIERDZONA, MOŻNA ODRZUCIĆ H0
P-VALUE: 0.0 (skrajnie mała)
"""
