import pandas as pd
from numpy.linalg import qr, inv
import numpy as np

# Importujemy punkty
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1].flatten()

# Dodajemy kolumnę wartości „1”, aby wygenerować wyraz wolny
X_1 = np.vstack([X, np.ones(len(X))]).transpose()

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Obliczamy nachylenie i wyraz wolny za pomocą rozkładu QR
Q, R = qr(X_1)
b = inv(R).dot(Q.transpose()).dot(Y)
print(b) # [1.93939394, 4.73333333]
