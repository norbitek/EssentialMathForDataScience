from math import exp

p = 100  # kapitał, kwota początkowa
r = .20  # stopa procentowa, roczna
t = 2.0  # czas, liczba lat

a = p * exp(r*t)

print(a) # wypisuje 149,18246976412703
