# Code par Elvin Mouyart 5Tb
Fini = False
# P11_Ex5

ventes=[ "Bruxelles",12897, "Charleroi",11782, "Namur", 17651,"Liège",17670]
moyenne=0

for i in range(len(ventes)%2):
    if i == 0:
        moyenne = moyenne + int(ventes[1])
    else:
        moyenne = moyenne + int(ventes[i*2+1])
moyenne = moyenne / (len(ventes)/2)
print(moyenne)
