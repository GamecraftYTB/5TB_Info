# Code par Elvin Mouyart 5Tb
Fini = True
# P7_Ex1

import random
count = 0

for i in range(1,26):
    nbr = random.randint(1,101)
    if (nbr % 9 == 0):
        count+=1
        print(nbr)
print(f"Il y a eu {count} de chiffre divisible par 9")