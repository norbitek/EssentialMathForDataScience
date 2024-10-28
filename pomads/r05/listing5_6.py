import pandas as pd
from numpy.linalg import inv
import numpy as np

# Importujemy punkty
df = pd.read_csv('https://bit.ly/3goOAnt', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1].flatten()

# Dodajemy kolumnę wartości „1”, aby wygenerować wyraz wolny
X_1 = np.vstack([X, np.ones(len(X))]).T

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Obliczamy współczynniki dla nachylenia i wyrazu wolnego
b = inv(X_1.transpose() @ X_1) @ (X_1.transpose() @ Y)
print(b) # [1.93939394, 4.73333333]

# Przewidujemy wartości y
y_przewidywana = X_1.dot(b)
