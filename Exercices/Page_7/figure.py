# Code par Elvin Mouyart 5Tb
Fini = True
# P7_Ex4

larg = int(input("Introduisez la largeur svp > "))
haut = int(input("Introduisez la hauteur svp > "))
print("X" * larg)
for i in range(haut-2):
    print("X" + " " * (larg - 2) + "X")
print("X" * larg)