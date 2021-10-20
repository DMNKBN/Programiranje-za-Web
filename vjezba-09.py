#Python igra - "Pogodi Broj"
#Kod pomoću naredbe "break"

import random 

tajnibroj = random.randint (1,30)

while True:
    
    pogodi = int(input("Pogodi broj od 1 do 30, koji će se pojaviti na zaslonu:"))

    if pogodi == tajnibroj:
        print("Bravo, broj je pogođen.")
        break
    else:
        print("Netočno, broj nije pogođen.")