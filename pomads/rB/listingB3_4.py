from scipy.stats import norm

srednia = 10345
odch_std = 552

p1 = 1.0 - norm.cdf(11641, srednia, odch_std)

# Wykorzystujemy symetrię
p2 = p1

# Wartość p obu „ogonów”
# Mógłbym również po prostu pomnożyć przez 2
wartosc_p = p1 + p2

print("Dwustronna wartość p:", wartosc_p)
if wartosc_p <= .05:
    print("Test dwustronny zaliczony")
else:
    print("Test dwustronny niezaliczony ")

# Dwustronna wartość p: 0.01888333596496139
# Test dwustronny zaliczony
