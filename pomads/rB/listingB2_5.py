from scipy.stats import beta

orly = 8
reszki = 2

p = 1.0 - beta.cdf(.5, orly, reszki)

print(p) # 0.98046875
