import pandas as pd
from math import log, exp
from scipy.stats import chi2

dane_pacjentow = list(pd.read_csv('https://bit.ly/33ebs2R', delimiter=",").itertuples())

# Deklarujemy dopasowaną regresję logistyczną
b0 = -3.17576395
b1 = 0.69267212

def funkcja_logistyczna(x):
    p = 1.0 / (1.0 + exp(-(b0 + b1 * x)))
    return p

# Obliczamy logarytm wiarygodności dopasowania
log_wiarygodnosci_dopasowania = sum(log(funkcja_logistyczna(p.x)) * p.y + \
                                log(1.0 - funkcja_logistyczna(p.x)) * (1.0 - p.y) \
                                for p in dane_pacjentow)

# Obliczamy logarytm wiarygodności bez dopasowania
wiarygodnosc = sum(p.y for p in dane_pacjentow) / len(dane_pacjentow)
log_wiarygodnosci = sum(log(wiarygodnosc) * p.y + \
                    log(1.0 - wiarygodnosc) * (1.0 - p.y) \
                    for p in dane_pacjentow)

# Obliczamy wartość p
chi2_wejscie = 2 * (log_wiarygodnosci_dopasowania - log_wiarygodnosci)
wartosc_p = chi2.pdf(chi2_wejscie, 1) # 1 stopień swobody (n - 1)
print(wartosc_p) # 0.0016604875618753787
