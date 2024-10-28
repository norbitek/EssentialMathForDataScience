# WYKRES: https://www.desmos.com/calculator/iildqi2vt7

from pulp import *

# Deklarujemy zmienne
x = LpVariable("x", 0) # 0<=x
y = LpVariable("y", 0) # 0<=y

# Definiujemy problem
prob = LpProblem("problem_fabryczny", LpMaximize)

# Definiujemy ograniczenia
prob += x + 3*y <= 20
prob += 6*x +2*y <= 45

# Definiujemy funkcję celu
prob += 200*x + 300*y

# Rozwiązujemy problem
status = prob.solve()
print(LpStatus[status])

# Wypisujemy wyniki: x = 5,9375, y = 4,6875
print(value(x))
print(value(y))
