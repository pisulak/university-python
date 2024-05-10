Paprotka Bransleya
Narysuj zbiór punktów tworzonych przez przekształcenia:
f1(x, y) = (0.85x + 0.04y, −0.04x + 0.85y + 1.6)
f2(x, y) = (−0.15x + 0.28y, 0.26x + 0.24y + 0.44)
f3(x, y) = (0.20x − 0.26y, 0.23x + 0.22y + 1.6)
f4(x, y) = (0, 0.16y)
Proporcje losowań równań:85:7:7:1
Punktem startowym jest punkt o współrzędnych p0 = (0, 0). Kolejne punkty na
wykresie tworzone są w sposób rekurencyjny:
pn+1(x, y) = fk(pn(x, y)),
lub nico prościej
(xn+1, yn+1) = fk(xn, yn),
gdzie k = 1, . . . , 4.
Liczba kroków (punktów) powinna wynosić około 1000. Do stworzenia wykresu
należy wykorzystać funkcje scatter z pakietu matplotlib. Kod w języku
Python należy napisać nie stosując instrukcji if oraz porównań logicznych.
1
