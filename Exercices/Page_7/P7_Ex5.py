# Code par Elvin Mouyart 5Tb
Fini = True
# P7_Ex5

import random
count = 0
nbr = 0
while (nbr != 75):
    nbr = random.randint(1,101)
    count+=1
print(f"Il aurat fallut {count} essai(s) pour obtenir le nbr {nbr}")
