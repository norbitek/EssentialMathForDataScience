from scipy.stats import t
from math import sqrt

# Rozmiar próby
n = 10

dolna_wk = t(n-1).ppf(.025)
gorna_wk = t(n-1).ppf(.975)

# Współczynnik korelacji
# Obliczony na podstawie danych pod adresem https://bit.ly/2KF29Bd
r = 0.957586

# Przeprowadzamy test
wartosc_testowa = r / sqrt((1-r**2) / (n-2))

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
