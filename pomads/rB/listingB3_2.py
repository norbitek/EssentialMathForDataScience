from scipy.stats import norm

srednia = 42
odch_std = 8

x = norm.cdf(30, srednia, odch_std) - norm.cdf(20, srednia, odch_std)

print(x) # 0.06382743803380352
