import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wszystkie_dane = pd.read_csv("https://tinyurl.com/y2qmhfsr")

# Tempo uczenia określa, jak szybko zbliżamy się do rozwiązania.
# Jeśli jest za małe, algorytm będzie wykonywał się za długo.
# Jeśli jest za duże, prawdopodobnie przestrzelimy i nie znajdziemy rozwiązania.
L = 0.05

# Wyodrębniamy kolumny wejściowe, skalujemy czynnikiem 1/255
wszystkie_wejscia = (wszystkie_dane.iloc[:, 0:3].values / 255.0)
wszystkie_wyjscia = wszystkie_dane.iloc[:, -1].values

# Rozdzielamy dane na zbiór treningowy i testowy
X_trening, X_test, Y_trening, Y_test = train_test_split(wszystkie_wejscia, \
    wszystkie_wyjscia, test_size=1 / 3)
n = X_trening.shape[0]

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

# Pochodne funkcji aktywacji
d_relu = lambda x: x > 0
d_logistyczna = lambda x: np.exp(-x) / (1 + np.exp(-x)) ** 2

# Zwraca nachylenia dla wag i biasów
# przy użyciu reguły łańcuchowej
def prop_wsteczna(Z1, A1, Z2, A2, X, Y):
    dC_dA2 = 2 * A2 - 2 * Y
    dA2_dZ2 = d_logistyczna(Z2)
    dZ2_dA1 = w_wyjsciowa
    dZ2_dW2 = A1
    dZ2_dB2 = 1
    dA1_dZ1 = d_relu(Z1)
    dZ1_dW1 = X
    dZ1_dB1 = 1

    dC_dW2 = dC_dA2 @ dA2_dZ2 @ dZ2_dW2.T

    dC_dB2 = dC_dA2 @ dA2_dZ2 * dZ2_dB2

    dC_dA1 = dC_dA2 @ dA2_dZ2 @ dZ2_dA1

    dC_dW1 = dC_dA1 @ dA1_dZ1 @ dZ1_dW1.T

    dC_dB1 = dC_dA1 @ dA1_dZ1 * dZ1_dB1

    return dC_dW1, dC_dB1, dC_dW2, dC_dB2

# Schodzimy po gradiencie
for i in range(100_000):
    # losowo wybieramy jedną daną treningową
    idx = np.random.choice(n, 1, replace=False)
    X_proba = X_trening[idx].transpose()
    Y_proba = Y_trening[idx]

    # Przepuszczamy losowo wybrane dane przez sieć neuronową
    Z1, A1, Z2, A2 = prop_w_przod(X_proba)

    # Dystrybuujemy błąd poprzez propagację wsteczną
    # i zwracamy nachylenia dla wag i biasów
    dW1, dB1, dW2, dB2 = prop_wsteczna(Z1, A1, Z2, A2, X_proba, Y_proba)

    # Aktualizujemy wagi i biasy
    w_ukryta -= L * dW1
    b_ukryta -= L * dB1
    w_wyjsciowa -= L * dW2
    b_wyjsciowa -= L * dB2

# Obliczamy dokładność
test_prognoza = prop_w_przod(X_test.transpose())[3] # Bierzemy tylko A2
test_porownanie = np.equal((test_prognoza >= .5).flatten().astype(int), Y_test)
dokladnosc = sum(test_porownanie.astype(int) / X_test.shape[0])
print("DOKŁADNOŚĆ: ", dokladnosc)

# Interaktywne testowanie nowych kolorów
def przewidz_prawdopodobienstwo(r, g, b):
    X = np.array([[r, g, b]]).transpose() / 255
    Z1, A1, Z2, A2 = prop_w_przod(X)
    return A2

def przewidz_odcien_czcionki(r, g, b):
    wartosci_wyjsciowe = przewidz_prawdopodobienstwo(r, g, b)
    if wartosci_wyjsciowe > .5:
        return "CIEMNA"
    else:
        return "JASNA"

while True:
    kol_wej = input("Czcionka jasna czy ciemna? Wprowadź wartości R,G,B: ")
    (r, g, b) = kol_wej.split(",")
    print(przewidz_odcien_czcionki(int(r), int(g), int(b)))
