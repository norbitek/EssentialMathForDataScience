import random
def f(x):
    return (x - 3) ** 2 + 4

def dx_f(x):
    return 2*(x - 3)

# Tempo nauki
L = 0.001

# Liczba iteracji w metodzie gradientu prostego
iteracje = 100_000

# Zaczynamy od losowej wartości x
x = random.randint(-15,15)

for i in range(iteracje):
    # Znajdujemy nachylenie
    d_x = dx_f(x)
    # Aktualizujemy x, odejmując (tempo nauki) * (nachylenie)
    x -= L * d_x

print(x, f(x)) # wypisuje 2.999999999999889 4.0
