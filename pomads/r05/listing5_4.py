import pandas as pd

# Importujemy punkty
points = pd.read_csv("https://bit.ly/2KF29Bd").itertuples()

# Testujemy z określoną linią
m = 1.93939
b = 4.73333

suma_kwadratow = 0.0

# Obliczamy sumę kwadratów
for p in points:
    y_rzeczywista = p.y
    y_przewidywana = m*p.x + b
    reszta_do_kwadratu = (y_przewidywana - y_rzeczywista)**2
    suma_kwadratow += reszta_do_kwadratu

print("suma kwadratów = {}".format(suma_kwadratow))
# suma kwadratów = 28.096969704500005
