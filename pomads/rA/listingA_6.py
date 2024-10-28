import math

def normalny_cdf(x: float, srednia: float, odch_std: float) -> float:
    return (1 + math.erf((x - srednia) / math.sqrt(2) / odch_std)) / 2

srednia = 29.23
odch_std = 1.37

x = normalny_cdf(30, srednia, odch_std) - normalny_cdf(28, srednia, odch_std)

print(x) # wypisuje 0.5283135419737843
