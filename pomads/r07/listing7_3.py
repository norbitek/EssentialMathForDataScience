import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wszystkie_dane = pd.read_csv("https://tinyurl.com/y2qmhfsr")

# Wyodrębniamy kolumny wejściowe, skalujemy czynnikiem 1/255
wszystkie_wejscia = (wszystkie_dane.iloc[:, 0:3].values / 255.0)
wszystkie_wyjscia = wszystkie_dane.iloc[:, -1].values

# Rozdzielamy dane na zbiór treningowy i testowy
X_trening, X_test, Y_trening, Y_test = train_test_split(wszystkie_wejscia, \
    wszystkie_wyjscia, test_size=1/3)
n = X_trening.shape[0] # Liczba rekordów treningowych

# Budujemy sieć neuronową z losowo
# zainicjowanymi wagami i biasami
w_ukryta = np.random.rand(3, 3)
w_wyjsciowa = np.random.rand(1, 3)

b_ukryta = np.random.rand(3, 1)
b_wyjsciowa = np.random.rand(1, 1)

# Funkcje aktywacji
relu = lambda x: np.maximum(x, 0)
logistyczna = lambda x: 1 / (1 + np.exp(-x))

# Wprowadzamy dane wejściowe do sieci neuronowej, aby uzyskać wyjściowe przewidywania
def prop_w_przod(X):
    Z1 = w_ukryta @ X + b_ukryta
    A1 = relu(Z1)
    Z2 = w_wyjsciowa @ A1 + b_wyjsciowa
    A2 = logistyczna(Z2)
    return Z1, A1, Z2, A2

# Obliczamy dokładność
test_prognoza = prop_w_przod(X_test.transpose())[3] # Bierzemy tylko A2
test_porownanie = np.equal((test_prognoza >= .5).flatten().astype(int), Y_test)
dokladnosc = sum(test_porownanie.astype(int) / X_test.shape[0])
print("DOKŁADNOŚĆ: ", dokladnosc)
