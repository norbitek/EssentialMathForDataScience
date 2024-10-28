from scipy.stats import norm

# Średni czas zdrowienia z przeziębienia to 18 dni, z odchyleniem standardowym 1,5
srednia = 18
odch_std = 1.5

# Za jaką wartością x znajduje się 2,5% obszaru?
x1 = norm.ppf(.025, srednia, odch_std)

# Za jaką wartością x znajduje się 97,5% obszaru?
x2 = norm.ppf(.975, srednia, odch_std)

print(x1) # 15.060054023189918
print(x2) # 20.93994597681008
