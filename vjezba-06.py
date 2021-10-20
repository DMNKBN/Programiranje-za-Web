#Izradi program koji će uzimati 2 broja kao ulazne podatke.
#Nakon toga ponudi korisniku odabir matematičke operacije.

x = 1

y = 2

z = 3

t = 4

Broj1 = int(input("Unesi svoj prvi broj:"))

Broj2 = int(input("Unesi svoj drugi broj:"))

Operacija = int(input("Odaberi želiš li zbrojiti, oduzeti, pomnožiti ili podijeliti svoja dva unešena broja. Ukoliko brojeve želiš zbrojiti, unesi 1. Ukoliko brojeve želiš oduzeti, unesi 2. Ukoliko želiš brojeve pomnožiti unesi 3. Ukoliko brojeve želiš podijeliti unesi 3. Tvoja matematička operacija:"))

if Operacija == x:
    print(Broj1 + Broj2)
if Operacija == y:
    print(Broj1-Broj2)
if Operacija == z:
    print(Broj1 * Broj2)
if Operacija == t:
    print(Broj1 / Broj2)
