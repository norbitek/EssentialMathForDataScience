from math import log, exp
import pandas as pd

dane_pacjentow = pd.read_csv('https://bit.ly/33ebs2R', delimiter=",").itertuples()

b0 = -3.17576395
b1 = 0.69267212

def funkcja_logistyczna(x):
    p = 1.0 / (1.0 + exp(-(b0 + b1 * x)))
    return p

# Sumujemy logarytmy prawdopodobieństw
log_wiarygodnosci_dopasowania = 0.0
for p in dane_pacjentow:
    if p.y == 1.0:
        log_wiarygodnosci_dopasowania += log(funkcja_logistyczna(p.x))
    elif p.y == 0.0:
        log_wiarygodnosci_dopasowania += log(1.0 - funkcja_logistyczna(p.x))

print(log_wiarygodnosci_dopasowania) # -9.946161673231583
