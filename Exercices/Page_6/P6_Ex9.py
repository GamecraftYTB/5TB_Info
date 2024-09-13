# Code par Elvin Mouyart 5Tb
Fini = True
# P6_Ex9

import random

for i in range(1, 201):
    nbr = random.randint(0,101)
    if (nbr%3 != 0):
        print(f"{nbr} n'est pas un multiple de 3")