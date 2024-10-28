from scipy.stats import norm

x = norm.ppf(.95, loc=29.23, scale=1.37)
print(x) # 31.483449468923517
