# Uśrednione próby z rozkładu jednostajnego dają rozkład normalny
import random
import plotly.express as px

rozmiar_probki = 31
liczba_probek = 1000

# Centralne twierdzenie graniczne, 1000 prób,
# każda z 31 liczbami losowymi od 0,0 do 1,0
wartosci_x = [(sum([random.uniform(0.0, 1.0) for i in range(rozmiar_probki)]) / \
   rozmiar_probki)
           for _ in range(liczba_probek)]

wartosci_y = [1 for _ in range(liczba_probek)]

px.histogram(x=wartosci_x, y = wartosci_y, nbins=20).show()
