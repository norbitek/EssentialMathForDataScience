import pandas as pd
import numpy as np

# Dane wejściowe
dane = pd.read_csv('https://bit.ly/2KF29Bd', header=0)
X = dane.iloc[:, 0].values
Y = dane.iloc[:, 1].values

n = dane.shape[0] # wiersze

# Budujemy model
m = 0.0
b = 0.0

rozmiar_proby = 1 # Rozmiar próby
L = .0001 # Tempo nauki
epoki = 1_000_000 # Liczba iteracji

# Stochastyczny gradient prosty
for i in range(epoki):
    idx = np.random.choice(n, rozmiar_proby, replace=False)
    x_proba = X[idx]
    y_proba = Y[idx]
    
    # Bieżąca przewidywana wartość Y
    Y_pred = m * x_proba + b
    
    # Pochodna d/dm funkcji straty
    D_m = (-2 / rozmiar_proby) * sum(x_proba * (y_proba - Y_pred))
    
    # Pochodna d/db funkcji straty
    D_b = (-2 / rozmiar_proby) * sum(y_proba - Y_pred)
    m = m - L * D_m # Aktualizujemy m
    b = b - L * D_b # Aktualizujemy b
    
    # Wyświetlamy postępy
    if i % 10000 == 0:
        print(i, m, b)

print("y = {0}x + {1}".format(m, b))
