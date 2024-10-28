import pandas as pd
from sklearn.linear_model import LogisticRegression

employee_data = pd.read_csv("https://tinyurl.com/y6r7qjrp")

# Wyodrębniamy kolumny zmiennych niezależnych
inputs = employee_data.iloc[:, :-1]

# Wyodrębniamy kolumnę zmiennej zależnej "did_quit" 
output = employee_data.iloc[:, -1]

# Budujemy regresję logistyczną
fit = LogisticRegression(penalty='none').fit(inputs.values, output.values)

# Wypisujemy współczynniki:
print("WSPÓŁCZYNNIKI: {0}".format(fit.coef_.flatten()))
print("WYRAZ WOLNY: {0}".format(fit.intercept_.flatten()))

# Funkcja do testowania nowych danych pracowników
def czy_zostanie(plec, wiek, awanse, lata_zatrudnienia):
    prognoza = fit.predict([[plec, wiek, awanse, lata_zatrudnienia]])
    prawdopodobienstwa = fit.predict_proba([[plec, wiek, awanse, lata_zatrudnienia]])
    if prognoza == [[1]]:
        return "ODEJDZIE: {0}".format(prawdopodobienstwa)
    else:
        return "ZOSTANIE: {0}".format(prawdopodobienstwa)

# Interaktywnie testujemy prognozę:
while True:
    n = input("Prognozuj, czy pracownik zostanie, czy odejdzie {płeć},{wiek},{awanse},{lata zatrudnienia}: ")
    (plec, wiek, awanse, lata_zatrudnienia) = n.split(",") 
    print(czy_zostanie(int(plec), int(wiek), int(awanse), int(lata_zatrudnienia)))
