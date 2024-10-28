from sympy import *

# "x" i wielkość przyrostu "s"
x, s = symbols('x s')

# deklarujemy funkcję
f = x**2

# nachylenie linii biegnącej między dwoma punktami oddalonymi o "s"
# używamy wzoru "różnica wysokości w pionie przez różnicę odległości w poziomie"
nachylenie_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# podstawiamy 2 za x
nachylenie_2 = nachylenie_f.subs(x, 2)

# obliczamy nachylenie w punkcie x = 2
# w nieskończoność zmniejszamy przyrost _s_ tak, aby zbliżał się do 0
wynik = limit(nachylenie_2, s, 0)

print(wynik) # 4
