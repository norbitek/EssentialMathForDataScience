import math
import random

import numpy as np
import pandas as pd

# Wykres Desmosa: https://www.desmos.com/calculator/6cb10atg3l

punkty = [p for p in pd.read_csv("https://tinyurl.com/y2cocoo7").itertuples()]

najlepsza_wiarygodnosc = -10_000_000
b0 = .01
b1 = .01

# Obliczamy maksymalną wiarygodność

def przewidz_prawdopodobienstwo(x):
    p = 1.0 / (1.0001 + math.exp(-(b0 + b1 * x)))
    return p

for i in range(1_000_000):

    # Wybieramy losowo wartość b0 lub b1 i losowo ją zmieniamy
    losowe_b = random.choice(range(2))

    losowa_poprawka = np.random.normal()

    if losowe_b == 0:
        b0 += losowa_poprawka
    elif losowe_b == 1:
        b1 += losowa_poprawka

    # Obliczamy łączną wiarygodność
    prawdziwe_estymacje = sum(math.log(przewidz_prawdopodobienstwo(p.x)) \
        for p in punkty if p.y == 1.0)
    falszywe_estymacje = sum(math.log(1.0 - przewidz_prawdopodobienstwo(p.x)) \
        for p in punkty if p.y == 0.0)

    laczna_wiarygodnosc = prawdziwe_estymacje + falszywe_estymacje

    # Jeśli wiarygodność się zwiększa, zachowujemy losową poprawkę. W przeciwnym razie wycofujemy zmiany.
    if najlepsza_wiarygodnosc < laczna_wiarygodnosc:
        najlepsza_wiarygodnosc = laczna_wiarygodnosc
    elif losowe_b == 0:
        b0 -= losowa_poprawka
    elif losowe_b == 1:
        b1 -= losowa_poprawka

print("1.0 / (1 + exp(-({0} + {1}*x))".format(b0, b1))
print("NAJLEPSZA WIARYGODNOŚĆ: {0}".format(math.exp(najlepsza_wiarygodnosc)))
