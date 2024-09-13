# Code par Elvin Mouyart 5Tb
Fini = True
# P6_Ex7

import random

for i in range(1, 201):
    nbr = random.randint(0,101)
    if (nbr%2 == 0):
        print(f"{nbr} est impaire")