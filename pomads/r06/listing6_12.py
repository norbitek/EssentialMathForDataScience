import pandas as pd
from math import log, exp

dane_pacjentow = list(pd.read_csv('https://bit.ly/33ebs2R', delimiter=",").itertuples())

wiarygodnosc = sum(p.y for p in dane_pacjentow) / len(dane_pacjentow)

log_wiarygodnosci = 0.0

for p in dane_pacjentow:
    if p.y == 1.0:
        log_wiarygodnosci += log(wiarygodnosc)
    elif p.y == 0.0:
        log_wiarygodnosci += log(1.0 - wiarygodnosc)

print(log_wiarygodnosci) # -14.341070198709906
