from numpy.random import normal
import pandas as pd

# Importujemy punkty danych z pliku CSV
punkty = [p for p in pd.read_csv("https://bit.ly/2KF29Bd").itertuples()]

# Budujemy model
m = 0.0
b = 0.0

# Liczba iteracji
iteracje = 150000

# Liczba punktów
n = float(len(punkty))

# Inicjalizujemy naprawdę dużym kosztem,
# który na pewno zostanie zastąpiony
najlepszy_koszt = 10000000000000.0

for i in range(iteracje):

    # Losowo zmieniamy "m" i "b"
    zmiana_m = normal(0,1)
    zmiana_b = normal(0,1)
    m += zmiana_m
    b += zmiana_b

    # Obliczamy koszt, czy sumę błędów podniesionych do kwadratu
    nowy_koszt = 0.0
    for p in punkty:
        nowy_koszt += (p.y - (m * p.x + b)) ** 2

    # Jeśli koszt poprawił się,  zachowujemy nowe wartości.
    # W przeciwnym razie cofamy zmiany.
    if nowy_koszt < najlepszy_koszt:
        print("y = {0}x + {1}".format(m, b))
        najlepszy_koszt = nowy_koszt
    else:
        m -= zmiana_m
        b -= zmiana_b

print("y = {0}x + {1}".format(m, b))
