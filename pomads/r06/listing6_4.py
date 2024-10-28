import math
import pandas as pd

dane_pacjentow = pd.read_csv('https://bit.ly/33ebs2R', delimiter=",").itertuples()

b0 = -3.17576395
b1 = 0.69267212

def funkcja_logistyczna(x):
    p = 1.0 / (1.0 + math.exp(-(b0 + b1 * x)))
    return p

# Obliczamy prawdopodobieństwo łączne
pp_laczne = 1.0

for p in dane_pacjentow:
    if p.y == 1.0:
        pp_laczne *= funkcja_logistyczna(p.x)
    elif p.y == 0.0:
        pp_laczne *= (1.0 - funkcja_logistyczna(p.x))

print(pp_laczne) # 4.7911180221699105e-05
