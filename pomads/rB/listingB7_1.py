import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Wczytujemy dane
df = pd.read_csv('https://tinyurl.com/y6r7qjrp', delimiter=",")

# Wyodrębniamy dane wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
X = df.values[:, :-1]

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Rozdzielamy dane treningowe i testowe
X_trening, X_test, Y_trening, Y_test = train_test_split(X, Y, test_size=1/3)

nn = MLPClassifier(solver='sgd',
                   hidden_layer_sizes=(3, ),
                   activation='relu',
                   max_iter=100_000,
                   learning_rate_init=.05)

nn.fit(X_trening, Y_trening)

print("Ocena zbioru treningowego: %f" % nn.score(X_trening, Y_trening))
print("Ocena zbioru testowego: %f" % nn.score(X_test, Y_test))

print("Macierz błędów:")
macierz = confusion_matrix(y_true=Y_test, y_pred=nn.predict(X_test))
print(macierz)
