import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# Wczytujemy dane
df = pd.read_csv('https://bit.ly/3ilJc2C', compression='zip', delimiter=",")

# Wyodrębniamy zmienne wejściowe (wszystkie wiersze, wszystkie kolumny oprócz ostatniej)
# Zauważ, że konieczne jest tu skalowanie liniowe
X = (df.values[:, :-1] / 255.0)

# Wyodrębniamy kolumnę wyjściową (wszystkie wiersze, ostatnia kolumna)
Y = df.values[:, -1]

# Określamy liczność każdej grupy, aby zagwarantować równomierne rozłożenie prób
print(df.groupby(["class"]).agg({"class" : [np.size]}))

# Rozdzielamy dane treningowe i testowe
# Zauważ, że używam parametru 'stratify', aby zagwarantować,
# że każda klasa będzie reprezentowana proporcjonalnie w obu zbiorach
X_trening, X_test, Y_trening, Y_test = train_test_split(X, Y, \
    test_size=.33, random_state=10, stratify=Y)

nn = MLPClassifier(solver='sgd',
                   hidden_layer_sizes=(100, ),
                   activation='logistic',
                   max_iter=480,
                   learning_rate_init=.1)

nn.fit(X_trening, Y_trening)

print("Ocena zbioru treningowego: %f" % nn.score(X_trening, Y_trening))
print("Ocena zbioru testowego: %f" % nn.score(X_test, Y_test))

# Wyświetlamy mapę cieplną
import matplotlib.pyplot as plt
fig, axes = plt.subplots(4, 4)

# Używamy globalnego minimum/maksimum, aby zagwarantować, że wszystkie wagi będą pokazywane w tej samej skali
vmin, vmax = nn.coefs_[0].min(), nn.coefs_[0].max()
for coef, ax in zip(nn.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin, vmax=.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
