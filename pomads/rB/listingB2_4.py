from scipy.stats import binom

n = 137
p = .40

p_niepojawienia_50_lub_wiecej = 0.0

for x in range(50,138):
    p_niepojawienia_50_lub_wiecej += binom.pmf(x, n, p)

print(p_niepojawienia_50_lub_wiecej) # 0.822095588147425
