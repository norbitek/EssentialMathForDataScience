from math import sqrt

proba = [1.78, 1.75, 1.72, 1.74, 1.77]

def srednia(wartosci):
    return sum(wartosci) /len(wartosci)

def wariancja_proby(wartosci):
    srednia = sum(wartosci) / len(wartosci)
    war = sum((v - srednia) ** 2 for v in wartosci) / len(wartosci)
    return war

def odch_std_proby(wartosci):
    return sqrt(wariancja_proby(wartosci))

srednia = srednia(proba)
odch_std = odch_std_proby(proba)

print("ŚREDNIA: ", srednia) # 1.752
print("ODCH STD: ", odch_std) # 0.02135415650406264
