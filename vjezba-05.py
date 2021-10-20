#Izradi program koji će generirati nasumičan broj od 1 do 10.
#Korisnik programa mora pokušati pogoditi odre0đeni broj.
#Ako je broj pogođen, napiši:"Bravo, broj je pogođen.".
#Inače, napiši:"Netočno, broj nije pogođen."

import random 

Broj = random.randint(1,10)

Pogodi = int(input("Pogodi broj od 1 do 10, koji će se pojaviti na zaslonu:"))

print(random.randrange(1,10))

if Pogodi == Broj:
    print("Bravo, broj je pogođen.")
else:
    print("Netočno, broj nije pogođen.")