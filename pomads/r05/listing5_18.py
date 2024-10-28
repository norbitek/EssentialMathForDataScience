import pandas as pd

# Wczytujemy dane do ramki danych Pandas
df = pd.read_csv('https://bit.ly/2KF29Bd', delimiter=",")

# Wypisujemy korelacje między zmiennymi
wsp_determinacji = df.corr(method='pearson') ** 2
print(wsp_determinacji)

# Wyniki:
#    x        y
# x  1.000000 0.916971
# y  0.916971 1.000000
