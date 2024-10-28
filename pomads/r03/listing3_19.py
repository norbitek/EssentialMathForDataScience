from scipy.stats import norm

# Średni czas zdrowienia z przeziębienia to 18 dni, z odchyleniem standardowym 1,5
srednia = 18
odch_std = 1.5

# Za jaką wartością x znajduje się 5% obszaru?
x = norm.ppf(.05, srednia, odch_std)

print(x) # 15.53271955957279
