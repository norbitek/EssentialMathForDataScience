from sympy import *

# Deklarujemy zmienne w SymPy
x, i, n = symbols('x i n')

# Deklarujemy funkcję i zakres
f = x**2 + 1
dolny, gorny = 0, 1

# Obliczamy szerokość i wysokość każdego prostokąta o indeksie „i”
delta_x = ((gorny - dolny) / n)
x_i = (dolny + delta_x * i)
fx_i = f.subs(x, x_i)

# Iterujemy po wszystkich „n” prostokątach i sumujemy ich pola
liczba_prostokatow = Sum(delta_x * fx_i, (i, 1, n)).doit()

# Obliczamy pole, zwiększając liczbę
# prostokątów „n” do nieskończoności
pole = limit(liczba_prostokatow, n, oo)

print(pole) # wypisuje 4/3
