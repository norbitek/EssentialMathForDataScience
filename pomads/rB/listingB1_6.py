from math import exp

p = 1000 # kapitał, kwota początkowa
r = .05 # stopa procentowa, roczna
t = 3.0 # czas, liczba lat

a = p * exp(r*t)

print(a) # wypisuje 1161.834242728283
