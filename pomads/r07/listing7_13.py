import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Wczytujemy dane
df = pd.read_csv('https://bit.ly/3GsNzGt', delimiter=",")

# Wyodrębniamy zmienne wyjściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
# Zauważ, że musimy przeskalować je liniowo
X = (df.values[:, :-1] / 255.0)

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna
Y = df.values[:, -1]

# Rozdzielamy dane na zbiór treningowy i testowy
X_trening, X_test, Y_trening, Y_test = train_test_split(X, Y, test_size=1/3)

nn = MLPClassifier(solver='sgd',
                   hidden_layer_sizes=(3, ),
                   activation='relu',
                   max_iter=100_000,
                   learning_rate_init=.05)

nn.fit(X_trening, Y_trening)

# Wypisujemy wagi i biasy
print(nn.coefs_ )
print(nn.intercepts_)

print("Ocena zbioru treningowego: %f" % nn.score(X_trening, Y_trening))
print("Ocena zbioru testowego: %f" % nn.score(X_test, Y_test))
