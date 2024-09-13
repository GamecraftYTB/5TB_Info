# Code par Elvin Mouyart 5Tb
Fini = True
# P11_Ex1

nb=[15,89,5,99,23,78,12,33,68,16]
count=0
for i in range(len(nb) - 1):
    if (nb[i] >= 30):
        count+=1
        print(nb[i])
print(f"Il y a {count} nbr supérieur a 30")