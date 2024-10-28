from scipy.stats import beta

a = 30
b = 6

p = 1.0 - beta.cdf(.90, a, b)

print(p) # 0.13163577484183708
