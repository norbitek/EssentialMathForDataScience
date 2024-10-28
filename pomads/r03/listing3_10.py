from scipy.stats import norm

srednia = 29.23
odch_std = 1.37

x = norm.cdf(29.23, srednia, odch_std)

print(x) # wypisuje 0.5
