# Code par Elvin Mouyart 5Tb
Fini = True
# P6_Ex8

total = 0
stop = False
while (stop==False):
    nbr = int(input("Entré un nombre > "))
    if (nbr>0):
        total += nbr
        print(f"Total = {total}")
    else:
        stop = True